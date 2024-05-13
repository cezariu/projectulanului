quest dragon_soul_refine begin
	state start begin
		when 20001.chat."Shop of the Refined" begin
			npc.open_shop(65)
			setskin(NOWINDOW)
		end
	end
end
