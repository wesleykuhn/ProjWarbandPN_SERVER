from header_common import *
from header_items import *
from header_troops import *
from header_skills import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id
#  2) Toop name (string)
#  3) Plural troop name (string)
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene and entry
#   5.1) Scene (only applicable to heroes)
#   5.2) Entry point using the entry() function: for example, entry(15)
#  6) Reserved (int). Put constant "reserved" or 0
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
####################################################################################################################

def wp(x):
  return wp_one_handed(x)|wp_two_handed(x)|wp_polearm(x)|wp_archery(x)|wp_firearm(x)|wp_throwing(x)

def wpe(m,a,c,t):
  return wp_one_handed(m)|wp_two_handed(m)|wp_polearm(m)|wp_archery(a)|wp_firearm(c)|wp_throwing(t)

def wpex(o,w,p,a,c,t):
  return wp_one_handed(o)|wp_two_handed(w)|wp_polearm(p)|wp_archery(a)|wp_firearm(c)|wp_throwing(t)

def wp_melee(x):
  return wp_one_handed(x + 20)|wp_two_handed(x)|wp_polearm(x + 10)

reserved = 0
no_scene = 0

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

bot_custom_face_1 = 0x000000000010200036db6db6db6db6db00000000001db6db0000000000000000
bot_custom_face_2 = 0x0000000fff1076e96baeb6db6db6d92d00000000001f6db60000000000000000

default_face_1 = 0x0000000400000001124000000020000000000000001c00800000000000000000
default_face_2 = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

# troops have 30 charisma and 10 weapon master to stop the game engine from adding random skill levels
pw_attr = cha_30|level(1)
knows_pw = knows_weapon_master_10

troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,0, [],
   str_15|agi_15|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all,0,0,0, [],
   str_14, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all,0,0,0, [],
   str_14, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,0,[],0,0,0,0],
