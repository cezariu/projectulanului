quest regenbogen begin
    state start begin
            when 50512.use  begin
                say_title("Rainbow Stone")
                say("This stone can make all of your")
                say("skills and passives PERFECT.")
               
                if pc.job ==0 then
                say("Choose your doctrine:")
				say_title("MAKE SURE YOU HAVE THE CORRECT SPECIALISATION")
				say_title("BEFORE CHOOSING OTHERWISE IT WONT WORK")
               
                local s=select("Corporal","Mental","Cancel")
               
                if s==1 then
                --Corp
                pc.set_skill_group(1)
                pc.set_skill_level(1 ,59)
                pc.set_skill_level(2 ,59)
                pc.set_skill_level(3 ,59)
                pc.set_skill_level(4 ,59)
                pc.set_skill_level(5 ,59)
                pc.set_skill_level(6 ,59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(236 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
               
                if s==2 then
                --Mental
                pc.set_skill_group(2)
                pc.set_skill_level(16 ,59)
                pc.set_skill_level(17 ,59)
                pc.set_skill_level(18 ,59)
                pc.set_skill_level(19 ,59)
                pc.set_skill_level(20 ,59)
                pc.set_skill_level(21 ,59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(240 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
				
				if s==3 then
				return
				end
               
                elseif pc.job ==1 then
                say("Choose your doctrine:.")
               
                local s=select("Blade","Archery","Cancel")
               
                if s==1 then
                --Lame
                pc.set_skill_group(3)
                pc.set_skill_level(31 ,59)
                pc.set_skill_level(32 ,59)
                pc.set_skill_level(33 ,59)
                pc.set_skill_level(34 ,59)
                pc.set_skill_level(35 ,59)
                pc.set_skill_level(36 ,59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(237 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
               
                if s==2 then
                --Arc
                pc.set_skill_group(4)
                pc.set_skill_level(46 ,59)
                pc.set_skill_level(47 ,59)
                pc.set_skill_level(48 ,59)
                pc.set_skill_level(49 ,59)
                pc.set_skill_level(50 ,59)
                pc.set_skill_level(51 ,59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(241 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
				
				if s==3 then
				return
				end				
               
                elseif pc.job ==2 then
                say("Choose your doctrine:.")
                local s=select("Magic","Weapons","Cancel")
               
                if s==1 then
                --Magie
                pc.set_skill_group(5)
                pc.set_skill_level(76 ,59)
                pc.set_skill_level(77 ,59)
                pc.set_skill_level(78 ,59)
                pc.set_skill_level(79 ,59)
                pc.set_skill_level(80 ,59)
                pc.set_skill_level(81, 59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(242 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
               
                if s==2 then
                --Arme
                pc.set_skill_group(6)
                pc.set_skill_level(61 ,59)
                pc.set_skill_level(62 ,59)
                pc.set_skill_level(63 ,59)
                pc.set_skill_level(64 ,59)
                pc.set_skill_level(65 ,59)
                pc.set_skill_level(66 ,59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(238 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
				
				if s==3 then
				return
				end				
               
                elseif pc.job ==3 then
                say("Choose your doctrine:.")
                local s=select("Vindecare","Dragon","Cancel")
               
                if s==1 then
                --Vindecare
                pc.set_skill_group(7)
                pc.set_skill_level(106 ,59)
                pc.set_skill_level(107 ,59)
                pc.set_skill_level(108 ,59)
                pc.set_skill_level(109 ,59)
                pc.set_skill_level(110 ,59)
                pc.set_skill_level(111 ,59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(243 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
               
                if s==2 then
                --Dragon
                pc.set_skill_group(8)
                pc.set_skill_level(91 ,59)
                pc.set_skill_level(92 ,59)
                pc.set_skill_level(93 ,59)
                pc.set_skill_level(94 ,59)
                pc.set_skill_level(95 ,59)
                pc.set_skill_level(96 ,59)
				pc.set_skill_level(221 ,59)
				pc.set_skill_level(222 ,59)
				pc.set_skill_level(223 ,59)
				pc.set_skill_level(224 ,59)
				pc.set_skill_level(225 ,59)
				pc.set_skill_level(226 ,59)
				pc.set_skill_level(227 ,59)
				pc.set_skill_level(228 ,59)
				pc.set_skill_level(239 ,59)
				pc.set_skill_level(143 ,59)
				pc.set_skill_level(144 ,59)
				pc.set_skill_level(145 ,59)
				pc.set_skill_level(146 ,59)
                say("All skills and passives are now PERFECT!")
                end
				
				if s==3 then
				return
				end
            end
        end
    end
end