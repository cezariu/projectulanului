quest main_quest_lv90 begin
	state start begin
	end

	state run begin
		when login or levelup with pc.get_level() >= 90 begin
			set_state(gotoinfomation)
		end
	end

	state gotoinfomation begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.title_5)
		end
		
		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_5))
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.title_5)
			end
			
			send_letter(gameforge[lang].main_quest.title_5)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_5))
			say("")
			say(string.format(gameforge[lang].main_quest._1, mob_name(20354)))
			say(gameforge[lang].main_quest._2)
		end

		when __TARGET__.target.click begin
			target.delete("__TARGET__")
			local lang = pc.get_language()
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			say(gameforge[lang].main_quest._23)
			say(gameforge[lang].main_quest._24)
			say("")
			say(gameforge[lang].main_quest._25)
			pc.setqf("1134", 150)
			pc.setqf("1137", 100)
			pc.setqf("1135", 250)
			pc.setqf("2401", 250)
			pc.setqf("2403", 200)
			pc.setqf("1192", 1)
			pc.setqf("2494", 1)
			pc.setqf("2495", 1)
			set_state(gotomission)
		end
	end

	state gotomission begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.subtitle_5)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_5))
			say("")
			say(gameforge[lang].main_quest._37)
			say(string.format("- %d %s,", pc.getqf("1134"), mob_name(1134)))
			say(string.format("- %d %s,", pc.getqf("1137"), mob_name(1137)))
			say(string.format("- %d %s,", pc.getqf("1135"), mob_name(1135)))
			say(string.format("- %d %s,", pc.getqf("2401"), mob_name(2401)))
			say(string.format("- %d %s,", pc.getqf("2403"), mob_name(2403)))
			say(string.format("- %d %s,", pc.getqf("1192"), mob_name(1192)))
			say(string.format("- %d %s,", pc.getqf("2494"), mob_name(2494)))
			say(string.format("- %d %s.", pc.getqf("2495"), mob_name(2495)))
		end

		when 1134.kill or 1137.kill or 1135.kill or 2401.kill or 2403.kill or 1192.kill or 2494.kill or 2495.kill begin
			local n = string.format("%s", npc.get_race())
			local c = pc.getqf(n)
			if c > 0 then
				pc.setqf(n, c - 1)
			end
			
			local t = pc.getqf("1134") + pc.getqf("1137") + pc.getqf("1135") + pc.getqf("2401") + pc.getqf("2403") + pc.getqf("1192") + pc.getqf("2494") + pc.getqf("2495")
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.donetitle_5)
			end
			
			send_letter(gameforge[lang].main_quest.donetitle_5)
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
			pc.give_item2(88963, 2)
			pc.give_item2(88961, 1)
			pc.change_gold(80000000)
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			local lang = pc.get_language()
			say(string.format(gameforge[lang].main_quest._51, pc.get_name()))
			say(gameforge[lang].main_quest._52)
			say("")
			say_reward(gameforge[lang].main_quest._58)
			say_reward(gameforge[lang].main_quest._68)
			say_reward(gameforge[lang].main_quest._69)
			say_reward(gameforge[lang].main_quest._70)
			pc.delqf("1134")
			pc.delqf("1137")
			pc.delqf("1135")
			pc.delqf("2401")
			pc.delqf("2403")
			pc.delqf("1192")
			pc.delqf("2494")
			pc.delqf("2495")
			set_quest_state("main_quest_lv110", "run")
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
	end
end

