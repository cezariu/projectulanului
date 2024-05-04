import uiscriptlocale

ROOT = "d:/ymir work/ui/minimap/"

window = {
	"name" : "MiniMap",
	"x" : SCREEN_WIDTH - 148,
	"y" : 0,
	"width" : 148,
	"height" : 160,
	"children" :
	(
		{
			"name" : "OpenWindow",
			"type" : "window",
			"x" : 0,
			"y" : 0,
			"width" : 148,
			"height" : 160,
			"children" :
			(
				{
					"name" : "OpenWindowBGI",
					"type" : "image",
					"x" : 12,
					"y" : 13,
					"image" : ROOT + "minimap.sub",
				},
				{
					"name" : "MiniMapWindow",
					"type" : "window",
					"x" : 4,
					"y" : 5 + 13,
					"width" : 128,
					"height" : 128,
				},
				{
					"name" : "BUTTON_DUNGEON_INFO",
					"type" : "button",
					
					"x" : 16,
					"y" : 110,
					
					"tooltip_text" : "Dungeon Info",
					
					"default_image" : "new/dungeon_info_normal.png",
					"over_image" : "new/dungeon_info_hover.png",
					"down_image" : "new/dungeon_info_down.png",
				},
				{
					"name" : "AtlasShowButton",
					"type" : "button",
					"x" : 24,
					"y" : 25,
					"default_image" : ROOT + "atlas_open_default.sub",
					"over_image" : ROOT + "atlas_open_over.sub",
					"down_image" : ROOT + "atlas_open_down.sub",
				},
				{
					"name" : "BUTTON_DAILY",
					"type" : "button",
					"x" : 4,
					"y" : 45,
					# "default_image" : ROOT + "chest.png",
					# "over_image" : ROOT + "chest_over.png",
					# "down_image" : ROOT + "chest_down.png",
				},
				{
					"name" : "BUTTON_BIOLOGO",
					"type" : "button",
					"x" : 5,
					"y" : 82,
					
					"tooltip_text" : "Biolog",
					
					"default_image" : "new/btn_biolog_normal.png",
					"over_image" : "new/btn_biolog_hover.png",
					"down_image" : "new/btn_biolog_down.png",
				},
				{
					"name" : "BUTTON_PASS",
					"type" : "button",
					"x" : 7,
					"y" : 54,
					
					"tooltip_text" : "BattlePass",
					
					"default_image" : "new/btn_battlepass_normal.png",
					"over_image" : "new/btn_battlepass_hover.png",
					"down_image" : "new/btn_battlepass_down.png",
				},
				{
					"name" : "BUTTON_WIKI_WONDER",
					"type" : "button",
					"x" : 67,
					"y" : 138,
					
					"tooltip_text" : "Wiki",
					
					"default_image" : "d:/ymir work/ui/wiki_btn_01.png",
					"over_image" : "d:/ymir work/ui/wiki_btn_02.png",
					"down_image" :"d:/ymir work/ui/wiki_btn_03.png",
				},
				{
					"name" : "ScaleUpButton",
					"type" : "button",
					"x" : 113,
					"y" : 129,
					"default_image" : ROOT + "minimap_scaleup_default.sub",
					"over_image" : ROOT + "minimap_scaleup_over.sub",
					"down_image" : ROOT + "minimap_scaleup_down.sub",
				},
				{
					"name" : "ScaleDownButton",
					"type" : "button",
					"x" : 127,
					"y" : 116,
					"default_image" : ROOT + "minimap_scaledown_default.sub",
					"over_image" : ROOT + "minimap_scaledown_over.sub",
					"down_image" : ROOT + "minimap_scaledown_down.sub",
				},
				{
					"name" : "MiniMapHideButton",
					"type" : "button",
					"x" : 123,
					"y" : 19,
					"default_image" : ROOT + "minimap_close_default.sub",
					"over_image" : ROOT + "minimap_close_over.sub",
					"down_image" : ROOT + "minimap_close_down.sub",
				},
				{
					"name" : "textInfoBar2",
					"type" : "bar",
					"x" : 8,
					"y" : 163 + 3,
					"color" : 0x00000000,
					"width" : 132,
					"height" : 28,
					"children" : 
					(
						{
							"name" : "ServerInfo",
							"type" : "text",
							"x" : 0,
							"y" : 1,
							"text" : "",
							"outline" : 1,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center"
						},
						{
							"name" : "MiniMapClock",
							"type" : "text",
							"x" : 0,
							"y" : 12,
							"text" : "",
							"outline" : 1,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center"
						},
						{
							"name" : "TimeInfo",
							"type" : "text",
							"x" : 0,
							"y" : 12,
							"text" : "",
							"outline" : 1,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center"
						},
						{
							"name" : "RenderInfo",
							"type" : "text",
						
							"text_horizontal_align" : "center",	

							"outline" : 1,

							"x" : 70,
							"y" : 25,

							"text" : "",
						},						
					),
				},
				{
					"name" : "ObserverCount",
					"type" : "text",
					"text_horizontal_align" : "center",
					"outline" : 1,
					"x" : 82,
					"y" : 213,
					"text" : "",
				},
			),
		},
		{
			"name" : "CloseWindow",
			"type" : "window",
			"x" : 10,
			"y" : 0,
			"width" : 132,
			"height" : 48,
			"children" :
			(
				{
					"name" : "MiniMapShowButton",
					"type" : "button",

					"x" : 100,
					"y" : 4,

					"default_image" : ROOT + "minimap_open_default.sub",
					"over_image" : ROOT + "minimap_open_default.sub",
					"down_image" : ROOT + "minimap_open_default.sub",
				},
			),
		},
		{
			"name" : "MastWindow",
			"type" : "thinboard",

			"x" : -18,
			"y" : 215,

			"width" : 165,
			"height" : 66,
			"children" :
			(
				{
					"name" : "MastText",
					"type" : "text",

					"text_horizontal_align" : "center",

					"x" : 85,
					"y" : 8,

					"text" : uiscriptlocale.DEFANCE_WAWE_MAST_TEXT,
				},
				{
					"name" : "MastHp",
					"type" : "gauge",

					"x" : 42,
					"y" : 23,

					"width" : 85,
					"color" : "red",
							
					"tooltip_text" : uiscriptlocale.DEFANCE_WAWE_GAUGE_TOOLTIP,
				},
				{
					"name" : "ActualMastText",
					"type" : "text",

					"text_horizontal_align" : "center",

					"x" : 84,
					"y" : 31,

					"text" : uiscriptlocale.MASK_HP_DEFAULT,
				},
				{
					"name" : "MastTimerText",
					"type" : "text",

					"text_horizontal_align" : "center",

					"x" : 85,
					"y" : 42,

					"text" : "-:-",
				},
			),
		},
	),
}

