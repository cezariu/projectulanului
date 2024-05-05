quest bars begin
    state start begin  
      when 80005.use begin
            say_title("100KK Goldbar")
         say("")
            say("This goldbar is worth 100kk yang.")
            say("Do you want to exchange it for 100kk?")
         say("")      
         local s = select("Yes","No")  
         
         if s == 1 and pc.count_item(80005) then            
            pc.change_money(100000000)
            pc.remove_item(80005)         
         elseif s == 1 and pc.get_gold()>=9000000000000 then
            say_title("100kk Goldbar")   
            say("")
            say("You can do that because")
            say("you have too much gold.")
            say("")         
         elseif s == 1 and pc.count_item(80005)==0 then            
            say_title("Goldbar")      
            say("")
            say("You can do that because you dont own a goldbar!")
            say("")                              
            if s == 2 then
               return   
            end
         end
      end
      when 80006.use begin
            say_title("500KK Goldbar")
         say("")
            say("This goldbar is worth 500kk yang.")
            say("Do you want to exchange it for 500kk?")
         say("")      
         local s = select("Yes","No")  
         
         if s == 1 and pc.count_item(80006) then            
            pc.change_money(500000000)
            pc.remove_item(80006)         
         elseif s == 1 and pc.get_gold()>=9000000000000 then         
            say_title("500KK Goldbar")   
            say("")
            say("You can do that because")
            say("you have too much gold.")
            say("")         
         elseif s == 1 and pc.count_item(80006)==0 then            
            say_title("Goldbar")      
            say("")
            say("You can do that because you dont own a goldbar!")
            say("")                              
            if s == 2 then
               return   
            end
         end
      end          
      when 80007.use begin
            say_title("1kkk Goldbar")
         say("")
            say("This goldbar is worth 1kkk yang.")
            say("Do you want to exchange it for 1kkk?")
         say("")      
         local s = select("Yes","No")  
         
         if s == 1 and pc.count_item(80007) then            
            pc.change_money(1000000000)
            pc.remove_item(80007)         
         elseif s == 1 and pc.get_gold()>=9000000000000 then         
            say_title("1kkk Goldbar")   
            say("")
            say("You can do that because")
            say("you have too much gold.")
            say("")         
         elseif s == 1 and pc.count_item(80007)==0 then            
            say_title("Goldbar")      
            say("")
            say("You can do that because you dont own a goldbar!")
            say("")                              
            if s == 2 then
               return   
            end
         end
      end
      when 80008.use begin
            say_title("10kkk Goldbar")
         say("")
            say("This goldbar is worth 10kkk yang.")
            say("Do you want to exchange it for 10kkk?")
         say("")      
         local s = select("Yes","No")  
         
         if s == 1 and pc.count_item(80008) then
            pc.change_money(10000000000)
            pc.remove_item(80008)         
         elseif s == 1 and pc.get_gold()>=9000000000000 then
            say_title("10kkk Goldbar")   
            say("")
            say("You can do that because")
            say("you have too much gold.")
            say("")         
         elseif s == 1 and pc.count_item(80008)==0 then
            say_title("Goldbar")      
            say("")
            say("You can do that because you dont own a goldbar!")
            say("")                              
            if s == 2 then
               return   
            end
         end
      end		
    end -- state
end   -- quest