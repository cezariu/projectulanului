quest baule_start begin
	state start begin
		when 60898.use begin
				pc.remove_item(60898, 1)
				pc.give_item2(40143,385)
				pc.give_item2(30006, 10)
				pc.give_item2(30047, 15)
				pc.give_item2(30015, 15)
				pc.give_item2(30050, 20)
				pc.give_item2(30165, 20)
				pc.give_item2(30166, 25)
				pc.give_item2(30167, 30)
				pc.give_item2(30168, 30)
				pc.give_item2(30251, 30)
				pc.give_item2(30252, 35)
				pc.give_item2(30002, 35)
				pc.give_item2(30003, 35)
				pc.give_item2(30004, 40)
				pc.give_item2(30005, 45)
		end
		when 61000.use begin
				pc.remove_item(61000, 1)
				pc.give_item2(61001,1)
				pc.give_item2(61002, 1)
				pc.give_item2(61003, 1)
		end
	end
end

