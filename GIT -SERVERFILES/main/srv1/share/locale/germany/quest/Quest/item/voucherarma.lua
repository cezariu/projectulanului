quest voucherarmaspirit begin
	state start begin
		when 40005.use begin
		say_title("Spirit Weapon Voucher:")
		say("")
		say("Pick a weapon:")
		say_reward("This is a SKIN !")
		say("")
		local premiu = select ("Spirit Sword", "Spirit Blade", "Spirit Daggers", "Spirit Bow", "Spirit Bell", "Spirit Fan", "I will decide later")
		if premiu == 1 then
			if pc.get_sex() == 0 then
				pc.give_item2(49021,1)
				pc.remove_item(40005, 1)
			elseif pc.get_sex() == 1 then
				pc.give_item2(49021,1)
				pc.remove_item(40005, 1)
			end
		elseif premiu == 2 then
			if pc.get_sex() == 0 then
				pc.give_item2(49024,1)
				pc.remove_item(40005, 1)
			elseif pc.get_sex() == 1 then
				pc.give_item2(49024,1)
				pc.remove_item(40005, 1)
			end
		elseif premiu == 3 then
			if pc.get_sex() == 0 then
				pc.give_item2(49022,1)
				pc.remove_item(40005, 1)
			elseif pc.get_sex() == 1 then
				pc.give_item2(49022,1)
				pc.remove_item(40005, 1)
			end
		elseif premiu == 4 then
			if pc.get_sex() == 0 then
				pc.give_item2(49023,1)
				pc.remove_item(40005, 1)
			elseif pc.get_sex() == 1 then
				pc.give_item2(49023,1)
				pc.remove_item(40005, 1)
			end
		elseif premiu == 5 then
			if pc.get_sex() == 0 then
				pc.give_item2(49025,1)
				pc.remove_item(40005, 1)
			elseif pc.get_sex() == 1 then
				pc.give_item2(49025,1)
				pc.remove_item(40005, 1)
			end
		elseif premiu == 6 then
			if pc.get_sex() == 0 then
				pc.give_item2(49026,1)
				pc.remove_item(40005, 1)
			elseif pc.get_sex() == 1 then
				pc.give_item2(49026,1)
				pc.remove_item(40005, 1)
			end
		end	
	end
end
end