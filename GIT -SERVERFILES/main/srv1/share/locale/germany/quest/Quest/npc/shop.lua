quest shopuri begin
	state start begin
		when 9002.chat."Beginner armours" begin
			npc.open_shop(4)
			setskin(NOWINDOW)
		end
		when 9002.chat."Advanced armours" begin
			npc.open_shop(5)
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
		when 9001.chat."Beginner weapons" begin
			npc.open_shop(80)
			setskin(NOWINDOW)
		end
		when 9001.chat."Warrior - swords" begin
			npc.open_shop(81)
			setskin(NOWINDOW)
		end
		when 9001.chat."Warrior - 2 hands" begin
			npc.open_shop(82)
			setskin(NOWINDOW)
		end
		when 9001.chat."Ninja - daggers" begin
			npc.open_shop(83)
			setskin(NOWINDOW)
		end
		when 9001.chat."Ninja - bows" begin
			npc.open_shop(84)
			setskin(NOWINDOW)
		end
		when 9001.chat."Saman - fans" begin
			npc.open_shop(85)
			setskin(NOWINDOW)
		end
		when 9001.chat."Saman - bells" begin
			npc.open_shop(86)
			setskin(NOWINDOW)
		end
	end
end