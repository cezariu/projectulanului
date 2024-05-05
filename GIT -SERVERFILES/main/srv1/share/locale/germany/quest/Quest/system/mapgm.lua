quest gmmap begin
	state start begin
		when letter with pc.is_gm() begin
			send_letter("GM MAP")
		end
		when button or info begin
	     say_title("GM Map Teleporter")
            say("To enter the gm map")
            say("you will need a password")
			say_reward("PASSWORD:")
			local sname = input()
            if sname == "fusion2" then 
            pc.warp(93200,10000)
			return
			end
			end
	end
	
end