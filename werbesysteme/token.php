<?php
include('config.php');
$db_link = mysql_connect (MYSQL_HOST, 
                           MYSQL_USER, 
                           MYSQL_PASSWROD, 
                           MYSQL_DATENBANK);
 
mysql_select_db(MYSQL_DATENBANK, $db_link) or die('Could not select database.');
if ( !$db_link )
{
die('keine Verbindung möglich: ' . mysql_error());
}
function version ()
{
$result = mysql_query("SELECT option_value FROM options WHERE option_name = 'version'");
if (!$result) {
    echo 'Konnte Abfrage nicht ausführen: ' . mysql_error();
    exit;
}
$row = mysql_fetch_row($result);
return ($row[0]);
}

function User_Check ($user,$token)
{
$result = mysql_query("SELECT * FROM `users` WHERE `user_login` = '".$user."' AND user_token = '".$token."' AND user_status=1 LIMIT 1");
if (!$result) {
	echo 'Konnte Abfrage nicht ausführen: ' . mysql_error();
 exit;
}
$row = mysql_fetch_row($result);
if( empty( $row ) )
{
	return (0);
}else{
	return (1);
}

}
$data = json_encode(file_get_contents('php://input'));
$newData = base64_decode(json_decode($data, true));
$my_array_data = json_decode($newData, TRUE);
$version = version ();
if(User_Check($my_array_data["username"],$my_array_data["token"]) === 1){
if($my_array_data["version"] === $version){
$title = $my_array_data["InfoLabel"]["result"]["item"]["title"];
$label = $my_array_data["InfoLabel"]["result"]["item"]["label"];	
$minutes = $my_array_data["time"]["result"]["time"]["minutes"];
$seconds = $my_array_data["time"]["result"]["time"]["seconds"];
	

$file = 'people.json';
$title = $title;
if($title === "07.04 - BLOCKBUSTAZ: BLOCKBUSTAZ - 3. Versicherung"){
	echo $minutes.":".$seconds;

}
//print_r($title);

file_put_contents($file, $newData);
}else{
print_r("für die version ".$my_array_data["version"]." ist ein update verfügbar");
}
	
	
}


?>