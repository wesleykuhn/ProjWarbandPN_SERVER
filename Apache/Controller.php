<?php
//Copyright (c) by Dominic Poppe / Illuminati / King Solutions / Infravider

//Read all Settings
include("./Data/Settings.php");

//Function List:
//DONE: 1 = Check Player Name and if Account is banned, Load Gear for Respawn
//DONE: 2 = Load Agent Data (Position)
//DONE: 3 = Save Player
//DONE: 4 = Kill Player
//DONE: 5 = Withdraw
//DONE: 6 = Deposit
//DONE: 7 = Ban a player permanent

//Common Done List:
//DONE: All kinds of logging
//DONE: Auto-Unban Cronjob (call each 30 minutes)
//DONE: Banning
//DONE: Panel (transform from PWSS style to this new system)

//Missing: API
//Missing: Panel - Player Name Search and list on Account?!

//Output List:
//DONE: -2 = Server Password is wrong
//DONE: -1 = Player Name is owned by other Player = Kick -> Done
//DONE: 0 = Account loaded = Parse Equipment of Player -> Done
//DONE: 1 = Parse Position, HP and Food to the Agent
//DONE: 2 = Save done
//DONE: 3 = Withdraw done
//DONE: 4 = Withdraw failed
//DONE: 5 = Deposit done
//DONE: 6 = Deposit failed
//DONE: 7 = Banned
//DONE: 8 = Kick player because ban!
//DONE: 9 = IP Banned

if (empty($_GET)) {
	echo "Fail";
	exit;
}

$securitypassword = $_GET["scpass"];
if($securitypassword == $settingspassword) {
	
} else {
	echo "-2";
	exit;
}

$Function = $_GET["function"];
$Player_ID = $_GET["playerid"];

if($Function == 7) {
	$GUID = $_GET["guid"];
	$ban_data = $_GET["bandata"];
	$banfile = "./Data/Banlist/$GUID" . ".json";
	
	if (strpos($ban_data, 'Never') !== false) {
		file_put_contents($banfile, $ban_data);
		echo "8|$Player_ID|$ban_data";
		exit;
	} else {
		$ban_data_array = explode("|", $ban_data);
		$ban_reason = $ban_data_array[0];
		$ban_days = $ban_data_array[1];
		$ban_time = $ban_data_array[2];
		$ban_admin = $ban_data_array[3];
		$ban_time_new = $ban_time . ":00";
		date_default_timezone_set('Europe/Paris');
		$date = date('Y-m-d');
		$days = $ban_days;
		$unbandate = date('Y-m-d', strtotime($date. ' + '.$days.' days'));
		$ban_data = str_replace("|" . $ban_days . "|", "|" . $unbandate . "|", $ban_data);
		$ban_data = str_replace("|" . $ban_time . "|", "|" . $ban_time_new . "|", $ban_data);
		file_put_contents($banfile, $ban_data);
		$playerHistoryAddon = "$ban_admin did ban $GUID at $date until $unbandate because: $ban_reason";
		file_put_contents("./Data/Banlist/$GUID" . "-history.txt", $playerHistoryAddon . "\r\n", FILE_APPEND);
		
		echo "8|$Player_ID|$ban_data";
		exit;
	}
}

if($Function == 6) {
	$GUID = $_GET["guid"];
	$to_put_on = $_GET["putonbank"];
	$accountfile = "./Data/Accounts/$GUID" . ".json";
	$userContent = file_get_contents($accountfile);
	$userContentArray = json_decode($userContent);
	$bank = $userContentArray->{'bank'};

	if($to_put_on == 0) {
		echo "6|$Player_ID"; //Player has no gold on him
		exit;
	} else {
		$bank = $bank + $to_put_on;
		$userContentArray->{'bank'} = "$bank";
		$userContentArray->{'carried'} = "0";
		$json = json_encode($userContentArray);
		file_put_contents($accountfile, $json);
		echo "5|$Player_ID|$bank";
	}
}

