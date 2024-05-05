quest main_quest_lv110 begin
	state start begin
	end

	state run begin
		when login or levelup with pc.get_level() >= 110 begin
			set_state(gotoinfomation)
		end
	end

	state gotoinfomation begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.title_6)
		end
		
		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_6))
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.title_6)
			end
			
			send_letter(gameforge[lang].main_quest.title_6)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_6))
			say("")
			say(string.format(gameforge[lang].main_quest._1, mob_name(20354)))
			say(gameforge[lang].main_quest._2)
		end

		when __TARGET__.target.click begin
			target.delete("__TARGET__")
			local lang = pc.get_language()
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			say(gameforge[lang].main_quest._26)
			say(gameforge[lang].main_quest._27)
			say(gameforge[lang].main_quest._28)
			say(gameforge[lang].main_quest._29)
			say("")
			say(gameforge[lang].main_quest._30)
			pc.setqf("3501", 50)
			pc.setqf("3405", 50)
			pc.setqf("3601", 50)
			pc.setqf("3503", 50)
			pc.setqf("3701", 50)
			pc.setqf("3102", 50)
			pc.setqf("3590", 1)
			pc.setqf("3490", 1)
			pc.setqf("3690", 1)
			pc.setqf("3790", 1)
			pc.setqf("3190", 1)
			set_state(gotomission)
		end
	end

	state gotomission begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.subtitle_6)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_6))
			say("")
			say(gameforge[lang].main_quest._37)
			say(string.format("- %d %s,", pc.getqf("3501"), mob_name(3501)))
			say(string.format("- %d %s,", pc.getqf("3405"), mob_name(3405)))
			say(string.format("- %d %s,", pc.getqf("3601"), mob_name(3601)))
			say(string.format("- %d %s,", pc.getqf("3503"), mob_name(3503)))
			say(string.format("- %d %s,", pc.getqf("3701"), mob_name(3701)))
			say(string.format("- %d %s,", pc.getqf("3102"), mob_name(3102)))
			say(string.format("- %d %s,", pc.getqf("3590"), mob_name(3590)))
			say(string.format("- %d %s,", pc.getqf("3490"), mob_name(3490)))
			say(string.format("- %d %s,", pc.getqf("3690"), mob_name(3690)))
			say(string.format("- %d %s,", pc.getqf("3790"), mob_name(3790)))
			say(string.format("- %d %s.", pc.getqf("3190"), mob_name(3190)))
		end

		when 3501.kill or 3405.kill or 3601.kill or 3503.kill or 3701.kill or 3102.kill or 3590.kill or 3490.kill or 3690.kill or 3790.kill or 3190.kill begin
			local n = string.format("%s", npc.get_race())
			local c = pc.getqf(n)
			if c > 0 then
				pc.setqf(n, c - 1)
			end
			
			local t = pc.getqf("3501") + pc.getqf("3405") + pc.getqf("3601") + pc.getqf("3503") + pc.getqf("3701") + pc.getqf("3102") + pc.getqf("3590") + pc.getqf("3490") + pc.getqf("3690") + pc.getqf("3790") + pc.getqf("3190")
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.donetitle_6)
			end
			
			send_letter(gameforge[lang].main_quest.donetitle_6)
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
			pc.give_item2(88962, 2)
			pc.give_item2(88961, 3)
			pc.change_gold(100000000)
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			local lang = pc.get_language()
			say(string.format(gameforge[lang].main_quest._51, pc.get_name()))
			say(gameforge[lang].main_quest._52)
			say("")
			say_reward(gameforge[lang].main_quest._58)
			say_reward(gameforge[lang].main_quest._71)
			say_reward(gameforge[lang].main_quest._72)
			say_reward(gameforge[lang].main_quest._73)
			pc.delqf("3501")
			pc.delqf("3405")
			pc.delqf("3601")
			pc.delqf("3503")
			pc.delqf("3701")
			pc.delqf("3102")
			pc.delqf("3590")
			pc.delqf("3490")
			pc.delqf("3690")
			pc.delqf("3790")
			pc.delqf("3190")
			set_quest_state("main_quest_lv120", "run")
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
	end
end

