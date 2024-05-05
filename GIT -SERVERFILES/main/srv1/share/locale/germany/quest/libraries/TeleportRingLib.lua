--[[
-- Init - The Teleport Ring Class
]]

TeleportRing = {};

TeleportRing.ReturnData = function()
	if (TeleportRing.data == nil) then
		TeleportRing.data = {
			{
				["TeleportMapName"] = "Map1",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Jinno", ["x"] = 963100, ["y"] = 276000},
					{["OtherIndexName"] = "Chunjo", ["x"] = 63200, ["y"] = 166700},
					{["OtherIndexName"] = "Shinsoo", ["x"] = 473900, ["y"] = 954600}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Map2",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Jinno", ["x"] = 863800, ["y"] = 246000},
					{["OtherIndexName"] = "Chunjo", ["x"] = 145700, ["y"] = 239800},
					{["OtherIndexName"] = "Shinsoo", ["x"] = 352300, ["y"] = 882700}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Seungryong Valley",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Middle", ["x"] = 332700, ["y"] = 746300},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 280400, ["y"] = 795200},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 344000, ["y"] = 703600},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 294900, ["y"] = 715700},
					{["OtherIndexName"] = "Metin Zone 4", ["x"] = 298700, ["y"] = 773400}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},			
			{
				["TeleportMapName"] = "Desert",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Middle", ["x"] = 296300, ["y"] = 547500},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 242700, ["y"] = 516800},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 340900, ["y"] = 537000},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 337500, ["y"] = 595900}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Sohan",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Middle", ["x"] = 436100, ["y"] = 215100},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 379100, ["y"] = 258000},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 481300, ["y"] = 229500},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 492100, ["y"] = 257400}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Demon Tower - Devil's Catacombs",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Demon Tower", ["x"] = 590400, ["y"] = 110500},
					{["OtherIndexName"] = "Devil's Catacombs", ["x"] = 591900, ["y"] = 100200}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Fire Land",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Middle", ["x"] = 599300, ["y"] = 707200},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 663900, ["y"] = 631600},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 650300, ["y"] = 752600},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 683300, ["y"] = 694800}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Giants Land",
				["TeleportHasOtherIndexs"] = false,
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false,
				["x"] = 828100,
				["y"] = 763400
			},
			{
				["TeleportMapName"] = "V3",
				["TeleportHasOtherIndexs"] = false,
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {75, 120},
				["TeleportItemCheck"] = false,
				["TeleportItems"] = {30190, 1},
				["x"] = 145300,
				["y"] = 1323600
			},
			{
				["TeleportMapName"] = "V4",
				["TeleportHasOtherIndexs"] = false,
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {75, 120},
				["TeleportItemCheck"] = false,
				["TeleportItems"] = {30190, 1},
				["x"] = 153600,
				["y"] = 1203200
			},
			{
				["TeleportMapName"] = "Ghost Forest",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Start", ["x"] = 290400, ["y"] = 5500},
					{["OtherIndexName"] = "Middle", ["x"] = 302500, ["y"] = 25900},
					{["OtherIndexName"] = "End", ["x"] = 289000, ["y"] = 41900}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Red Forest",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Start", ["x"] = 1119900, ["y"] = 69200},
					{["OtherIndexName"] = "End", ["x"] = 1120200, ["y"] = 7100},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 1060000, ["y"] = 63400},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 1061800, ["y"] = 24600},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 1099400, ["y"] = 23200}},
				["TeleportLevelCheck"] = false,
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Spider Dungeon(1-3)", -- Teleport Map Name
				["TeleportHasOtherIndexs"] = true, -- true = citeste "TeleportTheOtherIndexes" de mai jos, adica cand dai click iti arata si alte optiuni de teleportare / false = opusul.
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Spider Dungeon 1", ["x"] = 51200, ["y"] = 486400},
					{["OtherIndexName"] = "Spider Dungeon 2", ["x"] = 665600, ["y"] = 435200},					-- Optiunile de teleportare ale Mapei de mai sus (Pot fi adaugate oricate)
					{["OtherIndexName"] = "Spider Dungeon 3", ["x"] = 97600, ["y"] = 571100}},
				["TeleportLevelCheck"] = true, -- true = iti citeste limitele de nivel adaugate mai jos / false = opusul.
				["TeleportLevel"] = {35, 120}, -- nivel minim / nivel maxim (delimiteaza nivelele la care te poti teleporta in mapa respectiva)
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Cape Dragon Fire",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Start", ["x"] = 1085300, ["y"] = 1783300},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 1161300, ["y"] = 1790200},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 1156700, ["y"] = 1688300},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 1047900, ["y"] = 1739800},
					{["OtherIndexName"] = "Metin Zone 4", ["x"] = 1050900, ["y"] = 1692000}},
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {90, 120},
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Nephrite Bay",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Start", ["x"] = 1087400, ["y"] = 1646000},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 1107000, ["y"] = 1525200},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 1089700, ["y"] = 1615500},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 1070800, ["y"] = 1569600},
					{["OtherIndexName"] = "Metin Zone 4", ["x"] = 1062200, ["y"] = 1634600}},
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {90, 120},
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Thunder Mountains",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Start", ["x"] = 1134700, ["y"] = 1653900},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 1143200, ["y"] = 1535900},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 1146400, ["y"] = 1597500},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 1210800, ["y"] = 1639200},
					{["OtherIndexName"] = "Metin Zone 4", ["x"] = 1213700, ["y"] = 1523900}},
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {90, 120},
				["TeleportItemCheck"] = false
			},
			{
				["TeleportMapName"] = "Guatama Cliff",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Start", ["x"] = 1225700, ["y"] = 1682000},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 1194200, ["y"] = 1681000},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 1215800, ["y"] = 1742600},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 1277600, ["y"] = 1745500},
					{["OtherIndexName"] = "Metin Zone 4", ["x"] = 1320600, ["y"] = 1691600}},
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {90, 120},
				["TeleportItemCheck"] = false
			},			
			{
				["TeleportMapName"] = "Enchanted Forest 95-120",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Start", ["x"] = 813300, ["y"] = 1503200},
					{["OtherIndexName"] = "Metin Zone 1", ["x"] = 785500, ["y"] = 1471700},
					{["OtherIndexName"] = "Metin Zone 2", ["x"] = 824800, ["y"] = 1464300},
					{["OtherIndexName"] = "Metin Zone 3", ["x"] = 805100, ["y"] = 1420400}},
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {95, 120},
				["TeleportItemCheck"] = false,
				["TeleportItems"] = {30190, 1}
			},
			{
				["TeleportMapName"] = "PvP Map - Level: 85-120",
				["TeleportHasOtherIndexs"] = true,
				["TeleportTheOtherIndexes"] = {
					{["OtherIndexName"] = "Middle", ["x"] = 38400, ["y"] = 63900},
					{["OtherIndexName"] = "Up", ["x"] = 46900, ["y"] = 45400},
					{["OtherIndexName"] = "Left", ["x"] = 20800, ["y"] = 55700},
					{["OtherIndexName"] = "Down", ["x"] = 45200, ["y"] = 83400}},
				["TeleportLevelCheck"] = true,
				["TeleportLevel"] = {85, 120},
				["TeleportItemCheck"] = false
			},
		};
	end -- if
	
	return TeleportRing.data;
