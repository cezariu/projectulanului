quest main_quest_lv10 begin
	state start begin
		when login or levelup with pc.get_level() >= 10 begin
			set_state(gotoinfomation)
		end
	end

	state gotoinfomation begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.title_1)
		end
		
		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_1))
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.title_1)
			end
			
			send_letter(gameforge[lang].main_quest.title_1)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_1))
			say("")
			say(string.format(gameforge[lang].main_quest._1, mob_name(20354)))
			say(gameforge[lang].main_quest._2)
		end

		when __TARGET__.target.click begin
			target.delete("__TARGET__")
			local lang = pc.get_language()
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			say(string.format(gameforge[lang].main_quest._3, pc.get_name()))
			say(gameforge[lang].main_quest._4)
			say("")
			say(gameforge[lang].main_quest._5)
			say(gameforge[lang].main_quest._6)
			say(gameforge[lang].main_quest._7)
			say(gameforge[lang].main_quest._8)
			say("")
			say(gameforge[lang].main_quest._9)
			say(string.format(gameforge[lang].main_quest._10, mob_name(8512)))
			say(gameforge[lang].main_quest._9)
			pc.setqf("101", 20)
			pc.setqf("173", 30)
			pc.setqf("191", 1)
			pc.setqf("192", 1)
			pc.setqf("193", 1)
			pc.setqf("194", 1)
			set_state(gotomission)
		end
	end

	state gotomission begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.subtitle_1)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_1))
			say("")
			say(gameforge[lang].main_quest._37)
			say(string.format("- %d %s,", pc.getqf("101"), mob_name(101)))
			say(string.format("- %d %s,", pc.getqf("173"), mob_name(173)))
			say(string.format("- %d %s,", pc.getqf("191"), mob_name(191)))
			say(string.format("- %d %s,", pc.getqf("192"), mob_name(192)))
			say(string.format("- %d %s,", pc.getqf("193"), mob_name(193)))
			say(string.format("- %d %s.", pc.getqf("194"), mob_name(194)))
		end

		when 101.kill or 173.kill or 191.kill or 192.kill or 193.kill or 194.kill begin
			local n = string.format("%s", npc.get_race())
			local c = pc.getqf(n)
			if c > 0 then
				pc.setqf(n, c - 1)
			end
			
			local t = pc.getqf("101") + pc.getqf("173") + pc.getqf("191") + pc.getqf("192") + pc.getqf("193") + pc.getqf("194")
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.donetitle_1)
			end
			
			send_letter(gameforge[lang].main_quest.donetitle_1)
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
			pc.give_item2(88967, 1)
			pc.give_item2(88960, 1)
			pc.change_gold(5000000)
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			local lang = pc.get_language()
			say(string.format(gameforge[lang].main_quest._51, pc.get_name()))
			say(gameforge[lang].main_quest._52)
			say("")
			say_reward(gameforge[lang].main_quest._58)
			say_reward(gameforge[lang].main_quest._59)
			say_reward(gameforge[lang].main_quest._60)
			say_reward(gameforge[lang].main_quest._61)
			pc.delqf("101")
			pc.delqf("173")
			pc.delqf("191")
			pc.delqf("192")
			pc.delqf("193")
			pc.delqf("194")
			set_quest_state("main_quest_lv30", "run")
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
	end
end

