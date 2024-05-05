quest main_quest_lv30 begin
	state start begin
	end

	state run begin
		when login or levelup with pc.get_level() >= 30 begin
			set_state(gotoinfomation)
		end
	end

	state gotoinfomation begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.title_2)
		end
		
		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_2))
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.title_2)
			end
			
			send_letter(gameforge[lang].main_quest.title_2)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_2))
			say("")
			say(string.format(gameforge[lang].main_quest._1, mob_name(20354)))
			say(gameforge[lang].main_quest._2)
		end

		when __TARGET__.target.click begin
			target.delete("__TARGET__")
			local lang = pc.get_language()
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			say(gameforge[lang].main_quest._11)
			say(gameforge[lang].main_quest._12)
			say("")
			say(gameforge[lang].main_quest._13)
			say(gameforge[lang].main_quest._14)
			pc.setqf("636", 50)
			pc.setqf("602", 30)
			pc.setqf("756", 20)
			pc.setqf("757", 30)
			pc.setqf("691", 1)
			set_state(gotomission)
		end
	end

	state gotomission begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.subtitle_2)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_2))
			say("")
			say(gameforge[lang].main_quest._37)
			say(string.format("- %d %s,", pc.getqf("636"), mob_name(636)))
			say(string.format("- %d %s,", pc.getqf("602"), mob_name(602)))
			say(string.format("- %d %s,", pc.getqf("756"), mob_name(756)))
			say(string.format("- %d %s,", pc.getqf("757"), mob_name(757)))
			say(string.format("- %d %s.", pc.getqf("691"), mob_name(691)))
		end

		when 636.kill or 602.kill or 756.kill or 757.kill or 691.kill begin
			local n = string.format("%s", npc.get_race())
			local c = pc.getqf(n)
			if c > 0 then
				pc.setqf(n, c - 1)
			end
			
			local t = pc.getqf("636") + pc.getqf("602") + pc.getqf("756") + pc.getqf("757") + pc.getqf("691")
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.donetitle_2)
			end
			
			send_letter(gameforge[lang].main_quest.donetitle_2)
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
			pc.give_item2(70500, 1)
			pc.give_item2(88958, 1)
			pc.change_gold(20000000)
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			local lang = pc.get_language()
			say(string.format(gameforge[lang].main_quest._51, pc.get_name()))
			say(gameforge[lang].main_quest._52)
			say("")
			say_reward(gameforge[lang].main_quest._58)
			say_reward(gameforge[lang].main_quest._62)
			say_reward(gameforge[lang].main_quest._63)
			say_reward(gameforge[lang].main_quest._64)
			pc.delqf("636")
			pc.delqf("602")
			pc.delqf("756")
			pc.delqf("757")
			pc.delqf("691")
			set_quest_state("main_quest_lv50", "run")
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
	end
end