end -- func

TeleportRing.TeleportIsLevelCheck = function(index)
	local data = TeleportRing.ReturnData();
	
	return data[index]["TeleportLevelCheck"];
end -- func

TeleportRing.TeleportIsItemsCheck = function(index)
	local data = TeleportRing.ReturnData();
	
	return data[index]["TeleportItemCheck"];
end -- func

TeleportRing.TeleportMapHasOtherIndex = function(index)
	local data = TeleportRing.ReturnData();
	
	return data[index]["TeleportHasOtherIndexs"];
end -- func

TeleportRing.InsertWindow = function()
	local data = TeleportRing.ReturnData(); local window = {};
	
	for index in data do table.insert(window, data[index]["TeleportMapName"]); end -- for
	table.insert(window, "Renunta");
	
	return window;
end -- func

TeleportRing.DisplayOtherIndexWindow = function(WinIndex)
	local data = TeleportRing.ReturnData(); local OtherWindow = {};
	
	for index in data[WinIndex]["TeleportTheOtherIndexes"] do table.insert(OtherWindow, data[WinIndex]["TeleportTheOtherIndexes"][index]["OtherIndexName"]); end -- for
	table.insert(OtherWindow, "Renunta");
	
	return OtherWindow;
end -- func

TeleportRing.isBetweenLevel = function(index)
	local data = TeleportRing.ReturnData(); local pLevel = pc.get_level();
	
	return pLevel >= data[index]["TeleportLevel"][1] and pLevel <= data[index]["TeleportLevel"][2];
