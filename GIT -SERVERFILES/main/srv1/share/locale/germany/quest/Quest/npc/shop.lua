quest shopuri begin
	state start begin
		when 9002.chat."Armors" begin
			npc.open_shop(4)
			setskin(NOWINDOW)
		end
		when 9002.chat."Accesories" begin
			npc.open_shop(0)
			setskin(NOWINDOW)
		end
		when 9003.chat."Sundries" begin
			npc.open_shop(3)
			setskin(NOWINDOW)
		end
		when 9003.chat."Consumables" begin
			npc.open_shop(64)
			setskin(NOWINDOW)
		end
		when 20381.chat."Weapons/Armors" begin
			npc.open_shop(59)
			setskin(NOWINDOW)
		end
		when 20381.chat."Effects" begin
			npc.open_shop(62)
			setskin(NOWINDOW)
		end
		when 20381.chat."BELTS" begin
			npc.open_shop(995)
			setskin(NOWINDOW)
		end	
		when 30129.chat."EASTER SHOP" begin
			npc.open_shop(1049)
			setskin(NOWINDOW)
		end
		when 20092.chat."Battlepass Shop" begin
			npc.open_shop(1050)
			setskin(NOWINDOW)
		end
		when 20093.chat."Battlepass Shop" begin
			npc.open_shop(1050)
			setskin(NOWINDOW)
		end
		when 20094.chat."Battlepass Shop" begin
			npc.open_shop(1050)
			setskin(NOWINDOW)
		end
		when 20095.chat."Battlepass Shop" begin
			npc.open_shop(1050)
			setskin(NOWINDOW)
		end	
		when 9013.chat."Shop" begin
			npc.open_shop(5)
			setskin(NOWINDOW)
		end			

	end
end