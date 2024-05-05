quest give_basic_weapon begin
	state start begin
		when login begin
			local lang = pc.get_language()
			say_title(gameforge[lang].give_basic_weapon._1)
			say("")
			say(gameforge[lang].give_basic_weapon._2)
			say("")
			say(gameforge[lang].give_basic_weapon._3)
			say(gameforge[lang].give_basic_weapon._4)
			say(gameforge[lang].give_basic_weapon._5)
			say("")
			say(gameforge[lang].give_basic_weapon._6)
			say(gameforge[lang].give_basic_weapon._7)
			say(gameforge[lang].give_basic_weapon._8)
			chat(gameforge[lang].give_basic_weapon._9)
			notice_all(904, pc.get_name())
			set_state(__COMPLETE__)
		end
	end

	state __COMPLETE__ begin
		when login begin
			local lang = pc.get_language()
			chat(string.format(gameforge[lang].give_basic_weapon._10, pc.get_name()))
			chat(gameforge[lang].give_basic_weapon._11)
			chat(gameforge[lang].give_basic_weapon._12)
			chat(gameforge[lang].give_basic_weapon._13)
			chat(gameforge[lang].give_basic_weapon._14)
		end
	end
end