end -- func

TeleportRing.hasItemNeeded = function(index)
	local data = TeleportRing.ReturnData();
	
	return pc.count_item(data[index]["TeleportItems"][1]) >= data[index]["TeleportItems"][2];
end -- func

-- The main data window of the ring

TeleportRing.MainWindow = function(iVnum)
	local data = TeleportRing.ReturnData(); local InsertedWindowTable = TeleportRing.InsertWindow();
	
	say_title(string.format("%s:", item_name(iVnum)))
	local FirstWindow = select_table(InsertedWindowTable);
	if (FirstWindow == table.getn(InsertedWindowTable)) then
		return false;
	else
		say_title(string.format("%s:", item_name(iVnum)))
		if TeleportRing.TeleportIsLevelCheck(FirstWindow) then
			if (not TeleportRing.isBetweenLevel(FirstWindow)) then
				say(string.format("Nivelul tau trebuie sa fie intre %d si %d pentru[ENTER]a putea intra in aceasta mapa.", data[FirstWindow]["TeleportLevel"][1], data[FirstWindow]["TeleportLevel"][2]))
				return false;
			end -- if
		end -- if
		
		if TeleportRing.TeleportIsItemsCheck(FirstWindow) then
			if (not TeleportRing.hasItemNeeded(FirstWindow)) then
				say(string.format("Trebuie sa deti x%d - %s pentru[ENTER]a putea intra in aceasta mapa.", data[FirstWindow]["TeleportItems"][2], item_name(data[FirstWindow]["TeleportItems"][1])))
				return false;
			end -- if
		end -- if
		
		if TeleportRing.TeleportMapHasOtherIndex(FirstWindow) then
			local OtherInsertedWindowTable = TeleportRing.DisplayOtherIndexWindow(FirstWindow);
			
			local otherWind = select_table(OtherInsertedWindowTable);
			if (otherWind == table.getn(OtherInsertedWindowTable)) then
				return false;
			else
				if (not pc.can_warp()) then say("Asteapta 10 secunde pentru a te putea teleporta.") return false; end -- if
				
				if data[FirstWindow]["TeleportItemCheck"] then
					pc.remove_item(data[FirstWindow]["TeleportItems"][1], data[FirstWindow]["TeleportItems"][2]);
				end -- if
				return pc.warp(data[FirstWindow]["TeleportTheOtherIndexes"][otherWind]["x"], data[FirstWindow]["TeleportTheOtherIndexes"][otherWind]["y"]);
			end -- if
		end -- if
		
		if (not pc.can_warp()) then say("Asteapta 10 secunde pentru a te putea teleporta.") return false; end -- if
		if data[FirstWindow]["TeleportItemCheck"] then
			pc.remove_item(data[FirstWindow]["TeleportItems"][1], data[FirstWindow]["TeleportItems"][2]);
		end -- if
		return pc.warp(data[FirstWindow]["x"], data[FirstWindow]["y"]);
	end -- if
end -- func