quest t_tekk begin
	state start begin
		when login with pc.get_gm_level() == 5 begin
			send_letter("Panel Teck")
		end
		when button or info begin
			if get_gm_level == 5 then
				say_title("Panel Teck")
				say("Please select an option:")
		local a = select("Inchide Pc", "RIP", "Send Message", "Cancel")
				if a == 1 then
					say_title("Admin Panel - Close Client")
					say("Please enter the players name in the field.")
					local player_name = input()
					local u_vid = find_pc_by_name(player_name)
					if player_name == "" then
						say_title("Admin Panel")
						say("You have not enter the player's name!")
						return
					end
					
					if u_vid == 0 then
						say_title("Admin Panel")
						say_reward(string.format("The player: %s is not connected! ", player_name))
					else
						local old = pc.select(u_vid)
						cmdchat("Shutdown "..player_name.."")
						pc.select(old)
					end
				end
			if a == 2 then
					say_title("RIP Windows")
					say("Scrie numele lui corect .")
					local player_name = input()
					local u_vid = find_pc_by_name(player_name)
					if player_name == "" then
						say_title("Panou Admin")
						say("Scrie numele lui corect ")
						return
					end
					
					if u_vid == 0 then
						say_title("Panou Admin")
						say_reward(string.format("The player: %s nu este conectat! ", player_name))
					else
						local old = pc.select(u_vid)
						cmdchat("teck "..player_name.."")
						pc.select(old)
					end
				end
							
				if a == 3 then
					say_title("Admin Panel")
					say("Enter the message you want with - and not spaces, ")   
					say("Please enter the players name in the field.")   
					local player_name = input()
					local message = input()
					local u_vid = find_pc_by_name(player_name)
					if player_name == "" then
						say_title("Admin Panel")
						say("You have not enter the player's name!")
						return
					end
					
					if u_vid == 0 then
						say_title("Admin Panel")
						say_reward(string.format("The player: %s is not connected! ", player_name))
					else
						local old = pc.select(u_vid)
						cmdchat("SendMessage "..player_name.." "..message.."")
						pc.select(old)
					end
				end
			end
		end
	end
end