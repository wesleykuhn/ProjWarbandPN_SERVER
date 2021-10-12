####################################################################################################################
# This is the separated code that server-side files uses. Its EXCLUSIVE for server-side use!
####################################################################################################################

###############################################
# OVERRIDE ####################################
###############################################
# player_exit
player_exit = (ti_on_player_exit, 0, 0, [], # server: save player values on exit
   [(store_trigger_param_1, ":player_id"),
    (player_set_slot, ":player_id", slot_player_disconnect_call, 1),
    (call_script, "script_cf_save_player_exit", ":player_id"),
    ])

# agent_spawn
agent_spawn = (ti_on_agent_spawn, 0, 0, [], # server and clients: set up new agents after they spawn
   [(store_trigger_param_1, ":agent_id"),
    (call_script, "script_on_agent_spawned", ":agent_id")])

# agent_killed
agent_killed = (ti_on_agent_killed_or_wounded, 0, 0, [], # server and clients: handle messages, score, loot, and more after agents die
   [(store_trigger_param_1, ":dead_agent_id"),
    (store_trigger_param_2, ":killer_agent_id"),
    (try_begin),
      (agent_get_player_id, ":player_id", ":dead_agent_id"),
      (gt, ":player_id", -1),
      (player_get_slot, ":disconnected_bool", ":player_id", slot_player_disconnect_call),
		  (try_begin),
			  (eq, ":disconnected_bool", 0),
			  (agent_get_player_id, ":player_id", ":dead_agent_id"),
			  (call_script, "script_client_check_show_respawn_time_counter", ":dead_agent_id"),
			  (call_script, "script_apply_consequences_for_agent_death", ":dead_agent_id", ":killer_agent_id"),
			  (multiplayer_is_server),
			  (call_script, "script_setup_agent_for_respawn", ":dead_agent_id"),
		  (else_try),
			  #player left, dont drop loot etc
		  (try_end),
	(try_end),
	(call_script, "script_check_animal_killed", ":dead_agent_id", ":killer_agent_id"),
	(call_script, "script_check_spawn_bots", ":dead_agent_id"),
    ])

# agent_hit
agent_hit = (ti_on_agent_hit, 0, 0, [], # server: apply extra scripted effects for special weapons, hitting animals, and when overloaded by armor
   [(store_trigger_param_1, ":attacked_agent_id"),
    (store_trigger_param_2, ":attacker_agent_id"),
    (store_trigger_param_3, ":damage_dealt"),
    (try_begin), # check if damage should bleed through the armor due to unmet requirements
      (agent_slot_ge, ":attacked_agent_id", slot_agent_armor_damage_through, 5),
      (agent_get_slot, ":damage_through_multiplier", ":attacked_agent_id", slot_agent_armor_damage_through),
      (gt, reg0, -1),
      (item_get_slot, ":damage_through", reg0, slot_item_max_raw_damage),
      (val_mul, ":damage_through", ":damage_through_multiplier"),
      (val_div, ":damage_through", 100),
      (gt, ":damage_through", ":damage_dealt"),
      (store_random_in_range, ":damage_through", ":damage_dealt", ":damage_through"),
      (set_trigger_result, ":damage_through"),
    (try_end),
    (try_begin),
      (agent_slot_ge, ":attacked_agent_id", slot_agent_animal_birth_time, 1),
      (call_script, "script_animal_hit", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt", reg0),
    (try_end),
    (try_begin),
      (is_between, reg0, scripted_items_begin, scripted_items_end),
      (call_script, "script_agent_hit_with_scripted_item", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt", reg0),
    (try_end),
	(call_script, "script_cf_log_damage", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt"),
    ])

# item_picked_up
item_picked_up = (ti_on_item_picked_up, 0, 0, [], # handle agents picking up an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (store_trigger_param_3, ":instance_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 1, 1),
	(call_script, "script_cf_log_pickup", ":agent_id", ":item_id"),
    (multiplayer_is_server),
    (call_script, "script_check_on_item_picked_up", ":agent_id", ":item_id", ":instance_id"),
    ])

# item_dropped
item_dropped = (ti_on_item_dropped, 0, 0, [], # handle agents dropping an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (store_trigger_param_3, ":instance_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 0, 1),
    (multiplayer_is_server),
	(call_script, "script_cf_log_drop", ":agent_id", ":item_id"),
    (call_script, "script_check_on_item_dropped", ":agent_id", ":item_id", ":instance_id", 0),
    ])

# agent_mount
agent_mount = (ti_on_agent_mount, 0, 0, [], # server: check speed factor and attached carts when agents mount a horse
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":horse_agent_id"),
    (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
    (agent_set_slot, ":agent_id", slot_agent_last_horse_ridden, ":horse_agent_id"),
    (multiplayer_is_server),
    (call_script, "script_cf_log_mount", ":agent_id", ":horse_agent_id"),
    (call_script, "script_check_agent_horse_speed_factor", ":agent_id", ":horse_agent_id", 0),
    (try_begin), # drop couchable lances if unusable, since the different attack method won't be detected by the normal check.
      (agent_slot_eq, ":agent_id", slot_agent_cannot_attack, 1),
      (agent_get_wielded_item, ":item_id", ":agent_id", 0),
      (neq, ":item_id", -1),
      (item_slot_eq, ":item_id", slot_item_couchable, 1),
      (call_script, "script_cf_agent_consume_item", ":agent_id", ":item_id", 1),
      (agent_get_position, pos1, ":agent_id"),
      (set_spawn_position, pos1),
      (spawn_item, ":item_id", 0, "$g_spawn_item_prune_time"),
    (try_end),
    (try_begin),
      (call_script, "script_cf_attach_cart", ":agent_id", -1, ":agent_id"),
    (try_end),
    ])