if($Function == 5) {
	$GUID = $_GET["guid"];
	$accountfile = "./Data/Accounts/$GUID" . ".json";
	$userContent = file_get_contents($accountfile);
	$userContentArray = json_decode($userContent);
	$bank = $userContentArray->{'bank'};
	
	if($bank > 0) {
		if($bank > 5000) {
			$banknew = $bank - 5000;
			$userContentArray->{'bank'} = "$banknew";
			$json = json_encode($userContentArray);
			file_put_contents($accountfile, $json);
			echo "3|$Player_ID|5000|$banknew";
			exit;
		} else {
			$userContentArray->{'bank'} = "0";
			$json = json_encode($userContentArray);
			file_put_contents($accountfile, $json);
			echo "3|$Player_ID|$bank|$banknew";
			exit;
		}
	} else {
		echo "-4|$Player_ID"; //Player has no gold on his bank!
		exit;
	}
}

if($Function == 4) {
	$GUID = $_GET["guid"];
	$accountfile = "./Data/Accounts/$GUID" . ".json";
	$userContent = file_get_contents($accountfile);
	$userContentArray = json_decode($userContent);
	$userContentArray->{'head'} = "-1";
	$userContentArray->{'body'} = "-1";
	$userContentArray->{'foot'} = "-1";
	$userContentArray->{'gloves'} = "-1";
	$userContentArray->{'slot1'} = "-1";
	$userContentArray->{'slot2'} = "-1";
	$userContentArray->{'slot3'} = "-1";
	$userContentArray->{'slot4'} = "-1";
	$userContentArray->{'horse'} = "-1";
	$userContentArray->{'health'} = $respawn_hp;
	$userContentArray->{'food'} = $respawn_food;
	$userContentArray->{'x'} = "0";
	$userContentArray->{'y'} = "0";
	$userContentArray->{'z'} = "0";
	$userContentArray->{'horsehealth'} = "0";
	$json = json_encode($userContentArray);
	file_put_contents($accountfile, $json);
	echo "2";
	exit;
}

if($Function == 3) {
	$GUID = $_GET["guid"];
	$accountfile = "./Data/Accounts/$GUID" . ".json";
	$userContent = file_get_contents($accountfile);
	$userContentArray = json_decode($userContent);
	$userContentArray->{'carried'} = $_GET["d1"];
	$userContentArray->{'head'} = $_GET["d2"];
	$userContentArray->{'body'} = $_GET["d3"];
	$userContentArray->{'foot'} = $_GET["d4"];
	$userContentArray->{'gloves'} = $_GET["d5"];
	$userContentArray->{'slot1'} = $_GET["d6"];
	$userContentArray->{'slot2'} = $_GET["d7"];
	$userContentArray->{'slot3'} = $_GET["d8"];
	$userContentArray->{'slot4'} = $_GET["d9"];
	$userContentArray->{'horse'} = $_GET["d10"];
	$userContentArray->{'troop'} = $_GET["d11"];
	$userContentArray->{'faction'} = $_GET["d12"];
	$userContentArray->{'health'} = $_GET["d13"];
	$userContentArray->{'food'} = $_GET["d14"];
	$userContentArray->{'x'} = $_GET["d15"];
	$userContentArray->{'y'} = $_GET["d16"];
	$userContentArray->{'z'} = $_GET["d17"];
	$userContentArray->{'horsehealth'} = $_GET["d18"];
	$json = json_encode($userContentArray);
	file_put_contents($accountfile, $json);
	echo "2";
	exit;
}

if($Function == 2) {
	$GUID = $_GET["guid"];
	$Agent_ID = $_GET["agentid"];
	$accountfile = "./Data/Accounts/$GUID" . ".json";
	$userContent = file_get_contents($accountfile);
	$userContentArray = json_decode($userContent);
	$x = $userContentArray->{'x'};
	$y = $userContentArray->{'y'};
	$z = $userContentArray->{'z'};
	$horsehealth = $userContentArray->{'horsehealth'};
	$health = $userContentArray->{'health'};
	$food = $userContentArray->{'food'};
	echo "1|$Agent_ID|$x|$y|$z|$horsehealth|$health|$food";
	exit;
}

