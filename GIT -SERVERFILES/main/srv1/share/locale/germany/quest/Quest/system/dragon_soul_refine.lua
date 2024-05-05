quest dragon_soul_refine begin
	state start begin
		when 20001.chat."Shop of the Refined" begin
			npc.open_shop(65)
			setskin(NOWINDOW)
		end
		
		when 20001.chat."Dragon Stone Process" begin
			local lang = pc.get_language()
			say_title(string.format("%s:", mob_name(20001)))
			say("")
			say(gameforge[lang].dragon_soul_refine._1)
			say(gameforge[lang].dragon_soul_refine._2)
			say(gameforge[lang].dragon_soul_refine._3)
			say("")
			say(gameforge[lang].dragon_soul_refine._4)
			say(gameforge[lang].dragon_soul_refine._5)
			say(gameforge[lang].dragon_soul_refine._6)
			say(gameforge[lang].dragon_soul_refine._7)
			ds.open_refine_window()
			setskin(NOWINDOW)
		end
	end
end

