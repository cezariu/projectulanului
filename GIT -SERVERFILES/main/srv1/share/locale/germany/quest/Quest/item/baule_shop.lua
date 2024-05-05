quest baule_lega begin
	state start begin
		when 10969.use begin
			if pc.get_level() >= 1 then
				if not pc.can_warp() then
					syschat(gameforge[pc.get_language()].reset_scroll._35)
					return
				end
				
				pc.remove_item(10969, 1)
				local lang = pc.get_language()
				chat(string.format(gameforge[lang].baule_start._1, item_name(10969)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50512, 1)
				pc.give_item2(71227, 1)
				pc.give_item2(71235, 1)
				pc.give_item2(53250, 1)
				pc.give_item2(85112, 1)
				pc.give_item2(40005, 1)
				pc.give_item2(40006, 1)
				pc.give_item2(40007, 1)
			end
		end
		
		when 10970.use begin
			if pc.get_level() >= 1 then
				if not pc.can_warp() then
					syschat(gameforge[pc.get_language()].reset_scroll._35)
					return
				end
				
				pc.remove_item(10970, 1)
				local lang = pc.get_language()
				chat(string.format(gameforge[lang].baule_start._1, item_name(10970)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50512, 1)
				pc.give_item2(71228, 1)
				pc.give_item2(71235, 1)
				pc.give_item2(53250, 1)
				pc.give_item2(85112, 1)
				pc.give_item2(40005, 1)
				pc.give_item2(40006, 1)
				pc.give_item2(40007, 1)
			end
		end
		
		when 10971.use begin
			if pc.get_level() >= 1 then
				if not pc.can_warp() then
					syschat(gameforge[pc.get_language()].reset_scroll._35)
					return
				end
				
				pc.remove_item(10971, 1)
				local lang = pc.get_language()
				chat(string.format(gameforge[lang].baule_start._1, item_name(10971)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50512, 1)
				pc.give_item2(71227, 1)
				pc.give_item2(71235, 1)
				pc.give_item2(53250, 1)
				pc.give_item2(85148, 1)
			end
		end
		
		when 10972.use begin
			if pc.get_level() >= 1 then
				if not pc.can_warp() then
					syschat(gameforge[pc.get_language()].reset_scroll._35)
					return
				end
				
				pc.remove_item(10972, 1)
				local lang = pc.get_language()
				chat(string.format(gameforge[lang].baule_start._1, item_name(10972)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50512, 1)
				pc.give_item2(71228, 1)
				pc.give_item2(71235, 1)
				pc.give_item2(53250, 1)
				pc.give_item2(85148, 1)
			end
		end
	end
end

