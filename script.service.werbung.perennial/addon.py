import os, time, socket, urllib2 ,urllib , xbmc, xbmcaddon, xbmcgui, xbmcvfs , json ,threading 
import base64
ACTION_PREVIOUS_MENU = 110
ACTION_BACKSPACE = 110
ACTION_NAV_BACK = 92
ACTION_SELECT_ITEM = 7

ADD_ON_ID = 'script.video-werbung'
__addon__    = xbmcaddon.Addon()
version = __addon__.getAddonInfo('version')
name = __addon__.getAddonInfo('name')
id = __addon__.getAddonInfo('id')
token  = __addon__.getSetting('Security-Token')
username  = __addon__.getSetting('Username')
devicename = xbmc.getInfoLabel('System.FriendlyName')


class MyClass(xbmcgui.Window):
  def __init__(self):
    self.strActionInfo = xbmcgui.ControlLabel(100, 120, 200, 200, '', 'font13', '0xff00ff00')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Push BACK')
 
  def onAction(self, action):
    if action == ACTION_SELECT_ITEM:
      self.message('goodbye')
      self.close()
    #if action == ACTION_SELECT_ITEM:
    #  self.message('you pushed A')
 
  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" My message title", message)
	

 
	  
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
	dialog = xbmcgui.Dialog()
	dialog.notification('LOG',content,xbmcgui.NOTIFICATION_WARNING, 2000)
	#if not content:
	#mydisplay = MyClass()
	#mydisplay .doModal()
	#del mydisplay

		
	#text_file = open("Output.txt", "w")
	#text_file.write(content)
	#+text_file.close()
	#Time_Maker()
	
	
def Time_Maker():
	#dialog = xbmcgui.Dialog()
	#dialog.notification('LOG','manni',xbmcgui.NOTIFICATION_WARNING, 2000)
	threading.Timer(0.1, Time_Maker).start()
	
	
	
	
	
encoded = base64.b64encode('test apps Perennial AG')
dialog = xbmcgui.Dialog()
dialog.notification('LOG', encoded ,xbmcgui.NOTIFICATION_WARNING, 2000)
printit()