####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################

  # TROOPS FROM PW MODIFIED BY PN
  #   - Militia
  #   - Lancer
  #   - Sailor
  #   - Rufian
  #   - Brigand
  #   - Mercenary

  # NEW TROOPS OF PN
  #   - Line Infantry
  #   - Light Infantry
  #   - Grenadier
  #   - Infantry Musician
  #   - Infantry Officer
  #   - Hussar
  #   - Cuirassier
  #   - Dragoon
  #   - Cavalry Musician
  #   - Cavalry Officer
  #   - Artillery
  #   - Artillery Officer
  #   - Captain

  # TROOPS UNUSED BY PN
  #   - Footman
  #   - Archer
  #   - Crossbowman
  #   - Man At Arms
  #   - Sargeant

  ["peasant","Peasant","a peasant",tf_guarantee_all,0,0,"fac_commoners",
    ["itm_leather_vest_plain","itm_civil_coat1", "itm_civil_coat2", "itm_civil_fur_cloth_a", "itm_civil_peasant_shirt_1",
      "itm_leather_boots", "itm_hide_boots", "itm_hunter_boots", "itm_old_knife", "itm_russian_peasant_axe", "itm_hatchet", "itm_russian_peasant_knife",
      "itm_knife", "itm_cheap_scythe", "itm_small_mining_pick"],
    str_8|agi_8|pw_attr,wpex(50,30,30,0,0,30),knows_pw|knows_power_strike_1|knows_power_draw_1|knows_labouring_2|knows_tailoring_1|knows_riding_1,default_face_1,default_face_2
  ],

  ["serf","Serf","a serf",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_fur_coat","itm_leather_vest_plain","itm_civil_coat1", "itm_civil_coat2", "itm_civil_fur_cloth_a", "itm_civil_peasant_shirt_1",
      "itm_leather_boots", "itm_hide_boots", "itm_hunter_boots", "itm_old_knife", "itm_russian_peasant_axe", "itm_hatchet", "itm_russian_peasant_knife",
      "itm_knife", "itm_cheap_scythe", "itm_small_mining_pick", "itm_fishing_spear"],
   str_5|agi_5|pw_attr,wpex(30,30,30,0,0,50),knows_pw|knows_power_strike_1|knows_power_draw_1|knows_labouring_5|knows_engineer_1|knows_tailoring_2|knows_herding_3|knows_riding_1,default_face_1,default_face_2],

  ["militia","Militia","a militia",tf_guarantee_all,0,0,"fac_commoners",
    ["itm_civil_peasant_hat", "itm_civil_militia_hat", "itm_civil_peasant_hat2", "itm_civil_peasant_hat3", "itm_civil_fur_hat",
      "itm_civil_militia_uniform", "itm_civil_coat1", "itm_civil_coat2", "itm_civil_militia_pants1", "itm_civil_militia_pants2", 
      "itm_russian_peasant_pitchfork", "itm_russian_peasant_club", "itm_russian_peasant_birch_club", "itm_russian_peasant_pike", "itm_russian_peasant_rogatina"],
    str_11|agi_10|pw_attr,wpex(70,40,70,40,70,20),knows_pw|knows_ironflesh_2|knows_power_strike_1|knows_power_draw_1|knows_athletics_1|knows_engineer_1|knows_riding_1|knows_labouring_2|knows_herding_2,default_face_1,default_face_2
  ],

  ["huntsman","Huntsman","a huntsman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_fur_hat", "itm_leather_jacket", "itm_civil_fur_cloth_a", "itm_hunter_boots", "itm_short_bow", "itm_arrows"],
   str_11|agi_9|pw_attr,wpex(60,35,50,100,100,50),knows_pw|knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_riding_1|knows_labouring_2|knows_herding_3,default_face_1,default_face_2],

  ["craftsman","Craftsman","a craftsman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_3", "itm_civil_waistcoat_custom_4", "itm_leather_boots"],
   str_8|agi_8|pw_attr,wpex(50,30,30,20,20,20),knows_pw|knows_power_strike_2|knows_riding_1|knows_engineer_3|knows_labouring_1|knows_tailoring_5,default_face_1,default_face_2],

  ["healer","Healer","a healer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_3", "itm_civil_waistcoat_custom_4", "itm_leather_boots"],
   str_8|agi_8|pw_attr,wpex(40,10,20,0,0,5),knows_pw|knows_riding_1|knows_wound_treatment_1|knows_labouring_1|knows_tailoring_2|knows_herding_1,default_face_1,default_face_2],

  # (!) NOT USED
  ["footman","Footman","a footman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_ragged_woolen_cap","itm_old_coarse_tunic","itm_old_tabard","itm_tattered_wrapping_boots","itm_crude_spear","itm_rusty_sword","itm_chipped_falchion"],
   str_15|agi_14|pw_attr,wpex(100,100,130,10,45,80),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_shield_1|knows_athletics_5|knows_riding_2|knows_sailing_3,default_face_1,default_face_2],

  # PN INFANTRY BEGIN
  ["line_infantry","Line Infantry","a line infantry",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_inf_uniform_a", "itm_civil_inf_pants_a", "itm_training_musket"],
   str_13|agi_13|pw_attr,wpex(50,0,140,0,120,50),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_riding_1|knows_sailing_1,default_face_1,default_face_2],

  ["light_infantry","Light Infantry","a light infantry",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_inf_uniform_a", "itm_civil_inf_pants_a", "itm_training_musket"],
   str_11|agi_15|pw_attr,wpex(50,0,100,0,150,50),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_athletics_6|knows_riding_1|knows_sailing_1|knows_engineer_1,default_face_1,default_face_2],

  ["grenadier","Grenadier","a grenadier",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_inf_uniform_a", "itm_civil_inf_pants_a", "itm_training_musket"],
   str_15|agi_11|pw_attr,wpex(50,0,160,0,120,160),knows_pw|knows_ironflesh_5|knows_power_strike_3|knows_athletics_3|knows_riding_1|knows_sailing_1,default_face_1,default_face_2],

  ["infantry_musician","Infantry Musician","an infantry musician",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_inf_uniform_a", "itm_civil_inf_pants_a", "itm_training_musket"],
   str_12|agi_13|pw_attr,wpex(70,0,70,0,50,0),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_athletics_3|knows_riding_1,default_face_1,default_face_2],

  ["infantry_officer","Infantry Officer","an infantry officer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_1", "itm_civil_noble_pants_grey", "itm_french_old_pistol_1766", "itm_bullets", "itm_spyglass"],
   str_14|agi_14|pw_attr,wpex(160,50,100,0,90,50),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_athletics_3|knows_riding_2,default_face_1,default_face_2],
  # PN INFANTRY END

  # (!) NOT USED
  ["archer","Archer","an archer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_tattered_headcloth","itm_old_coarse_tunic","itm_old_tabard","itm_tattered_wrapping_boots","itm_crude_bow","itm_bent_arrows","itm_blunt_falchion"],
   str_14|agi_14|pw_attr,wpex(90,60,70,150,50,50),knows_pw|knows_ironflesh_4|knows_power_strike_2|knows_power_draw_4|knows_athletics_4|knows_riding_2|knows_sailing_3,default_face_1,default_face_2],
  # (!) NOT USED
  ["crossbowman","Crossbowman","a crossbowman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_woolen_cap","itm_old_coarse_tunic","itm_old_tabard","itm_tattered_wrapping_boots","itm_flimsy_crossbow","itm_crude_bolts","itm_blunt_falchion"],
   str_14|agi_14|pw_attr,wpex(90,60,60,50,150,50),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_athletics_4|knows_riding_2|knows_sailing_3,default_face_1,default_face_2],

  # PN CAVALRY BEGIN
  ["lancer","Lancer","a lancer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_2", "itm_civil_noble_pants_grey", "itm_rhine_lance"],
   str_12|agi_13|pw_attr,wpex(100,0,160,0,50,20),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_5,default_face_1,default_face_2],

  ["hussar","Hussar","a hussar",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_2", "itm_civil_noble_pants_grey", "itm_training_light_sabre"],
   str_12|agi_15|pw_attr,wpex(160,0,50,0,70,20),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_riding_6,default_face_1,default_face_2],

  ["cuirassier","Cuirassier","a cuirassier",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_2", "itm_civil_noble_pants_grey", "itm_training_heavy_sword"],
   str_15|agi_10|pw_attr,wpex(160,70,20,0,70,20),knows_pw|knows_ironflesh_5|knows_power_strike_3|knows_athletics_2|knows_riding_5,default_face_1,default_face_2],

  ["dragoon","Dragoon","a dragoon",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_2", "itm_civil_noble_pants_grey", "itm_training_heavy_sword"],
   str_13|agi_13|pw_attr,wpex(120,0,120,0,120,20),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_riding_3,default_face_1,default_face_2],

  ["cavalry_musician","Cavalry Musician","a cavalry musician",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_2", "itm_civil_noble_pants_grey", "itm_training_light_sabre"],
   str_12|agi_12|pw_attr,wpex(120,0,20,0,50,20),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_1|knows_riding_5,default_face_1,default_face_2],

  ["cavalry_officer","Cavalry Officer","a cavalry officer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_gentleman_outfit_brown", "itm_leather_boots_b", "itm_french_old_pistol_1766", "itm_bullets", "itm_spyglass"],
   str_14|agi_14|pw_attr,wpex(160,70,100,0,90,20),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_6,default_face_1,default_face_2],
  # PN CAVALRY END

  # (!) NOT USED
  ["man_at_arms","Man at Arms","a man at arms",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_old_tabard","itm_old_hide_boots","itm_rusty_sword","itm_worn_sword","itm_old_shield"],
   str_15|agi_15|pw_attr,wpex(105,120,110,20,50,30),knows_pw|knows_ironflesh_4|knows_power_strike_4|knows_shield_1|knows_athletics_2|knows_riding_4,default_face_1,default_face_2],
  # (!) NOT USED
  ["sergeant","Sergeant","a sergeant",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_old_tabard","itm_old_hide_boots","itm_rusty_sword","itm_worn_sword","itm_old_shield"],
   str_15|agi_15|pw_attr,wpex(110,125,110,20,60,40),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_shield_2|knows_athletics_5|knows_riding_2,default_face_1,default_face_2],
  
  ["engineer","Engineer","an engineer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_3", "itm_civil_waistcoat_custom_4", "itm_leather_boots"],
   str_10|agi_12|pw_attr,wpex(90,50,60,30,65,50),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_engineer_5|knows_riding_2|knows_looting_1|knows_sailing_4,default_face_1,default_face_2],
  
  ["master_smith","Master Smith","a master smith",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_3", "itm_civil_waistcoat_custom_4", "itm_leather_boots"],
   str_12|agi_12|pw_attr,wpex(100,55,70,30,70,50),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_athletics_2|knows_engineer_7|knows_riding_2|knows_looting_2|knows_sailing_4,default_face_1,default_face_2],
  
  ["doctor","Doctor","a doctor",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_gentleman_cloth_a", "itm_leather_boots"],
   str_10|agi_10|pw_attr,wpex(70,40,50,10,20,30),knows_pw|knows_athletics_2|knows_power_strike_2|knows_wound_treatment_5|knows_riding_2,default_face_1,default_face_2],

  # PN NAVAL START
  ["sailor","Sailor","a sailor",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_fur_coat", "itm_leather_boots"],
   str_15|agi_13|pw_attr,wpex(90,0,50,0,50,100),knows_pw|knows_ironflesh_4|knows_power_strike_3|knows_athletics_5|knows_sailing_7|knows_engineer_1,default_face_1,default_face_2],

  ["captain","Captain","a captain",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_1", "itm_civil_noble_pants_grey", "itm_french_old_pistol_1766", "itm_bullets", "itm_spyglass"],
   str_14|agi_12|pw_attr,wpex(120,50,50,0,100,20),knows_pw|knows_ironflesh_4|knows_power_strike_2|knows_athletics_3|knows_sailing_9|knows_riding_1|knows_engineer_1,default_face_1,default_face_2],
  # PN NAVAL END

  ["traveler","Traveler","a traveler",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_fur_coat", "itm_leather_boots"],
   str_10|agi_13|pw_attr,wpex(60,40,50,10,20,60),knows_pw|knows_ironflesh_1|knows_power_strike_2|knows_athletics_5|knows_sailing_5|knows_riding_3|knows_labouring_1|knows_herding_1|knows_tailoring_2,default_face_1,default_face_2],

  ["herdsman","Herdsman","a herdsman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_leather_vest_plain", "itm_civil_coat1", "itm_civil_coat2", "itm_civil_fur_cloth_a", "itm_civil_peasant_shirt_1",
      "itm_leather_boots", "itm_hide_boots", "itm_hunter_boots", "itm_russian_peasant_knife"],
   str_10|agi_14|pw_attr,wpex(50,35,40,0,10,40),knows_pw|knows_power_strike_1|knows_athletics_5|knows_riding_5|knows_labouring_2|knows_herding_5|knows_tailoring_1,default_face_1,default_face_2],

  # PN Le Emperor
  ["lord","Majesty","the majesty",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_emperor_crown", "itm_civil_gentleman_outfit_blue", "itm_leather_boots_b", "itm_cane"],
   str_12|agi_15|pw_attr,wpex(160,0,70,0,50,20),knows_pw|knows_leadership_4|knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_riding_6,default_face_1,default_face_2],

  # PN BANDITS BEGIN
  ["pirate","Pirate","a pirate",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_fur_coat", "itm_leather_boots", "itm_civil_pirates_headscarf_a"],
   str_13|agi_13|pw_attr,wpex(100,0,50,0,100,70),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_looting_6|knows_sailing_8,default_face_1,default_face_2],
  
  ["rebel","Rebel","a rebel",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_peasant_hat", "itm_civil_militia_hat", "itm_civil_peasant_hat2", "itm_civil_peasant_hat3", "itm_civil_fur_hat",
      "itm_civil_militia_uniform", "itm_civil_coat1", "itm_civil_coat2", "itm_civil_militia_pants1", "itm_civil_militia_pants2", 
      "itm_russian_peasant_pitchfork", "itm_russian_peasant_club", "itm_russian_peasant_birch_club", "itm_russian_peasant_pike", "itm_russian_peasant_rogatina"],
   str_12|agi_12|pw_attr,wpex(70,0,70,45,100,20),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_2|knows_athletics_4|knows_riding_3|knows_looting_4,default_face_1,default_face_2],
  # PN BANDITS END

  ["mercenary","Mercenary","a mercenary",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_inf_uniform_a", "itm_civil_inf_pants_a", "itm_training_musket"],
   str_13|agi_14|pw_attr,wpex(50,0,100,0,120,50),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_riding_1|knows_engineer_1|knows_sailing_1|knows_tailoring_1,default_face_1,default_face_2],

  # PN ARTILLERY START
  ["artillerist","Artillerist","an artillerist",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_inf_uniform_a", "itm_civil_inf_pants_a", "itm_training_light_sabre"],
   str_15|agi_9|pw_attr,wpex(70,0,50,0,70,20),knows_pw|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_1|knows_engineer_1,default_face_1,default_face_2],

  ["artillerist_officer","Artillerist Officer","an artillerist officer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_shirt_1", "itm_civil_noble_pants_grey", "itm_french_old_pistol_1766", "itm_bullets", "itm_spyglass"],
   str_15|agi_9|pw_attr,wpex(120,30,50,0,90,20),knows_pw|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_2,default_face_1,default_face_2],
  # PN ARTILLERY END

  # PW Dummies
  ["track_select_dummy","{!}track_select_dummy","{!}track_select_dummy",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["destroyed_props_dummy","{!}destroyed_props_dummy","{!}destroyed_props_dummy",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],

  #Sapper and Enginner
  ["sapper","Sapper","a sapper",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_civil_inf_uniform_a", "itm_civil_inf_pants_a", "itm_cheap_sapper_axe", "itm_shovel"],
   str_15|agi_13|pw_attr,wpex(80,140,70,0,90,40),knows_pw|knows_ironflesh_4|knows_power_strike_2|knows_athletics_4|knows_riding_1|knows_engineer_2,default_face_1,default_face_2],
   
  ["godlike_hero","Godlike Hero","a godlike hero",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_french_artillery_bearskin_officer", "itm_admin_uniform", "itm_prussian_freikorps_pants", "itm_officer_gloves"],
   str_30|agi_30|pw_attr,wpex(300,300,300,300,300,300),knows_pw|knows_ironflesh_10|knows_power_strike_10|knows_power_draw_10|knows_power_throw_10|knows_shield_10|knows_athletics_10|knows_riding_10|knows_engineer_10|knows_wound_treatment_10|knows_looting_10|knows_labouring_10|knows_sailing_10|knows_tailoring_10|knows_herding_10,default_face_1,default_face_2],

  ["playable_troops_end","playable_troops_end","playable_troops_end",0,0,0,0,[],0,0,0,0,0],

  # NW Gambiarra
  ["custom_string_1", "Use", "{!}custom_string_1", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_2", "Use", "{!}custom_string_2", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_3", "Use", "{!}custom_string_3", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_4", "Use", "{!}custom_string_4", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_5", "Use", "{!}custom_string_5", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_6", "Use", "{!}custom_string_6", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_7", "Use", "{!}custom_string_7", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_8", "Use", "{!}custom_string_8", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_9", "Use", "{!}custom_string_9", tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_10","Use","{!}custom_string_10",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_11","Use","{!}custom_string_11",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_12","Use","{!}custom_string_12",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_13","Use","{!}custom_string_13",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_14","Use","{!}custom_string_14",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_15","Use","{!}custom_string_15",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_16","Use","{!}custom_string_16",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_17","Use","{!}custom_string_17",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_18","Use","{!}custom_string_18",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_19","Use","{!}custom_string_19",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_20","Use","{!}custom_string_20",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_21","Use","{!}custom_string_21",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_22","Use","{!}custom_string_22",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_23","Use","{!}custom_string_23",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_24","Use","{!}custom_string_24",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_25","Use","{!}custom_string_25",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_26","Use","{!}custom_string_26",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_27","Use","{!}custom_string_27",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_28","Use","{!}custom_string_28",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_29","Use","{!}custom_string_29",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_30","Use","{!}custom_string_30",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_31","Use","{!}custom_string_31",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_32","Use","{!}custom_string_32",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_33","Use","{!}custom_string_33",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_34","Use","{!}custom_string_34",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_35","Use","{!}custom_string_35",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_36","Use","{!}custom_string_36",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_37","Use","{!}custom_string_37",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_38","Use","{!}custom_string_38",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_39","Use","{!}custom_string_39",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_string_40","Use","{!}custom_string_40",tf_hero|tf_inactive,0,reserved,"fac_commoners",[],def_attrib,0,knows_pw,0],
  ["custom_strings_end","{!}custom_strings_end","{!}custom_strings_end", 0, 0, 0, "fac_commoners", [], 0, 0, 0, 0, 0],
  # End NW Gambiarra

  # PN Bots begin
  ["bot_merchant_1", "(BOT)Fakir", "{!}bot_merchant", tf_guarantee_all,0,0,"fac_commoners",
   ["itm_fur_coat", "itm_leather_boots", "itm_civil_peasant_hat2"], str_10|agi_10|pw_attr, wpex(20,20,20,20,20,20), 
   knows_pw|knows_ironflesh_1|knows_power_strike_2|knows_athletics_5, bot_custom_face_1, bot_custom_face_2],

  ["bot_merchant_2", "(BOT)Muhtar", "{!}bot_merchant", tf_guarantee_all,0,0,"fac_commoners",
   ["itm_leather_jacket", "itm_hide_boots", "itm_civil_top_hat"], str_10|agi_10|pw_attr, wpex(20,20,20,20,20,20), 
   knows_pw|knows_ironflesh_1|knows_power_strike_2|knows_athletics_5, bot_custom_face_1, bot_custom_face_2],
  # PN Bots end

  ["inactive_players_array","inactive_players_array","inactive_players_array",0,0,0,0,[],0,0,0,0,0],
  ["mission_data","mission_data","mission_data",0,0,0,0,[],0,0,0,0,0],
  ["banner_background_color_array","banner_background_color_array","banner_background_color_array",0,0,0,0,[],0,0,0,0,0],
  ["temp_array","temp_array","temp_array",0,0,0,0,[],0,0,0,0,0],
  ["last_chat_message","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_0","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_1","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_2","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_3","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_4","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_5","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_6","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_7","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_8","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_9","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_10","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_end","-","-",0,0,0,0,[],0,0,0,0,0],
  ["ship_array","ship_array","ship_array",0,0,0,0,[],0,0,0,0,0],
  ["cart_array","cart_array","cart_array",0,0,0,0,[],0,0,0,0,0],
  ["removed_scene_props","removed_scene_props","removed_scene_props",0,0,0,0,[],0,0,0,0,0],
  ["animation_menu_strings","animation_menu_strings","animation_menu_strings",0,0,0,0,[],0,0,0,0,0],
  ["animation_durations","animation_durations","animation_durations",0,0,0,0,[],0,0,0,0,0],
]
