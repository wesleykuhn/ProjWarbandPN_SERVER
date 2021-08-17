####################################################################################################################
# This is the separated code that server-side files uses. Its EXCLUSIVE for server-side use!
####################################################################################################################

# SCRIPTS TO OVERRIDE
# game_receive_url_response
# player_check_name
# cf_save_player_exit
# cf_use_cart
# cf_hit_chest
# cf_hit_door
# cf_drop_money_bag_item
# cf_use_castle_money_chest
# cf_use_money_bag_item
###################################################################
# SCRIPTS TO ADD
# api_bank_system_call
# api_agent_get_position
# cf_log_damage
# cf_log_mount
# cf_log_dismount
# cf_log_loot
# cf_log_cart
# cf_log_pickup
# cf_log_drop
# cf_log_hit_chest
# cf_log_hit_door
# cf_log_drop_money_bag
# cf_log_money_from_chest
# cf_log_money_to_chest
# cf_log_use_money_bag

###############################################
# LINES TO ADD ################################
###############################################
# In the event:
(else_try),
        (eq, ":event_type", client_event_agent_loot_armor),
        (store_script_param, ":corpse_instance_id", 3),
        (try_begin),
          (prop_instance_is_valid, ":corpse_instance_id"),
          (neg | scene_prop_slot_eq, ":corpse_instance_id", slot_scene_prop_inventory_unique_id, 0),
          (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":corpse_instance_id"),
          (eq, ":scene_prop_id", "itm_agent_corpse"),
          (player_get_agent_id, ":agent_id", ":sender_player_id"),
          (agent_is_active, ":agent_id"),
          (agent_is_alive, ":agent_id"),
          (agent_get_position, pos1, ":agent_id"),
          (prop_instance_get_position, pos2, ":corpse_instance_id"),
          (get_sq_distance_between_positions, ":sq_distance", pos1, pos2),
          (le, ":sq_distance", sq(max_distance_to_loot)),
          (call_script, "script_cf_use_inventory", ":agent_id", ":corpse_instance_id", 0),
        (try_end),
# Add the before last line:
(else_try),
        (eq, ":event_type", client_event_agent_loot_armor),
        (store_script_param, ":corpse_instance_id", 3),
        (try_begin),
          (prop_instance_is_valid, ":corpse_instance_id"),
          (neg|scene_prop_slot_eq, ":corpse_instance_id", slot_scene_prop_inventory_unique_id, 0),
          (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":corpse_instance_id"),
          (eq, ":scene_prop_id", "itm_agent_corpse"),
          (player_get_agent_id, ":agent_id", ":sender_player_id"),
          (agent_is_active, ":agent_id"),
          (agent_is_alive, ":agent_id"),
          (agent_get_position, pos1, ":agent_id"),
          (prop_instance_get_position, pos2, ":corpse_instance_id"),
          (get_sq_distance_between_positions, ":sq_distance", pos1, pos2),
          (le, ":sq_distance", sq(max_distance_to_loot)),
          (call_script, "script_cf_use_inventory", ":agent_id", ":corpse_instance_id", 0),
(call_script, "script_cf_log_loot", ":agent_id"),
        (try_end),



