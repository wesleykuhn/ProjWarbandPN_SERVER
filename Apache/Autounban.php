<?php
//Call each 30 minutes

date_default_timezone_set('Europe/Paris');
$date = date('Y-m-d');
$dt = new DateTime();
$time = $dt->format('H');
$time = $time . ":00";

$banlocation = "./Data/Banlist/";

$bans = scandir($banlocation);
foreach($bans as $ban) {
  $bancontent = file_get_contents($ban);
   $teile = explode("|", $line);
   if($teile[1] == $date) {
       if($teile[2] == $time) {
		   unlink($ban);
	   }
   }
}
?>