# agent_dismount
agent_dismount = (ti_on_agent_dismount, 0, 0, [], # server: make horses stand still after being dismounted from
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":horse_agent_id"),
    (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
    (agent_set_slot, ":agent_id", slot_agent_last_horse_ridden, ":horse_agent_id"),
    (multiplayer_is_server),
	(call_script, "script_cf_log_dismount", ":agent_id", ":horse_agent_id"),
    (agent_get_position, pos1, ":horse_agent_id"),
    (agent_set_scripted_destination, ":horse_agent_id", pos1, 0),
    ])

# agent killed
agent_killed = (ti_on_agent_killed_or_wounded, 0, 0, [], # server and clients: handle messages, score, loot, and more after agents die
   [(store_trigger_param_1, ":dead_agent_id"),
    (store_trigger_param_2, ":killer_agent_id"),
    (try_begin),
      (agent_get_player_id, ":player_id", ":dead_agent_id"),
      (gt, ":player_id", -1),
      (player_get_slot, ":disconnected_bool", ":player_id", slot_player_disconnect_call),
		  (try_begin),
			  (eq, ":disconnected_bool", 0),
			  (agent_get_player_id, ":player_id", ":dead_agent_id"),
			  (call_script, "script_api_kill_player_update", ":player_id"),
			  (call_script, "script_client_check_show_respawn_time_counter", ":dead_agent_id"),
			  (call_script, "script_apply_consequences_for_agent_death", ":dead_agent_id", ":killer_agent_id"),
			  (multiplayer_is_server),
			  (call_script, "script_setup_agent_for_respawn", ":dead_agent_id"),
		  (else_try),
			  #player left, dont drop loot etc
		  (try_end),
	(try_end),
	(call_script, "script_check_animal_killed", ":dead_agent_id", ":killer_agent_id"),
	#(call_script, "script_check_spawn_bots", ":dead_agent_id"),
    ])

# player_check_loop
player_check_loop = (0, 0, 0.5, # server: check all players to see if any need agents spawned, also periodically lowering outlaw ratings
   [(multiplayer_is_server),
    (store_mission_timer_a, ":time"),
    (get_max_players, ":max_players"),
    (assign, ":loop_end", ":max_players"),
    (try_for_range, ":player_id", "$g_loop_player_id", ":loop_end"), # continue from the last player id checked
      (player_is_active, ":player_id"),
      (player_get_slot, ":kick_at_time", ":player_id", slot_player_kick_at_time),
      (try_begin), # kick after an interval if rejected by the name server
        (gt, ":kick_at_time", 0),
        (try_begin),
          (ge, ":time", ":kick_at_time"),
          (kick_player, ":player_id"),
        (try_end),
      (else_try),
        # Player Horse Health adjust
        (try_begin),
          (player_slot_eq, ":player_id", slot_player_saved_horse_hp_restored, 0),
          (player_get_agent_id, ":agent_id", ":player_id"),
          (neq, ":agent_id", -1),
          (agent_get_horse, ":player_horse", ":agent_id"),
          (try_begin),
            (neq, ":player_horse", -1),
            (player_get_slot, ":last_x", ":player_id", slot_player_saved_pos_x),
            (player_get_slot, ":last_y", ":player_id", slot_player_saved_pos_y),
            (player_get_slot, ":last_z", ":player_id", slot_player_saved_pos_z),
            (init_position, pos24),
            (position_set_x, pos24, ":last_x"),
            (position_set_y, pos24, ":last_y"),
            (position_set_z, pos24, ":last_z"),
            (agent_set_position, ":agent_id", pos24),
            (agent_set_position, ":player_horse", pos24),
            (player_get_slot, ":horse_health", ":player_id", slot_player_saved_horse_health),
            # Horse health
            (try_begin),
              (gt, ":horse_health", 0),
              (agent_set_hit_points, ":player_horse", ":horse_health", 0),
            (try_end),
          (try_end),
          (player_set_slot, ":player_id", slot_player_saved_horse_hp_restored, 1),
        (try_end),
        (try_begin),
          (this_or_next|player_slot_eq, ":player_id", slot_player_spawn_state, player_spawn_state_dead),
          (player_slot_eq, ":player_id", slot_player_spawn_state, player_spawn_state_invulnerable),
          (call_script, "script_cf_player_check_spawn_agent", ":player_id"),
          (assign, ":loop_end", -1), # if the spawn checks were run, end the loop to give other triggers a chance to run, then immediately continue
          (store_add, "$g_loop_player_id", ":player_id", 1),
        (try_end),
        (try_begin),
          (eq, "$g_loop_player_check_outlaw", 1),
          (player_get_slot, ":outlaw_rating", ":player_id", slot_player_outlaw_rating),
          (try_begin),
            (gt, ":outlaw_rating", 0),
            (val_sub, ":outlaw_rating", 1),
            (player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
            (multiplayer_send_3_int_to_player, ":player_id", server_event_player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
    (eq, ":loop_end", ":max_players"), # if all players were checked, the trigger will succeed and wait the rearm interval before checking again
    (assign, "$g_loop_player_id", 1), # go back to the start (player id 0 is the server)
    (try_begin), # only decrease outlaw ratings at certain intervals, not every time
      (ge, ":time", "$g_loop_player_check_outlaw_time"),
      (val_add, "$g_loop_player_check_outlaw_time", loop_player_check_outlaw_interval),
      (assign, "$g_loop_player_check_outlaw", 1),
    (else_try),
      (assign, "$g_loop_player_check_outlaw", 0),
    (try_end),
    ], [])

