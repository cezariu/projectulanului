quest craft_new begin
	state start begin
		when 20377.chat."PvP Refinement" begin
			command("cube open")
			setskin(NOWINDOW)
		end
		
		when 20378.chat."PvM Refinement" begin
			command("cube open")
			setskin(NOWINDOW)
		end		

		when 20503.chat."Gem Creation" begin
			command("cube open")
			setskin(NOWINDOW)
		end
	end
end