###############################################
# OVERRIDE ####################################
###############################################
("game_receive_url_response", # called by the game when a response is received from a web server, if used
   [#(store_script_param, ":integer_count", 1),
    #(store_script_param, ":string_count", 2),

    (assign, ":return_code", reg0),
    (try_begin),
      # Load Player and his Gear
      (eq, ":return_code", 0),
      (assign, ":player_id", reg1),
      #(assign, ":bank_gold", reg2),
      (call_script, "script_player_adjust_gold", ":player_id", reg3, 0),
      
      (try_begin),
        (gt, reg4, 0),
        (player_add_spawn_item, ":player_id", ek_head, reg4),
        (player_set_slot, ":player_id", slot_player_equip_head, reg4),
      (try_end),
      (try_begin),
        (gt, reg5, 0),
        (player_add_spawn_item, ":player_id", ek_body, reg5),
        (player_set_slot, ":player_id", slot_player_equip_body, reg5),
      (try_end),
      (try_begin),
        (gt, reg6, 0),
        (player_add_spawn_item, ":player_id", ek_foot, reg6),
        (player_set_slot, ":player_id", slot_player_equip_foot, reg6),
      (try_end),
      (try_begin),
        (gt, reg7, 0),
        (player_add_spawn_item, ":player_id", ek_gloves, reg7),
        (player_set_slot, ":player_id", slot_player_equip_gloves, reg7),
      (try_end),
      (try_begin),
        (gt, reg8, 0),
        (player_add_spawn_item, ":player_id", ek_item_0, reg8),
        (player_set_slot, ":player_id", slot_player_equip_item_0, reg8),
      (try_end),
      (try_begin),
        (gt, reg9, 0),
        (player_add_spawn_item, ":player_id", ek_item_1, reg9),
        (player_set_slot, ":player_id", slot_player_equip_item_1, reg9),
      (try_end),
      (try_begin),
        (gt, reg10, 0),
        (player_add_spawn_item, ":player_id", ek_item_2, reg10),
        (player_set_slot, ":player_id", slot_player_equip_item_2, reg10),
      (try_end),
      (try_begin),
        (gt, reg11, 0),
        (player_add_spawn_item, ":player_id", ek_item_3, reg11),
        (player_set_slot, ":player_id", slot_player_equip_item_3, reg11),
      (try_end),
      (try_begin),
        (gt, reg12, 0),
        (player_add_spawn_item, ":player_id", ek_horse, reg12),
        (player_set_slot, ":player_id", slot_player_equip_horse, reg12),
      (try_end),
      
      (player_set_troop_id, ":player_id", reg13),
      
      (try_begin),
        (call_script, "script_change_faction", ":player_id", reg14, change_faction_type_respawn),
      (try_end),

      # (try_begin),
      #   (player_is_admin, ":player_id"),
      #   (call_script, "script_set_admin_permissions", ":player_id", reg17),
      # (try_end),

      (str_store_string, s10, "@Welcome to our Server! Your token is: {s0}"),
      (str_store_string, s11, "@You currently have {reg2} gold in your bank account!"),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s10),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s11),
    (else_try),
      # Load Agent his Position, HP and Food
      (eq, ":return_code", 1),
      (agent_get_player_id, ":player_id", reg1),
      (gt, ":player_id", 0),
      (player_is_active, ":player_id"),
      (try_begin),
        (gt, reg2, 0),
        (gt, reg3, 0),
        (gt, reg4, 0),
        (init_position, pos20),
        (position_set_x, pos20, reg2),
        (position_set_y, pos20, reg3),
        (position_set_z, pos20, reg4),
        (agent_get_horse, ":horse_agent", reg1),
        (try_begin),
          (eq, ":horse_agent", -1),
          (agent_set_position, reg1, pos20),
        (else_try),
          (agent_set_position, reg1, pos20),
          (agent_set_position, ":horse_agent", pos20),
          (agent_set_hit_points, ":horse_agent", reg5, 0),
        (try_end),
      (try_end),
      (try_for_range, ":equip_slot", ek_head, ek_gloves + 1),
        (agent_get_item_slot, ":item_id", reg1, ":equip_slot"),
        (ge, ":item_id", all_items_begin),
        (call_script, "script_agent_calculate_stat_modifiers_for_item", reg1, ":item_id", 1, 1),
      (try_end),
      (player_get_agent_id, ":agent_id", ":player_id"),
      (agent_set_hit_points, ":agent_id", reg6, 0),
      (agent_set_slot, ":agent_id", slot_agent_food_amount, reg7),
      (multiplayer_send_3_int_to_player, ":player_id", server_event_agent_set_slot, ":agent_id", slot_agent_food_amount, reg7),
      (str_store_string, s11, "@Everything loaded!"),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s11),
    (else_try),
      #Save is ok
      (eq, ":return_code", 2),
    (else_try),
      #Withdraw fail
      (eq, ":return_code", 4),
      (assign, ":player_id", reg1),
      (str_store_string, s11, "@You have no gold on the bank!"),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s11),
    (else_try),
      #Deposit fail
      (eq, ":return_code", 6),
      (assign, ":player_id", reg1),
      (str_store_string, s11, "@You don't have any gold which you can put in the bank!"),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s11),
    (else_try),
      #Withdraw okay
      (eq, ":return_code", 3),
      (assign, ":player_id", reg1),
      (call_script, "script_player_adjust_gold", ":player_id", reg2, 1),
      (str_store_string, s11, "@Now your balance is {reg3} gold on bank."),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s11),
    (else_try),
      #Deposit okay
      (eq, ":return_code", 5),
      (assign, ":player_id", reg1),
      (call_script, "script_player_adjust_gold", ":player_id", 0, 0),
      (str_store_string, s11, "@Now your balance is {reg2} gold on bank."),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s11),
    (else_try),
      #Player is banned
      (eq, ":return_code", 7),
      (assign, ":player_id", reg1),
      (str_store_string, s11, "@You are banned. {s3} banned you!"),
      (str_store_string, s12, "@Ban Reason: {s0}"),
      (str_store_string, s13, "@Unban at: {s1} {s2}!"),
      (multiplayer_send_string_to_player, ":player_id", server_event_admin_chat_announce, s11),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s12),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s13),
      (kick_player, ":player_id"),
    (else_try),
      #Player got banned
      (eq, ":return_code", 8),
      (assign, ":player_id", reg1),
      (str_store_string, s11, "@You got banned. {s3} banned you!"),
      (str_store_string, s12, "@Ban Reason: {s0}"),
      (str_store_string, s13, "@Unban at: {s1} {s2}!"),
      (multiplayer_send_string_to_player, ":player_id", server_event_admin_chat_announce, s11),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s12),
      (multiplayer_send_string_to_player, ":player_id", server_event_local_chat, s13),
      (kick_player, ":player_id"),
    (else_try),
      #Player is banned
      (eq, ":return_code", 9),
      (assign, ":player_id", reg1),
      (str_store_string, s11, "@You are IP banned!"),
      (multiplayer_send_string_to_player, ":player_id", server_event_admin_chat_announce, s11),
      (kick_player, ":player_id"),
    (try_end),
  ]),

  ("cf_hit_door", # server: handle hitting a rotating destructible door; should be called from ti_on_scene_prop_hit
   [(multiplayer_is_server),
    (store_script_param, ":instance_id", 1), # must be valid
    (store_script_param, ":hit_damage", 2),
    (store_script_param, ":resource_class", 3),
    (store_script_param, ":id_agent", 4), # -1 called from game trigger, else called manually by PN
    (set_fixed_point_multiplier, 1),
    (try_begin),
      (eq, ":id_agent", -1),
      (position_get_x, ":agent_id", pos2), # expects agent id in pos2.x from ti_on_scene_prop_hit
      (assign, ":called_by", 0), # from game triiger
    (else_try),
      (assign, ":agent_id", ":id_agent"),
      (assign, ":called_by", 1), # from PN manuaaly by a script
    (try_end),
    (set_fixed_point_multiplier, 100),
    (call_script, "script_cf_log_hit_door", ":agent_id", ":hit_damage"),
    (try_begin), # only allow repairing standing doors if they are open
      (scene_prop_slot_eq, ":instance_id", slot_scene_prop_rotation, 1),
      (assign, ":repair_active", 1),
    (else_try),
      (assign, ":repair_active", 0),
    (try_end),
    (scene_prop_get_slot, ":full_hit_points", ":instance_id", slot_scene_prop_full_hit_points),
    (call_script, "script_cf_hit_repairable_scene_prop", ":instance_id", ":hit_damage", ":full_hit_points", ":resource_class", ":agent_id", ":repair_active", ":called_by"),
    (assign, ":result", reg0),
    (try_begin),
      (eq, ":result", repairable_hit),
      (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (call_script, "script_hit_scene_prop_play_sound", ":agent_id", ":instance_id", "snd_shield_hit_wood_metal"),
    (else_try),
      (eq, ":result", repairable_destroyed),
      (call_script, "script_destroy_door", ":agent_id", ":instance_id"),
      (particle_system_burst, "psys_dummy_smoke", pos1, 20),
      (particle_system_burst, "psys_dummy_straw", pos1, 50),
      (call_script, "script_hit_scene_prop_play_sound", ":agent_id", ":instance_id", "snd_cut_wood_break"),
    (else_try),
      (eq, ":result", repairable_hit_destroyed),
      (call_script, "script_hit_scene_prop_play_sound", ":agent_id", ":instance_id", "snd_cut_wood_scratch"),
    (else_try),
      (eq, ":result", repairable_repairing),
      (agent_play_sound, ":agent_id", "snd_repair_wood"),
    (else_try),
      (eq, ":result", repairable_repaired),
      (prop_instance_get_starting_position, pos2, ":instance_id"),
      (prop_instance_animate_to_position, ":instance_id", pos2, 400),
      (agent_play_sound, ":agent_id", "snd_man_grunt"),
    (try_end),]),

  ("cf_drop_money_bag_item", # server: handle players dropping money bags
   [(store_script_param, ":player_id", 1), # must be valid
    (store_script_param, ":gold_amount", 2),
    (player_get_agent_id, ":agent_id", ":player_id"),
    (agent_is_alive, ":agent_id"),
    (call_script, "script_cf_check_enough_gold", ":player_id", ":gold_amount"),
    (store_mission_timer_a, ":time"),
    (player_get_slot, ":last_action_time", ":player_id", slot_player_last_action_time),
    (store_sub, ":interval", ":time", ":last_action_time"),
    (this_or_next|ge, ":interval", repeat_action_min_interval),
    (player_is_admin, ":player_id"),
    (player_set_slot, ":player_id", slot_player_last_action_time, ":time"),
    (call_script, "script_player_adjust_gold", ":player_id", ":gold_amount", -1),
    (agent_get_position, pos1, ":agent_id"),
    (position_move_y, pos1, 50),
    (set_spawn_position, pos1),
    (spawn_item, "itm_money_bag", 0, "$g_spawn_item_prune_time"),
    (scene_prop_set_slot, reg0, slot_scene_prop_gold_value, ":gold_amount"),
	(call_script, "script_cf_log_drop_money_bag", ":player_id", ":gold_amount"),
    ]),

  ("cf_hit_chest", # server: handle damaging and repairing a storage chest; should be called from ti_on_scene_prop_hit
   [(multiplayer_is_server),
    (store_script_param, ":instance_id", 1), # must be valid
    (store_script_param, ":hit_damage", 2),
    (store_script_param, ":full_hit_points", 3),
    (set_fixed_point_multiplier, 1),
    (position_get_x, ":agent_id", pos2), # expects agent id in pos2.x from ti_on_scene_prop_hit
    (set_fixed_point_multiplier, 100),
	(call_script, "script_cf_log_hit_chest", ":agent_id", ":hit_damage"),
    (call_script, "script_cf_hit_repairable_scene_prop", ":instance_id", ":hit_damage", ":full_hit_points", item_class_wood, ":agent_id", 1, 0),
    (assign, ":result", reg0),
    (try_begin),
      (eq, ":result", repairable_hit),
      (call_script, "script_hit_scene_prop_play_sound", ":agent_id", ":instance_id", "snd_shield_hit_wood_metal"),
    (else_try),
      (eq, ":result", repairable_destroyed),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_unlocked, 1),
      (particle_system_burst, "psys_dummy_smoke", pos1, 10),
      (particle_system_burst, "psys_dummy_straw", pos1, 30),
      (call_script, "script_hit_scene_prop_play_sound", ":agent_id", ":instance_id", "snd_shield_broken"),
    (else_try),
      (eq, ":result", repairable_hit_destroyed),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_unlocked, 1),
      (call_script, "script_hit_scene_prop_play_sound", ":agent_id", ":instance_id", "snd_cut_wood_scratch"),
    (else_try),
      (eq, ":result", repairable_repairing),
      (agent_play_sound, ":agent_id", "snd_repair_wood"),
    (else_try),
      (eq, ":result", repairable_repaired),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_unlocked, 0),
      (agent_play_sound, ":agent_id", "snd_repair_wood"),
    (try_end),
    ]),

  ("cf_use_cart", # server: handle players trying to attach or access carts
   [(store_script_param, ":agent_id", 1), # must be valid
    (store_script_param, ":instance_id", 2), # must be valid
    (store_script_param, ":action", 3), # from cart_choose_action: -1 = attach, 1 = access
    (agent_get_player_id, ":player_id", ":agent_id"),
    (player_is_active, ":player_id"),
    (agent_is_alive, ":agent_id"),
    (assign, ":fail", 0),
    (try_begin),
      (eq, ":action", 1),
      (call_script, "script_cf_use_inventory", ":agent_id", ":instance_id", 0),
	  (call_script, "script_cf_log_cart", ":player_id"),
    (else_try),
      (eq, ":action", -1),
      (scene_prop_get_slot, ":required_horse", ":instance_id", slot_scene_prop_required_horse),
      (agent_get_horse, ":horse_agent_id", ":agent_id"),
      (try_begin), # if a horse is required, check
        (ge, ":required_horse", 1),
        (assign, ":attach_agent_id", ":horse_agent_id"),
        (try_begin),
          (gt, ":horse_agent_id", -1),
          (agent_get_item_id, ":horse_item_id", ":horse_agent_id"),
          (this_or_next|eq, ":required_horse", 1),
          (eq, ":horse_item_id", ":required_horse"),
        (else_try),
          (assign, ":fail", 1),
          (multiplayer_send_2_int_to_player, ":player_id", server_event_preset_message, "str_not_riding_necessary_horse", preset_message_error),
        (try_end),
      (else_try), # if mounted but horse not required, disallow attaching hand carts
        (gt, ":horse_agent_id", -1),
        (assign, ":fail", 1),
      (else_try), # hand carts
        (assign, ":attach_agent_id", ":agent_id"),
        (agent_get_troop_id, ":troop_id", ":agent_id"),
        (store_skill_level, ":labouring", "skl_labouring", ":troop_id"),
        (try_begin),
          (lt, ":labouring", 1),
          (assign, ":fail", 1),
          (multiplayer_send_2_int_to_player, ":player_id", server_event_preset_message, "str_craft_not_skilled", preset_message_error),
        (try_end),
      (try_end),
      (eq, ":fail", 0),
      (try_begin),
        (call_script, "script_cf_attach_cart", ":attach_agent_id", ":instance_id", ":agent_id"),
      (else_try),
        (assign, ":fail", 1),
        (multiplayer_send_2_int_to_player, ":player_id", server_event_preset_message, "str_already_attached_cart", preset_message_error),
      (try_end),
    (else_try),
      (assign, ":fail", 1),
    (try_end),
    (eq, ":fail", 0),
    ]),

    ("player_check_name", # server: check the player name and unique id with the name server, if enabled
        [
            (store_script_param, ":player_id", 1), # must be valid
            (str_store_string, s20, "str_api_host_controller"),
            (str_store_string, s21, "str_api_password"),
            (str_encode_url, s21),
            (assign, reg20, ":player_id"),
            (str_store_player_username, s22, ":player_id"),
            (str_encode_url, s22),
            (player_get_unique_id, reg21, ":player_id"),
            (str_store_player_ip, s23, ":player_id"),
            (str_encode_url, s23),
            (send_message_to_url, "@{s20}?scpass={s21}&function=1&playerid={reg20}&username={s22}&guid={reg21}&userip={s23}"),
            (server_add_message_to_log, "@{s20}?scpass={s21}&function=1&playerid={reg20}&username={s22}&guid={reg21}&userip={s23}"),
        ]
    ),

    ("cf_save_player_exit", # server: when a player disconnects, save attributes to the inactive players list
   [(store_script_param, ":player_id", 1), # must be valid
    (player_get_agent_id, ":agent_id", ":player_id"),
	(gt, ":agent_id", 0),
	(agent_is_active, ":agent_id"),
	(agent_is_alive, ":agent_id"),
	(agent_get_item_slot, ":item0", ":agent_id", 0),
	(agent_get_item_slot, ":item1", ":agent_id", 1),
	(agent_get_item_slot, ":item2", ":agent_id", 2),
	(agent_get_item_slot, ":item3", ":agent_id", 3),
	(try_begin),
		(is_between, ":item0", "itm_pw_banner_pole_a01", "itm_pw_banner_castle_fac_1a"),
		(assign, ":item0", 0),
	(try_end),
	(try_begin),
		(is_between, ":item1", "itm_pw_banner_pole_a01", "itm_pw_banner_castle_fac_1a"),
		(assign, ":item1", 0),
	(try_end),
	(try_begin),
		(is_between, ":item2", "itm_pw_banner_pole_a01", "itm_pw_banner_castle_fac_1a"),
		(assign, ":item2", 0),
	(try_end),
	(try_begin),
		(is_between, ":item3", "itm_pw_banner_pole_a01", "itm_pw_banner_castle_fac_1a"),
		(assign, ":item3", 0),
	(try_end),
	(agent_get_item_slot, ":head", ":agent_id", ek_head),
	(agent_get_item_slot, ":body", ":agent_id", ek_body),
	(agent_get_item_slot, ":foot", ":agent_id", ek_foot),
	(agent_get_item_slot, ":gloves", ":agent_id", ek_gloves),
	(store_agent_hit_points, ":player_hit_points", ":agent_id", 0),
	(player_get_troop_id, ":this_troop_id", ":player_id"),
	(player_get_slot, ":faction", ":player_id", slot_player_faction_id),
	(assign, reg2, ":head"),
	(assign, reg3, ":body"),
	(assign, reg4, ":foot"),
	(assign, reg5, ":gloves"),
	(assign, reg6, ":item0"),
	(assign, reg7, ":item1"),
	(assign, reg8, ":item2"),
	(assign, reg9, ":item3"),
	(assign, reg10, ":player_hit_points"),
	(assign, reg20, ":this_troop_id"),
	(assign, reg11, ":faction"),
	(player_get_gold, ":original_player_gold", ":player_id"),
	(assign, reg12, ":original_player_gold"),
	(agent_get_position, pos1, ":agent_id"),
	(position_get_x, ":pos_x", pos1),
	(position_get_y, ":pos_y", pos1),
	(position_get_z, ":pos_z", pos1),
	(assign, reg13, ":pos_x"),
	(assign, reg14, ":pos_y"),
	(assign, reg15, ":pos_z"),
	(agent_get_slot, ":food_amount", ":agent_id", slot_agent_food_amount),
	(assign, reg16, ":food_amount"),
	(try_begin),
	(gt, ":item0", -1),
	(call_script, "script_cf_agent_consume_item", ":agent_id", ":item0", 1),
	(try_end),
	(try_begin),
	(gt, ":item1", -1),
	(call_script, "script_cf_agent_consume_item", ":agent_id", ":item1", 1),
	(try_end),
	(try_begin),
	(gt, ":item2", -1),
	(call_script, "script_cf_agent_consume_item", ":agent_id", ":item2", 1),
	(try_end),
	(try_begin),
	(gt, ":item3", -1),
	(call_script, "script_cf_agent_consume_item", ":agent_id", ":item3", 1),
	(try_end),
	(agent_fade_out, ":agent_id"),
	# horse reg 17...
	(try_begin), #checken ob pferd ueberhaupt existiert
		(agent_get_horse, ":horse", ":agent_id"),
		(agent_is_active, ":horse"),
		(agent_is_alive, ":horse"),
		(agent_get_item_id, ":horse_itemid", ":horse"),
		(assign, reg17, ":horse_itemid"),
		(store_agent_hit_points, ":horse_hit_points", ":horse", 0),
		(assign, reg21, ":horse_hit_points"),
		(agent_fade_out, ":horse"),
		(else_try),
		(assign, reg17, "@0"),
	(try_end),
    (str_store_string, s20, "str_api_host_controller"),
    (str_store_string, s21, "str_api_password"),
    (str_encode_url, s21),
    (assign, reg30, ":player_id"),
    (player_get_unique_id, reg31, ":player_id"),
    (assign, reg32, ":agent_id"),
    (send_message_to_url, "@{s20}?scpass={s21}&function=3&playerid={reg30}&agentid={reg32}&guid={reg31}&d1={reg12}&d2={reg2}&d3={reg3}&d4={reg4}&d5={reg5}&d6={reg6}&d7={reg7}&d8={reg8}&d9={reg9}&d10={reg17}&d11={reg20}&d12={reg11}&d13={reg10}&d14={reg16}&d15={reg13}&d16={reg14}&d17={reg15}&d18={reg21}"),
    (server_add_message_to_log, "@{s20}?scpass={s21}&function=3&playerid={reg30}&agentid={reg32}&guid={reg31}&d1={reg12}&d2={reg2}&d3={reg3}&d4={reg4}&d5={reg5}&d6={reg6}&d7={reg7}&d8={reg8}&d9={reg9}&d10={reg17}&d11={reg20}&d12={reg11}&d13={reg10}&d14={reg16}&d15={reg13}&d16={reg14}&d17={reg15}&d18={reg21}"),
   ]),

  ("cf_use_castle_money_chest", # server and clients: handle depositing to and withdrawing from a money chest. the client version just does the checks, the server version also applies changes
   [(store_script_param, ":player_id", 1), # must be valid
    (store_script_param, ":instance_id", 2),
    (store_script_param, ":gold_value", 3), # positive values to deposit, negative to withdraw
    (assign, ":fail_message", -1),
    (try_begin),
      (neq, "$g_game_type", "mt_no_money"),
      (neq, ":gold_value", 0),
      (assign, ":fail_message", "str_no_money_chest_nearby"),
      (call_script, "script_cf_can_use_scene_prop", ":player_id", ":instance_id", "spr_pw_castle_money_chest"),
      (scene_prop_get_slot, ":chest_gold", ":instance_id", slot_scene_prop_stock_count),
      (try_begin),
        (lt, ":gold_value", 0),
        (call_script, "script_scene_prop_get_owning_faction", ":instance_id"),
        (try_begin),
          (eq, reg1, -1),
        (else_try),
          (neg|multiplayer_is_server),
        (else_try),
          (scene_prop_slot_eq, ":instance_id", slot_scene_prop_unlocked, 1),
        (else_try),
          (player_slot_eq, ":player_id", slot_player_faction_id, reg0),
          (player_slot_eq, ":player_id", slot_player_has_faction_money_key, 1),
        (else_try),
          (player_slot_eq, ":player_id", slot_player_faction_id, reg0),
          (call_script, "script_cf_player_is_lord", ":player_id"),
        (else_try),
          (assign, ":fail_message", "str_cant_open_money_chest"),
        (try_end),
        (neq, ":fail_message", "str_cant_open_money_chest"),
        (assign, ":fail_message", "str_not_enough_money_in_chest"),
        (store_mul, ":gold_requested", ":gold_value", -1),
        (ge, ":chest_gold", ":gold_requested"),
        (try_begin),
          (multiplayer_is_server),
          (val_sub, ":chest_gold", ":gold_requested"),
          (call_script, "script_player_adjust_gold", ":player_id", ":gold_requested", 1),
		  (call_script, "script_cf_log_money_from_chest", ":player_id", ":gold_requested", 1),
        (try_end),
        (assign, ":fail_message", 0),
      (else_try),
        (gt, ":gold_value", 0),
        (assign, ":fail_message", "str_dont_have_enough_money"),
        (call_script, "script_cf_check_enough_gold", ":player_id", ":gold_value"),
        (try_begin),
          (multiplayer_is_server),
		  (call_script, "script_cf_log_money_to_chest", ":player_id", ":gold_value", 1),
          (call_script, "script_player_adjust_gold", ":player_id", ":gold_value", -1),
          (val_add, ":chest_gold", ":gold_value"),
          (val_clamp, ":chest_gold", 0, max_possible_gold),
        (try_end),
        (assign, ":fail_message", 0),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":fail_message", 0),
      (try_begin),
        (multiplayer_is_server),
        (scene_prop_set_slot, ":instance_id", slot_scene_prop_stock_count, ":chest_gold"),
        (multiplayer_send_3_int_to_player, ":player_id", server_event_scene_prop_set_slot, ":instance_id", slot_scene_prop_stock_count, ":chest_gold"),
      (else_try),
        (multiplayer_send_3_int_to_server, client_event_transfer_gold, ":instance_id", ":gold_value"),
      (try_end),
    (else_try),
      (multiplayer_is_server),
      (gt, ":fail_message", 0),
      (neq, ":fail_message", "str_dont_have_enough_money"),
      (multiplayer_send_2_int_to_player, ":player_id", server_event_preset_message, ":fail_message", preset_message_error),
    (try_end),
    (assign, reg0, ":fail_message"),
    (eq, ":fail_message", 0),
    ]),

    ("cf_use_money_bag_item", # server: handle players retrieving the contents of equipped money bags
   [(store_script_param, ":agent_id", 1), # must be valid
    (neq, "$g_game_type", "mt_no_money"),
    (call_script, "script_cf_agent_consume_item", ":agent_id", "itm_money_bag", 1),
    (call_script, "script_cf_pop_agent_money_bag_value", ":agent_id"),
    (assign, ":gold_value", reg0),
    (agent_get_player_id, ":player_id", ":agent_id"),
    (player_is_active, ":player_id"),
    (call_script, "script_player_adjust_gold", ":player_id", ":gold_value", 1),
	(call_script, "script_cf_log_use_money_bag", ":player_id", ":gold_value"),
    ]),