if($Function == 1) {
	$GUID = $_GET["guid"];
	$Username = $_GET["username"];
	$userip = $_GET["userip"];
	$accountfile = "./Data/Accounts/$GUID" . ".json";
	$banfile = "./Data/Banlist/$GUID" . ".json";
	if (file_exists($banfile)) {
		$bandata = file_get_contents($banfile);
		$bandataarray = explode("|", $bandata);
		$banreason = $bandataarray[0];
		$unbandate = $bandataarray[1];
		$unbantime = $bandataarray[2];
		$admin = $bandataarray[3];
		
		echo "7|$Player_ID|$banreason|$unbandate|$unbantime|$admin";
		exit;
	} else {
		if(file_exists("./Data/IPBanlist/$userip" . ".json")) {
			echo "9|$Player_ID";
			exit;
		}
		if (file_exists($accountfile)) {
			//User has an account, check first if he can use the username
			$check_valid = 0;
			$playernamefile = "./Data/Player Names/$Username-$GUID" . ".json";
			if(file_exists($playernamefile)) {
				$playerNameOwner = file_get_contents($playernamefile);
				if($playerNameOwner == $GUID) {
					$check_valid = 1;
				}
			} else {
				file_put_contents($playernamefile, $GUID);
				$check_valid = 1;
			}
			if($check_valid == 0) {
				echo "-1|$Player_ID";
				exit;
			}
			
			//If continue, the player is allowed to use the Player Name
			$userContent = file_get_contents($accountfile);
			$userContentArray = json_decode($userContent);
			$bank = $userContentArray->{'bank'};
			$carried = $userContentArray->{'carried'};
			$head = $userContentArray->{'head'};
			$body = $userContentArray->{'body'};
			$foot = $userContentArray->{'foot'};
			$gloves = $userContentArray->{'gloves'};
			$weapon1 = $userContentArray->{'slot1'};
			$weapon2 = $userContentArray->{'slot2'};
			$weapon3 = $userContentArray->{'slot3'};
			$weapon4 = $userContentArray->{'slot4'};
			$horse = $userContentArray->{'horse'};
			$troop = $userContentArray->{'troop'};
			$faction = $userContentArray->{'faction'};
			$health = $userContentArray->{'health'};
			$food = $userContentArray->{'food'};
			$token = $userContentArray->{'token'};
			$adminlevel = $userContentArray->{'adminlevel'};
			//HP, Food and Position is loaded when Agent does Spawn!
			echo "0|$Player_ID|$bank|$carried|$head|$body|$foot|$gloves|$weapon1|$weapon2|$weapon3|$weapon4|$horse|$troop|$faction|$health|$food|$token|$adminlevel";
			exit;
			} else {
				//User has no account so create one but check first if he can use the Player Name
				$check_valid = 0;
				$playernamefile = "./Data/Player Names/$Username-$GUID" . ".json";
				if(file_exists($playernamefile)) {
					$playerNameOwner = file_get_contents($playernamefile);
					if($playerNameOwner == $GUID) {
						$check_valid = 1;
					}
				} else {
					file_put_contents($playernamefile, $GUID);
					$check_valid = 1;
				}
				if($check_valid == 0) {
					echo "-1|$Player_ID";
					exit;
				}
				
				function generateRandomString($length = 11) {
				$characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
				$charactersLength = strlen($characters);
				$randomString = '';
				for ($i = 0; $i < $length; $i++) {
					$randomString .= $characters[rand(0, $charactersLength - 1)];
				}
				return $randomString;
				}

				$token = generateRandomString(6);
				
				//Player can use the Name, means: Create him a new Account
				$nothing = "-1";
				$creation = array (
					"bank" => "$start_bank",
					"carried" => "$start_carried_gold",
					"head" => "$nothing",
					"body" => "$nothing",
					"foot" => "$nothing",
					"gloves" => "$nothing",
					"slot1" => "$nothing",
					"slot2" => "$nothing",
					"slot3" => "$nothing",
					"slot4" => "$nothing",
					"horse" => "$nothing",
					"health" => "100",
					"food" => "20",
					"x" => "$nothing",
					"y" => "$nothing",
					"z" => "$nothing",
					"troop" => "4",
					"horsehealth" => "0",
					"faction" => "0",
					"token" => "$token",
					"adminlevel" => "0"
				);
				
				$json = json_encode($creation);
				file_put_contents($accountfile, $json);
				
				echo "0|$Player_ID|$start_bank|$start_carried_gold|-1|-1|-1|-1|-1|-1|-1|-1|-1|4|0|0|$token";
				exit;
			}
	}
}
?>