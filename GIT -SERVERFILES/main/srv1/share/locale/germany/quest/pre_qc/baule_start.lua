quest baule_start begin
	state start begin
		when 50187.use begin
			local lang = pc.get_language()
			if pc.get_level() >= 1 then
				if not pc.can_warp() then
					syschat(gameforge[lang].reset_scroll._35)
					return
				end
				
				pc.remove_item(50187, 1)
				chat(string.format(gameforge[lang].baule_start._1, item_name(50187)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50188, 1)
				pc.give_item2(72725, 1)
				pc.give_item2(72729, 1)
				pc.give_item2(53276, 1)
				pc.give_item2(70038, 1)
				pc.give_item2(71085, 1)
				pc.give_item2(88935, 1)
				pc.give_item2(88936, 1)
				pc.give_item2(88937, 1)
				pc.give_item2(88938, 1)
				pc.give_item2(88939, 1)
				pc.give_item2(88940, 1)
				pc.give_item2(71127, 1)
				pc.give_item2(30897, 1)
				pc.give_item2(85084, 1)
				if pc.get_sex() == 0 then
					pc.give_item2(41856, 1)
					pc.give_item2(45596, 1)
				elseif pc.get_sex() == 1 then
					pc.give_item2(41858, 1)
					pc.give_item2(45598, 1)
				end
				if pc.get_job() == 0 then
					pc.give_item2(40108, 1)
					pc.give_item2(40111, 1)
				elseif pc.get_job() == 1 then
					pc.give_item2(40109, 1)
					pc.give_item2(40110, 1)
				elseif pc.get_job() == 2 then
					pc.give_item2(40108, 1)
				elseif pc.get_job() == 3 then
					pc.give_item2(40112, 1)
					pc.give_item2(40113, 1)
				end
			else
				say_title(string.format("%s:", item_name(50187)))
				say("")
				say(string.format(gameforge[lang].baule_start._3, 1))
			end
		end

		when 50188.use begin
			local lang = pc.get_language()
			if pc.get_level() >= 10 then
				if not pc.can_warp() then
					syschat(gameforge[lang].reset_scroll._35)
					return
				end
				
				pc.remove_item(50188, 1)
				chat(string.format(gameforge[lang].baule_start._1, item_name(50188)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50190, 1)
				pc.give_item2(88960, 5)
			else
				say_title(string.format("%s:", item_name(50188)))
				say("")
				say(string.format(gameforge[lang].baule_start._3, 10))
			end
		end

		when 50190.use begin
			local lang = pc.get_language()
			if pc.get_level() >= 30 then
				if not pc.can_warp() then
					syschat(gameforge[lang].reset_scroll._35)
					return
				end
				
				pc.remove_item(50190,1)
				chat(string.format(gameforge[lang].baule_start._1, item_name(50190)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50192, 1)
				pc.give_item2(88960, 5)
				pc.give_item2(88959, 700)
			else
				say_title(string.format("%s:", item_name(50190)))
				say("")
				say(string.format(gameforge[lang].baule_start._3, 30))
			end
		end

		when 50192.use begin
			local lang = pc.get_language()
			if pc.get_level() >= 50 then
				if not pc.can_warp() then
					syschat(gameforge[lang].reset_scroll._35)
					return
				end
				
				pc.remove_item(50192, 1)
				chat(string.format(gameforge[lang].baule_start._1, item_name(50192)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50194, 1)
				pc.give_item2(88911, 1)
				pc.give_item2(88963, 10)
				pc.give_item2(88918, 1)
				pc.give_item2(88910, 1)
			else
				say_title(string.format("%s:", item_name(50192)))
				say("")
				say(string.format(gameforge[lang].baule_start._3, 50))
			end
		end

		when 50194.use begin
			local lang = pc.get_language()
			if pc.get_level() >= 75 then
				if not pc.can_warp() then
					syschat(gameforge[lang].reset_scroll._35)
					return
				end
				
				pc.remove_item(50194, 1)
				chat(string.format(gameforge[lang].baule_start._1, item_name(50194)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50195, 1)
				pc.give_item2(88930, 1)
				pc.give_item2(88932, 1)
				pc.give_item2(88933, 1)
				pc.give_item2(88934, 1)
			else
				say_title(string.format("%s:", item_name(50194)))
				say("")
				say(string.format(gameforge[lang].baule_start._3, 75))
			end
		end

		when 50195.use begin
			local lang = pc.get_language()
			if pc.get_level() >= 100 then
				if not pc.can_warp() then
					syschat(gameforge[lang].reset_scroll._35)
					return
				end
				
				pc.remove_item(50195, 1)
				chat(string.format(gameforge[lang].baule_start._1, item_name(50195)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(50196, 1)
				pc.give_item2(88931, 1)
				pc.give_item2(88964, 1)
				pc.give_item2(88965, 1)
				pc.give_item2(88966, 1)
				pc.give_item2(88958, 1)
				pc.give_item2(88962, 5)
				pc.give_item2(88912, 1)
			else
				say_title(string.format("%s:", item_name(50195)))
				say("")
				say(string.format(gameforge[lang].baule_start._3, 100))
			end
		end

		when 50196.use begin
			local lang = pc.get_language()
			if pc.get_level() >= 120 then
				if not pc.can_warp() then
					syschat(gameforge[lang].reset_scroll._35)
					return
				end
				
				pc.remove_item(50196, 1)
				chat(string.format(gameforge[lang].baule_start._1, item_name(50196)))
				chat(gameforge[lang].baule_start._2)
				pc.give_item2(88914, 1)
				pc.give_item2(88915, 1)
				pc.give_item2(88913, 1)
				pc.give_item2(88960, 10)
				pc.give_item2(88958, 1)
				pc.give_item2(88961, 3)
				pc.give_item2(88962, 10)
				pc.give_item2(88965, 5)
			else
				say_title(string.format("%s:", item_name(50196)))
				say("")
				say(string.format(gameforge[lang].baule_start._3, 120))
			end
		end
	end
end

