import os, time, socket, urllib2 ,urllib , xbmc, xbmcaddon, xbmcgui, xbmcvfs , json ,threading 
import base64
ACTION_PREVIOUS_MENU = 110
ACTION_BACKSPACE = 110
ACTION_NAV_BACK = 92
ACTION_SELECT_ITEM = 7
ADD_ON_ID = 'script.video-werbung'
__addon__    = xbmcaddon.Addon()

version = __addon__.getAddonInfo('version')
path = __addon__.getAddonInfo('path')
name = __addon__.getAddonInfo('name')
id = __addon__.getAddonInfo('id')
token  = __addon__.getSetting('Security-Token')
username  = __addon__.getSetting('Username')
devicename = xbmc.getInfoLabel('System.FriendlyName')

def printit():
	threading.Timer(10.0, printit).start()
	Player = {"jsonrpc":"2.0","method":"Player.GetActivePlayers","id":1}
	method = json.loads(xbmc.executeJSONRPC(json.dumps(Player)))
	Time = {"jsonrpc":"2.0","method":"Player.GetProperties","id":1,"params":{"playerid":1,"properties":["playlistid","speed","position","totaltime","time"]}}
	istime = json.loads(xbmc.executeJSONRPC(json.dumps(Time)))
	stream ={"jsonrpc":"2.0","method":"Player.GetItem","id":1,"params":{"playerid":1,"properties":["title","season","episode","plot","runtime","showtitle","thumbnail"]}}
	isstream = json.loads(xbmc.executeJSONRPC(json.dumps(stream)))
	stream2= {"id":1,"jsonrpc":"2.0","result":[{"playerid":1,"type":"video"}]}
	isstream2 = json.loads(xbmc.executeJSONRPC(json.dumps(stream2)))
	url = 'http://136.243.130.66/werbesysteme/token.php'
	postdata = {'time':istime,'method':method,'InfoLabel':isstream,'InfoLabel2':isstream2,'devicename':devicename,'id':id,'name':name,'version':version,'token':token,'username':username}
	req = urllib2.Request(url)
	req.add_header('Content-Type','application/json')
	data = json.dumps(postdata)
	enc = data.encode()  # utf-8 by default
	database64 =  base64.encodestring(enc)
	response = urllib2.urlopen(req,database64)
	content = response.read()
        json_loads = json.loads(content)
	
	if (json_loads[0]['login'] == '0'):
		dialog = xbmcgui.Dialog()
		dialog.notification('LOG',"Anmeldefehler",xbmcgui.NOTIFICATION_WARNING, 2000)
	else:
		xbmc.executebuiltin(json_loads[0]['notification'])

encoded = base64.b64encode('test apps Perennial AG')
dialog = xbmcgui.Dialog()
dialog.notification('LOG', encoded ,xbmcgui.NOTIFICATION_INFO, 2000)
printit()
