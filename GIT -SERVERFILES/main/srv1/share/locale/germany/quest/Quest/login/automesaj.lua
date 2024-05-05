quest automesaj begin 
state start begin 
when login begin 
timer("timer1", 601) 
end 

when timer1.timer begin 
timer("timer2", 721) 
notice("Players with [H] included in the name are called HELPERS")
notice("They can answer server related questions.")
end 

when timer2.timer begin 
timer("timer3", 901) 
notice("Join our Discord server for all the updates")
notice("and all types of support: https://discord.gg/Tf5UY2zAD9")
end 

when timer3.timer begin 
notice("Premium Battlepass can be purchased from the itemshop.")
notice("Contains new rewards and new extra missions(easier).")
end 
end 
end