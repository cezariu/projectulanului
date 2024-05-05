quest main_quest_lv120 begin
	state start begin
	end

	state run begin
		when login or levelup with pc.get_level() >= 120 begin
			set_state(gotoinfomation)
		end
	end

	state gotoinfomation begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.title_7)
		end
		
		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_7))
			say("")
			say(string.format(gameforge[lang].main_quest._1, mob_name(20354)))
			say(gameforge[lang].main_quest._2)
			set_state(gototeacher)
		end
	end

	state gototeacher begin
		when letter begin
			local lang = pc.get_language()
			local v = find_npc_by_vnum(20354)
			if v != 0 then
				target.vid("__TARGET__", v, gameforge[lang].main_quest.title_7)
			end
			
			send_letter(gameforge[lang].main_quest.title_7)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_7))
			say("")
			say(string.format(gameforge[lang].main_quest._1, mob_name(20354)))
			say(gameforge[lang].main_quest._2)
		end

		when __TARGET__.target.click begin
			target.delete("__TARGET__")
			local lang = pc.get_language()
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			say(string.format(gameforge[lang].main_quest._31, mob_name(8512)))
			say(gameforge[lang].main_quest._32)
			say(gameforge[lang].main_quest._33)
			say(gameforge[lang].main_quest._34)
			say("")
			say(gameforge[lang].main_quest._35)
			say(gameforge[lang].main_quest._36)
			pc.setqf("8512", 1)
			pc.setqf("dungeon", 0)
			set_state(gotomission)
		end
	end

	state gotomission begin
		when end_azrael.server_timer begin
			local arg = get_server_timer_arg()
			clear_server_timer("loop_azrael", arg)
			clear_server_timer("end_azrael", arg)
			if d.find(arg) then
				d.kill_all(arg)
				d.exit_all_lobby(arg, 3)
			end
		end

		when 8512.kill begin
			local idx = pc.get_map_index()
			if idx >= 3560000 and idx < 3570000 then
				d.notice(idx, 988, "", true)
				d.notice(idx, 989, "", true)
				server_timer("end_azrael", 10, idx)
				
				local c = pc.getf("main_quest_lv120", "8512")
				if c > 0 then
					pc.setf("main_quest_lv120", "8512", c - 1)
				end
				
				local t = pc.getf("main_quest_lv120", "8512")
				if t == 0 then
					pc.setf("main_quest_lv120", "dungeon", 2)
					pc.setf("main_quest_lv120", "success", 0)
				end
				
				pc.setf("dungeon", string.format("%d", idx), 0)
			end
		end

		when loop_azrael.server_timer begin
			local arg = get_server_timer_arg()
			if d.find(arg) then
				local s = d.getf(arg, "step")
				if s > 0 then
					if s == 1 then
						d.notice(arg, 984, "", true)
					else
						d.notice(arg, 985, string.format("%d", s), true)
					end
					
					d.setf(arg, "step", s - 1)
				else
					d.notice(arg, 986, "", true)
					clear_server_timer("loop_azrael", arg)
					d.kill_all(arg)
					d.exit_all_lobby(arg, 3)
				end
			end
		end

		when logout begin
			local idx = pc.get_map_index()
			if idx >= 3560000 and idx < 3570000 then
				pc.setf("main_quest_lv120", "disconnect", get_global_time() + 300)
			end
		end

		when login begin
			if pc.getqf("dungeon") == 2 then
				pc.delqf("dungeon")
				set_state(gotoreward)
			end
			
			local idx = pc.get_map_index()
			if idx == 356 then
				pc.warp(645800, 351400)
			elseif idx >= 3560000 and idx < 3570000 then
				pc.set_warp_location(361, 6458, 3514)
				pc.setf("main_quest_lv120", "idx", idx)
				pc.setf("main_quest_lv120", "ch", pc.get_channel_id())
				if pc.getqf("dungeon") == 0 then
					pc.setqf("dungeon", idx)
					d.setf(idx, "floor", 1)
					d.setf(idx, "step", 9)
					d.notice(idx, 987, "", true)
					d.spawn_mob(idx, 8512, 384, 657)
					server_timer("loop_azrael", 60, idx)
				end
			end
		end

		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.subtitle_7)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_7))
			say("")
			local idx = pc.get_map_index()
			if idx >= 3560000 and idx < 3570000 then
				say(string.format(gameforge[lang].main_quest._38, mob_name(8512)))
				say(gameforge[lang].main_quest._39)
				--wait()
				--send_letter(gameforge[lang].main_quest.subtitle_7)
			else
				say(gameforge[lang].main_quest._37)
				say(string.format("- %d %s.", pc.getqf("8512"), mob_name(8512)))
				say(gameforge[lang].main_quest._40)
				local s = select(gameforge[lang].main_quest._41, gameforge[lang].main_quest._42)
				if s == 1 then
					say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_7))
					say("")
					if party.is_party() then
						say(gameforge[lang].main_quest._43)
						--wait()
						--send_letter(gameforge[lang].main_quest.subtitle_7)
						return
					end
					
					if pc.get_map_index() != 361 then
						say(gameforge[lang].main_quest._44)
						say(gameforge[lang].main_quest._45)
						return
					end
					
					local r = pc.getqf("success") - get_time()
					if r > 0 then
						local goahead = 1
						local rejoinTIME = pc.getf("catacombe", "disconnect") - get_global_time()
						if rejoinTIME > 0 then
							local rejoinIDX = pc.getf("catacombe", "idx")
							if rejoinIDX > 0 then
								local rejoinCH = pc.getf("catacombe", "ch")
								if rejoinCH != pc.get_channel_id() then
									say(string.format(gameforge[lang].common.dungeon_26, rejoinCH))
									return
								end
								
								if d.find(rejoinIDX) then
									goahead = 0
									pc.warp(1528200, 2318700, rejoinIDX)
								end
							end
						end
						
						if goahead == 1 then
							local d1 = math.floor(r / 3600)
							local d2 = math.floor((r - (d1 * 3600))) / 60
							if d1 < 0 then
								d1 = 0
							end
							
							if d2 < 0 then
								d2 = 0
							end
							
							j = string.format(gameforge[lang].main_quest._47, d1, d2)
							say(string.format(gameforge[lang].main_quest._48, j))
							--wait()
							--send_letter(gameforge[lang].main_quest.subtitle_7)
						end
					else
						say(gameforge[lang].main_quest._46)
						wait()
						pc.setqf("success", get_time() + 60 * 60 * 8)
						pc.setqf("dungeon", 0)
						d.join_cords(356, 15282, 23187)
					end
				else
					send_letter(gameforge[lang].main_quest.subtitle_7)
				end
			end
		end
	end

	state gotoreward begin
		when letter begin
			local lang = pc.get_language()
			local v = find_npc_by_vnum(20354)
			if v != 0 then
				target.vid("__TARGET__", v, gameforge[lang].main_quest.donetitle_7)
			end
			
			send_letter(gameforge[lang].main_quest.donetitle_7)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.donetitle_1))
			say("")
			say(gameforge[lang].main_quest._49)
			say(string.format(gameforge[lang].main_quest._50, mob_name(20354)))
		end

		when __TARGET__.target.click begin
			target.delete("__TARGET__")
			pc.give_item2(88960, 2)
			pc.give_item2(88967, 1)
			pc.give_item2(88961, 1)
			pc.give_item2(88963, 1)
			pc.give_item2(88962, 1)
			pc.give_item2(88965, 1)
			pc.change_gold(150000000)
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			local lang = pc.get_language()
			say(gameforge[lang].main_quest._53)
			say(gameforge[lang].main_quest._54)
			say(string.format(gameforge[lang].main_quest._55, mob_name(8512)))
			say("")
			say(gameforge[lang].main_quest._56)
			say(gameforge[lang].main_quest._57)
			wait()
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			say_reward(gameforge[lang].main_quest._58)
			say_reward(gameforge[lang].main_quest._74)
			say_reward(gameforge[lang].main_quest._75)
			say_reward(gameforge[lang].main_quest._76)
			say_reward(gameforge[lang].main_quest._77)
			say_reward(gameforge[lang].main_quest._78)
			say_reward(gameforge[lang].main_quest._79)
			say_reward(gameforge[lang].main_quest._80)
			pc.delqf("8512")
			pc.delqf("success")
			clear_letter()
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
	end
end