###############################################
# ADD #########################################
###############################################
    ("api_bank_system_call",
        [
            (store_script_param, ":player_id", 1),
            (store_script_param, ":to_do", 2),
            (try_begin),
                (eq, ":to_do", 1), #Withdraw
                (str_store_string, s20, "str_api_host_controller"),
                (str_store_string, s21, "str_api_password"),
                (str_encode_url, s21),
                (assign, reg20, ":player_id"),
                (player_get_unique_id, reg21, ":player_id"),
                (send_message_to_url, "@{s20}?scpass={s21}&function=5&playerid={reg20}&guid={reg21}"),
                (server_add_message_to_log, "@{s20}?scpass={s21}&function=5&playerid={reg20}&guid={reg21}"),
            (else_try),
                (eq, ":to_do", 2), #Deposit
                (player_get_gold, reg24, ":player_id"),
                (str_store_string, s20, "str_api_host_controller"),
                (str_store_string, s21, "str_api_password"),
                (str_encode_url, s21),
                (assign, reg20, ":player_id"),
                (player_get_unique_id, reg21, ":player_id"),
                (send_message_to_url, "@{s20}?scpass={s21}&function=6&playerid={reg20}&guid={reg21}&putonbank={reg24}"),
                (server_add_message_to_log, "@{s20}?scpass={s21}&function=6&playerid={reg20}&guid={reg21}&putonbank={reg24}"),
            (try_end)
        ]
    ),

    ("api_agent_get_position", #will load armor etc
        [
            (store_script_param, ":player_id", 1),
            (store_script_param, ":agent_id", 2),

            (str_store_string, s20, "str_api_host_controller"),
            (str_store_string, s21, "str_api_password"),
            (str_encode_url, s21),
            (assign, reg20, ":player_id"),
            (player_get_unique_id, reg21, ":player_id"),
            (assign, reg22, ":agent_id"),
            (send_message_to_url, "@{s20}?scpass={s21}&function=2&playerid={reg20}&agentid={reg22}&guid={reg21}"),
            (server_add_message_to_log, "@{s20}?scpass={s21}&function=2&playerid={reg20}&agentid={reg22}&guid={reg21}"),
        ]
    ),

    ("cf_log_damage",
        [
            (multiplayer_is_server),
            (store_script_param, ":attacked_agent_id", 1),
            (store_script_param, ":attacker_agent_id", 2),
            (store_script_param, ":damage_dealt", 3),
            (try_begin),
                (neg|eq,":attacked_agent_id",":attacker_agent_id"),#dont log if he hurts himself
                (assign,":log_the_data",1),
                (try_begin),
                    (neg|agent_is_human,":attacked_agent_id"),
                    (str_store_string,s1,"@Horse"),
                    (try_begin),
                        (agent_get_rider,":rider_agent_id", ":attacked_agent_id"),
                        (agent_is_active,":rider_agent_id"),
                        (try_begin),
                            (eq,":rider_agent_id",":attacker_agent_id"), ##Check to see if he is damaging his own horse
                            (assign,":log_the_data",0),
                        (try_end),
                        (agent_get_player_id,":rider_player_id",":rider_agent_id"),
                        (str_store_player_username,s10, ":rider_player_id"),
                        (str_store_string,s1,"@Horse ({s10})"),
                    (try_end),
                    (else_try),
                        (agent_get_player_id,":attacked_player_id",":attacked_agent_id"),
                        (str_store_player_username,s1, ":attacked_player_id"),
                    (try_end),
                    (try_begin),
                        (eq,":log_the_data",1),
                        (neg|agent_is_human,":attacker_agent_id"),
                        (str_store_string,s0,"@Horse"),
                        (try_begin),
                            (agent_get_rider,":rider_agent_id", ":attacker_agent_id"),
                            (agent_is_active,":rider_agent_id"),
                            (agent_get_player_id,":rider_player_id",":rider_agent_id"),
                            (str_store_player_username,s15, ":rider_player_id"),
                            (str_store_string,s0,"@Horse ({s15})"),
                        (try_end),
                    (else_try),
                        (eq,":log_the_data",1),
                        (agent_get_player_id,":attacker_player_id",":attacker_agent_id"),
                        (str_store_player_username,s0, ":attacker_player_id"),
                    (try_end),
                (try_begin),
                    (eq,":log_the_data",1),
                    (assign,reg0,":damage_dealt"),
                    (server_add_message_to_log, "@{s0} attacked {s1} dealing {reg0} damage"),
                (try_end),
            (try_end)
        ]
    ),

    ("cf_log_mount",
        [
            (multiplayer_is_server),
            (store_script_param, ":agent_id", 1),
            (store_script_param, ":horse_agent_id", 2),
            (try_begin),
                (agent_get_player_id,":player_id",":agent_id"),
                (gt, ":player_id", 0),
                (player_is_active, ":player_id"),
                (str_store_player_username, s1, ":player_id"),
                (agent_get_item_id, ":horse_item_id", ":horse_agent_id"),
                (str_store_item_name,s2 ,":horse_item_id"),
                (server_add_message_to_log, "@{s1} did mount a {s2}"),
            (try_end),
        ]
    ),
        
    ("cf_log_dismount",
        [
            (multiplayer_is_server),
            (store_script_param, ":agent_id", 1),
            (store_script_param, ":horse_agent_id", 2),
            (try_begin),
                (agent_get_player_id,":player_id",":agent_id"),
                (gt, ":player_id", 0),
                (player_is_active, ":player_id"),
                (str_store_player_username, s1, ":player_id"),
                (agent_get_item_id, ":horse_item_id", ":horse_agent_id"),
                (str_store_item_name, s2 ,":horse_item_id"),
                (server_add_message_to_log, "@{s1} did dismount a {s2}"),
            (try_end),
        ]
    ),
        
    ("cf_log_loot",
        [
            (multiplayer_is_server),
            (store_script_param, ":agent_id", 1),
            (agent_get_player_id, ":player_id", ":agent_id"),
            (try_begin),
                (gt, ":player_id", 0),
                (player_is_active, ":player_id"),
                (str_store_player_username,s1, ":player_id"),
                (server_add_message_to_log, "@{s1} looted a corpse."),
            (try_end),
        ]
    ),
        
    ("cf_log_cart",
        [
            (multiplayer_is_server),
            (store_script_param, ":player_id", 1),
            (try_begin),
                (str_store_player_username,s1, ":player_id"),
                (server_add_message_to_log, "@{s1} looked into a cart."),
            (try_end),
        ]
    ),
        
    ("cf_log_pickup",
        [
            (multiplayer_is_server),
            (store_script_param, ":agent_id", 1),
            (store_script_param, ":item_id", 2),
            (agent_get_player_id,":player_id",":agent_id"),
            (str_store_player_username,s1, ":player_id"),
            (str_store_item_name, s2, ":item_id"),         
            (try_begin),
                (server_add_message_to_log, "@{s1} picked up {s2} from the ground."),
            (try_end),
        ]
    ),
        
    ("cf_log_drop",
        [
            (multiplayer_is_server),
            (store_script_param, ":agent_id", 1),
            (store_script_param, ":item_id", 2),
            (agent_get_player_id,":player_id",":agent_id"),
            (str_store_player_username,s1, ":player_id"),
            (str_store_item_name, s2, ":item_id"),         
            (try_begin),
                (server_add_message_to_log, "@{s1} droppped {s2} on the ground."),
            (try_end),
        ]
    ),
        
    ("cf_log_hit_chest",
        [
            (multiplayer_is_server),
            (store_script_param, ":agent_id", 1),
            (store_script_param, ":hit_damage", 2),
            (agent_get_player_id,":player_id",":agent_id"),
            (gt, ":player_id", 0),
            (player_is_active, ":player_id"),
            (str_store_player_username,s1, ":player_id"),  
            (assign, reg1, ":hit_damage"),
            (try_begin),
                (server_add_message_to_log, "@{s1} hit chest for {reg1} damage."),
            (try_end),
        ]
    ),
        
    ("cf_log_hit_door",
        [
            (multiplayer_is_server),
            (store_script_param, ":agent_id", 1),
            (store_script_param, ":hit_damage", 2),
            (agent_get_player_id,":player_id",":agent_id"),
            (gt, ":player_id", 0),
            (player_is_active, ":player_id"),
            (str_store_player_username,s1, ":player_id"),  
            (assign, reg1, ":hit_damage"),
            (try_begin),
                (server_add_message_to_log, "@{s1} hit door for {reg1} damage."),
            (try_end),
        ]
    ),
        
    ("cf_log_drop_money_bag",
        [
            (multiplayer_is_server),
            (store_script_param, ":player_id", 1),
            (store_script_param, ":gold_amount", 2),
            (str_store_player_username, s1, ":player_id"),    
            (assign, reg1, ":gold_amount"),
            (try_begin),
                (server_add_message_to_log, "@{s1} did drop a money bag with {reg1} gold."),
            (try_end),
        ]
    ),
    
    ("cf_log_money_from_chest",
        [
            (multiplayer_is_server),
            (store_script_param, ":player_id", 1),
            (store_script_param, ":gold_requested", 2),
            (str_store_player_username, s1, ":player_id"),    
            (assign, reg1, ":gold_requested"),
            (try_begin),
                (server_add_message_to_log, "@{s1} did withdraw {reg1} money from chest."),
            (try_end),
        ]
    ),
        
    ("cf_log_money_to_chest",
        [
            (multiplayer_is_server),
            (store_script_param, ":player_id", 1),
            (store_script_param, ":gold_value", 2),
            (str_store_player_username,s1, ":player_id"),    
            (assign, reg1, ":gold_value"),
            (try_begin),
                (server_add_message_to_log, "@{s1} put {reg1} gold into a chest."),
            (try_end),
        ]
    ),
    
    ("cf_log_use_money_bag",
        [
            (multiplayer_is_server),
            (store_script_param, ":player_id", 1),
            (store_script_param, ":gold_value", 2),
            (str_store_player_username,s1, ":player_id"),    
            (assign, reg1, ":gold_value"),
            (try_begin),
                (server_add_message_to_log, "@{s1} used a money bag containing {reg1} gold."),
            (try_end),
        ]
    ),