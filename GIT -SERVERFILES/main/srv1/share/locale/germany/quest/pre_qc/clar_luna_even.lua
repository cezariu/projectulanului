quest event_mingi begin
	state start begin
		function clear_state()
			clear_server_timer("ballon_event", get_server_timer_arg())
			clear_server_timer("ballon_event_half", get_server_timer_arg())
			clear_server_timer("ballon_event_40", get_server_timer_arg())
			clear_server_timer("ballon_event_50", get_server_timer_arg())
			game.set_event_flag("mingi_event", 0)
			game.set_event_flag("drop_ballon", 0)
			game.set_event_flag("ballon_event", 0)
		end
		
		when login with game.get_event_flag("mingi_event") == 1 begin
			send_letter("Cuferele Clar Luna")
		end
		
		when button or info begin
			local timer = game.get_event_flag("ballon_event")
			if game.get_event_flag("mingi_event") == 0 then
				say_title("Cuferele Clar Luna")
				say("")
				say("Imi pare rau, evenimentul a luat sfarsit.")
				say("Din pacate ai sosit prea tarziu, oricum")
				say("ramai cu ochii in patru, alte evenimente")
				say("vor urma in curand!")
				say("")
				return
			end
			if game.get_event_flag("mingi_event") == 1 then
				say_title("Cuferele Clar Luna")
				say("Evenimentul Cuferele Clar Luna este deschis chiar acum!")
				say("Omoara mosntrii apropiati de nivelul tau si obtine")
				say("cuferele aurite si stralucitoare ale lunii!")
				say("")
				--say_reward(string.format("Mai sunt %s din eveniment!", get_time_remaining(timer-get_global_time())))
			end
		end
		
		when kill with game.get_event_flag("mingi_event") == 1 begin
			mid = pc.get_map_index()
			
			--if (mid == 1 or mid == 3 or mid == 21 or mid == 23 or mid == 41 or mid == 43 or mid == 64 or mid == 63) and pc.get_level() <= 60 then
			local chance = number(1, 200)
			local chance_max = game.get_event_flag("drop_ballon")
			if chance <= chance_max then
				game.drop_item_with_ownership(50011)
			end
			--end
			
			--if (mid == 71 or mid == 72 or mid == 73 or mid == 104 or mid == 217 or mid == 61 or mid == 68) and pc.get_level() <= 95 then
				-- local chance = number(1, 200)
				-- local chance_max = game.get_event_flag("drop_ballon")
				-- if chance <= chance_max then
					-- game.drop_item_with_ownership(50011)
				-- end
			--end
			
			--if (mid == 209 or mid == 210 or mid == 301 or mid == 302 or mid == 303 or mid == 304) and pc.get_level() <= 120 then
				-- local chance = number(1, 200)
				-- local chance_max = game.get_event_flag("drop_ballon")
				-- if chance <= chance_max then
					-- game.drop_item_with_ownership(50011)
				-- end
			--end
		end
			
		when 20023.chat."Eveniment Clar Luna" with pc.is_gm() and pc.get_name() == "[SA]K1LL3R" or pc.get_name() == "[SA]Moralised" or pc.get_name() == "[GA]salvE" begin
			table_rate = {3, 5, 6, 7}
			
			if game.get_event_flag("mingi_event") == 1 then
				say_title("Magazin General - Event")
				say("")
				say("Evenimentul este deja pornit,")
				say("doresti sa inchizi evenimentul?")
				say("")
				if (select("Da", "Nu") == 1) then
					notice_all("Evenimentul a fost inchis de catre echipa Zentoria2.")
					event_mingi.clear_state()
				end
			end
			if game.get_event_flag("mingi_event") == 0 then
				say_title("Magazin General - Event")
				say("")
				say("Manage Event:")
				say("")
				local manage = select("Deschide Eveniment", "Curata Timer/Event_Flag", "Renunta")
				if manage == 3 then return end
				if manage == 1 then
					say_title("Magazin General - Event")
					say("")
					say("Alege o metoda:")
					say("")
					say_reward("ATENTIE: Timpul se calculeaza in minute!")
					say("")
					local metoda = select("Scrie Timpul", "Renunta")
					if metoda == 2 then return end
					if metoda == 1 then
						say_title("Magazin General - Event")
						say("")
						say("Insereaza cat timp va tine evenimentul:")
						say("")
						say_reward("ATENTIE: Timpul se calculeaza in minute!")
						say("")
						local input = tonumber(input())
						if input == nil then
							say_title("Magazin General - Event")
							say("")
							say("Trebuie sa scri ceva pentru ca evenimentul sa inceapa.")
							say("")
							return
						end
						if input <= 10080 then
							if input >= 1 then
								say_title("Magazin General - Event")
								say("")
								say("Vad ca esti foarte hotarat, asa sa fie.")
								event_mingi.clear_state()
								wait()
								game.set_event_flag("ballon_event", get_global_time() + input * 60)
								game.set_event_flag("mingi_event", 1)
								game.set_event_flag("drop_ballon", table_rate[1])
								server_timer("ballon_event", input * 60, get_server_timer_arg())
								server_timer("ballon_event_half", input * 60/2, get_server_timer_arg())
								server_timer("ballon_event_40", input * 60/2*1.5, get_server_timer_arg())
								server_timer("ballon_event_50", input * 60/2*1.5*1.22, get_server_timer_arg())
								notice_all("Evenimentul Cufarul Clar Luna a fost deschis!")
								notice_all(string.format("Acesta a fost setat pentru inchidere in %s ", get_time_remaining(input * 60)))
								return
							end
						else
							say_title("Magazin General - Event")
							say("")
							say("Erroare - Timp prea mare!")
							return
						end
						if input <= 0 then
							say_title("Magazin General - Event")
							say("")
							say("Erroare - Timp prea mic!")
							return
						end
					end
				end
				if manage == 2 then
					say_title("Magazin General - Event")
					say("")
					say("Eveniment curatat cu succes.")
					say("")
					event_mingi.clear_state()
				end
			end
		end

		when ballon_event.server_timer begin
			event_mingi.clear_state()
			notice_all("Timpul s-a sfarsit,")
			notice_all("Evenimentul Cufere Clar de Luna a fost inchis.")
			notice_all("Va multumim pentru participare!")
		end
		
		when ballon_event_half.server_timer begin
			table_rate = {3, 5, 6, 7}
			local timer = game.get_event_flag("ballon_event")
			
			game.set_event_flag("drop_ballon", table_rate[2])
			notice_all(string.format("Mai sunt %s pana la incheierea evenimentului", get_time_remaining(timer-get_global_time())))
			notice_all("Dropul Cuferelor Clar de Luna a fost marit!")
			notice_all("Drop Precedent ".. table_rate[1] .."%, Drop actual ".. table_rate[2].."%")
		end
		
		when ballon_event_40.server_timer begin
			table_rate = {3, 5, 6, 7}
			local timer = game.get_event_flag("ballon_event")
			
			game.set_event_flag("drop_ballon", table_rate[3])
			notice_all(string.format("Mai sunt %s pana la incheierea evenimentului", get_time_remaining(timer-get_global_time())))
			notice_all("Dropul Cuferelor Clar de Luna a fost marit!")
			notice_all("Drop Precedent ".. table_rate[2] .."%, Drop actual ".. table_rate[3].."%")
		end
		
		when ballon_event_50.server_timer begin
			table_rate = {3, 5, 6, 7}
			local timer = game.get_event_flag("ballon_event")
			
			game.set_event_flag("drop_ballon", table_rate[4])
			notice_all(string.format("Mai sunt %s pana la incheierea evenimentului", get_time_remaining(timer-get_global_time())))
			notice_all("Dropul Cuferelor Clar de Luna a fost marit!")
			notice_all("Drop Precedent ".. table_rate[3] .."%, Drop actual ".. table_rate[4].."%")
		end
	end
end