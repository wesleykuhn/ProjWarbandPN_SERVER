####################################################################################################################
# This is the separated code that server-side files uses. Its EXCLUSIVE for server-side use!
####################################################################################################################

# SCRIPTS TO OVERRIDE
# game_receive_url_response

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