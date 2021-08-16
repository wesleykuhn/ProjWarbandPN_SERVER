####################################################################################################################
# This is the separated code that server-side files uses. Its EXCLUSIVE for server-side use!
####################################################################################################################

###############################################
# OVERRIDE ####################################
###############################################
# FROM:
("pn_bank_deposit", sokf_invisible|spr_chest_flags(1), "pw_invisible_chest","bo_pw_invisible_chest", spr_item_chest_triggers(hit_points=2000, inventory_count=12, max_item_length=120)),
("pn_bank_withdraw", sokf_invisible|spr_chest_flags(1), "pw_invisible_chest","bo_pw_invisible_chest", spr_item_chest_triggers(hit_points=2000, inventory_count=12, max_item_length=120)),
# TO:
("pn_bank_deposit", sokf_invisible|spr_chest_flags(1), "pw_invisible_chest","bo_pw_invisible_chest", spr_bank_deposit_triggers()),
("pn_bank_withdraw", sokf_invisible|spr_chest_flags(1), "pw_invisible_chest","bo_pw_invisible_chest", spr_bank_withdraw_triggers()),

###############################################
# ADD #########################################
###############################################
def spr_bank_deposit_triggers():
  return [(ti_on_scene_prop_use,
   [(store_trigger_param_1, ":agent_id"),
		(agent_get_player_id, ":player_id", ":agent_id"),
		(player_is_active, ":player_id"),
		(gt, ":player_id", 0),
		(call_script, "script_bank_system_call", ":player_id", 2),
    ])] 

def spr_bank_withdraw_triggers():
  return [(ti_on_scene_prop_use,
   [(store_trigger_param_1, ":agent_id"),
		(agent_get_player_id, ":player_id", ":agent_id"),
		(player_is_active, ":player_id"),
		(gt, ":player_id", 0),
		(call_script, "script_bank_system_call", ":player_id", 1),
    ])]
