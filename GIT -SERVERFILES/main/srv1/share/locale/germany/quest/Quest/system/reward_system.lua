quest reward_check begin
	state start begin
		when levelup with pc.get_level() == 120 and not pc.is_gm() begin
			--REWARD_120=3
			game.set_reward(3)
			end
		when levelup with pc.get_level() == 100 and not pc.is_gm() begin
			--REWARD_120=3
			game.set_reward(1)
			end
		when 2493.kill begin
			game.set_reward(8)
		end
		when 3965.kill begin
			game.set_reward(7)
		end
	end
end
