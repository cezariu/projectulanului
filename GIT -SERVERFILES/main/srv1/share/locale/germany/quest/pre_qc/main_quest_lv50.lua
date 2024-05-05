quest main_quest_lv50 begin
	state start begin
	end

	state run begin
		when login or levelup with pc.get_level() >= 50 begin
			set_state(gotoinfomation)
		end
	end

	state gotoinfomation begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.title_3)
		end
		
		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_3))
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.title_3)
			end
			
			send_letter(gameforge[lang].main_quest.title_3)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.title_3))
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
			say(gameforge[lang].main_quest._14)
			say(gameforge[lang].main_quest._15)
			say(gameforge[lang].main_quest._16)
			pc.setqf("903", 100)
			pc.setqf("1107", 50)
			pc.setqf("1601", 80)
			pc.setqf("1402", 35)
			pc.setqf("2203", 100)
			pc.setqf("2202", 50)
			pc.setqf("1901", 1)
			pc.setqf("2206", 1)
			set_state(gotomission)
		end
	end
	
	state gotomission begin
		when letter begin
			send_letter(gameforge[pc.get_language()].main_quest.subtitle_3)
		end

		when button or info begin
			local lang = pc.get_language()
			say_title(string.format("%s:", gameforge[lang].main_quest.subtitle_3))
			say("")
			say(gameforge[lang].main_quest._37)
			say(string.format("- %d %s,", pc.getqf("903"), mob_name(903)))
			say(string.format("- %d %s,", pc.getqf("1107"), mob_name(1107)))
			say(string.format("- %d %s,", pc.getqf("1601"), mob_name(1601)))
			say(string.format("- %d %s,", pc.getqf("1402"), mob_name(1402)))
			say(string.format("- %d %s,", pc.getqf("2203"), mob_name(2203)))
			say(string.format("- %d %s,", pc.getqf("2202"), mob_name(2202)))
			say(string.format("- %d %s,", pc.getqf("1901"), mob_name(1901)))
			say(string.format("- %d %s.", pc.getqf("2206"), mob_name(2206)))
		end

		when 903.kill or 1107.kill or 1601.kill or 1402.kill or 2203.kill or 2202.kill or 1901.kill or 2206.kill begin
			local n = string.format("%s", npc.get_race())
			local c = pc.getqf(n)
			if c > 0 then
				pc.setqf(n, c - 1)
			end
			
			local t = pc.getqf("903") + pc.getqf("1107") + pc.getqf("1601") + pc.getqf("1402") + pc.getqf("2203") + pc.getqf("2202") + pc.getqf("1901") + pc.getqf("2206")
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
				target.vid("__TARGET__", v, gameforge[lang].main_quest.donetitle_3)
			end
			
			send_letter(gameforge[lang].main_quest.donetitle_3)
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
			pc.give_item2(88959, 100)
			pc.give_item2(88963, 2)
			pc.change_gold(40000000)
			say_title(string.format("%s:", mob_name(20354)))
			say("")
			local lang = pc.get_language()
			say(string.format(gameforge[lang].main_quest._51, pc.get_name()))
			say(gameforge[lang].main_quest._52)
			say("")
			say_reward(gameforge[lang].main_quest._58)
			say_reward(gameforge[lang].main_quest._65)
			say_reward(gameforge[lang].main_quest._66)
			say_reward(gameforge[lang].main_quest._67)
			pc.delqf("903")
			pc.delqf("1107")
			pc.delqf("1601")
			pc.delqf("1402")
			pc.delqf("2203")
			pc.delqf("2202")
			pc.delqf("1901")
			pc.delqf("2206")
			set_quest_state("main_quest_lv70", "run")
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
	end
end

