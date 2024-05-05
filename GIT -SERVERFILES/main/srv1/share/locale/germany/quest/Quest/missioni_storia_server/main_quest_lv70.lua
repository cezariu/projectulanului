quest main_quest_lv70 begin
	state start begin
	end

	state run begin
		when login or levelup with pc.get_level() >= 70 begin
			set_state(gotoinfomation)
		end
	end

	state gotoinfomation begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.title_4)
		end
		
		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_4))
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.title_4)
			end
			
			send_letter(gameforge[lang].main_quest.title_4)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_4))
			say("")
			say(string.format(gameforge[lang].main_quest._1, mob_name(20354)))
			say(gameforge[lang].main_quest._2)
		end

		when __TARGET__.target.click begin
			target.delete("__TARGET__")
			local lang = pc.get_language()
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			say(gameforge[lang].main_quest._17)
			say(gameforge[lang].main_quest._18)
			say("")
			say(gameforge[lang].main_quest._19)
			say(gameforge[lang].main_quest._20)
			say(gameforge[lang].main_quest._21)
			say("")
			say(gameforge[lang].main_quest._22)
			pc.setqf("2032", 200)
			pc.setqf("2107", 200)
			pc.setqf("2311", 100)
			pc.setqf("2303", 200)
			pc.setqf("2091", 1)
			pc.setqf("2306", 1)
			set_state(gotomission)
		end
	end
	
	state gotomission begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.subtitle_4)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_4))
			say("")
			say(gameforge[lang].main_quest._37)
			say(string.format("- %d %s,", pc.getqf("2032"), mob_name(2032)))
			say(string.format("- %d %s,", pc.getqf("2107"), mob_name(2107)))
			say(string.format("- %d %s,", pc.getqf("2311"), mob_name(2311)))
			say(string.format("- %d %s,", pc.getqf("2303"), mob_name(2303)))
			say(string.format("- %d %s,", pc.getqf("2091"), mob_name(2091)))
			say(string.format("- %d %s.", pc.getqf("2306"), mob_name(2306)))
		end

		when 2032.kill or 2107.kill or 2311.kill or 2303.kill or 2091.kill or 2306.kill begin
			local n = string.format("%s", npc.get_race())
			local c = pc.getqf(n)
			if c > 0 then
				pc.setqf(n, c - 1)
			end
			
			local t = pc.getqf("2032") + pc.getqf("2107") + pc.getqf("2311") + pc.getqf("2303") + pc.getqf("2091") + pc.getqf("2306")
			if t == 0 then
				set_state(gotoreward)
			end
		end
	end

	state gotoreward begin
		when letter begin
			local lang = pc.get_language()
			local v = find_npc_by_vnum(20354)
			if v != 0 then
				target.vid("__TARGET__", v, gameforge[lang].main_quest.donetitle_4)
			end
			
			send_letter(gameforge[lang].main_quest.donetitle_4)
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
			pc.give_item2(88958, 1)
			pc.give_item2(70505, 1)
			pc.change_gold(60000000)
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			local lang = pc.get_language()
			say(string.format(gameforge[lang].main_quest._51, pc.get_name()))
			say(gameforge[lang].main_quest._52)
			say("")
			say_reward(gameforge[lang].main_quest._58)
			say_reward(gameforge[lang].main_quest._82)
			say_reward(gameforge[lang].main_quest._64)
			say_reward(gameforge[lang].main_quest._81)
			pc.delqf("2032")
			pc.delqf("2107")
			pc.delqf("2311")
			pc.delqf("2303")
			pc.delqf("2091")
			pc.delqf("2306")
			set_quest_state("main_quest_lv90", "run")
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
	end
end

