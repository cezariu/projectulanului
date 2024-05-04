import uiscriptlocale

WINDOW_WIDTH = 184
WINDOW_HEIGHT = 328+32+35+30+20

window = {
	"name" : "ExtraInventory",

	"x" : (SCREEN_WIDTH - WINDOW_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - WINDOW_HEIGHT) / 2,

	"style" : ("movable", "float",),

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 184,
			"height" : 328+32+35+30+20,

			"children" :
			(
				# Separate Button (38x24)
				# {
					# "name" : "RefreshButton",
					# "type" : "button",
				
					# "x" : 8,
					# "y" : 7,
				
					# "tooltip_text" : uiscriptlocale.INVENTORY_SPECIAL_SEPARATE,
				
					# "default_image" : "d:/ymir work/ui/public/button_refresh_02.sub",
					# "over_image" : "d:/ymir work/ui/public/button_refresh_01.sub",
					# "down_image" : "d:/ymir work/ui/public/button_refresh_03.sub",
					# "disable_image" : "d:/ymir work/ui/public/button_refresh_03.sub",
				# },
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					#"x" : 8 +38,
					"x" : 6,
					"y" : 7,

					#"width" : WINDOW_WIDTH-15 - 38,
					"width" : WINDOW_WIDTH-15,
					"color" : "yellow",

					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : 0, "y" : -1, "text" : uiscriptlocale.EXTRA_INVENTORY_TITLE, "all_align" : "center" },
					),
				},
				{
					"name" : "boardv2",
					"type" : "border_a",
					"x" : 0,
					"y" : 120+295,
					"vertical_align" : "bottom",
					"horizontal_align" : "center",
					"width" : 166,
					"height" : 110+295,
				},
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 12,
					"y" : 34,

					"start_index" : 0,
					"x_count" : EXTRA_INVENTORY_PAGE_COLUMN,
					"y_count" : EXTRA_INVENTORY_PAGE_ROW,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				{
					"name":"cover_open_8",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 0)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_8",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 0)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_7",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 1)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_7",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 1)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_6",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 2)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_6",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 2)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_5",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 3)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_5",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 3)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_4",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 4)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_4",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 4)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_3",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 5)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_3",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 5)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_2",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 6)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_2",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 6)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_1",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 7)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_1",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 7)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				{
					"name":"cover_open_0",
					"type":"button",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 8)+ 137,

					"default_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"over_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
					"down_image":"d:/ymir work/ui/ex_inven_cover_button_open.sub",
				},
				{
					"name":"cover_close_0",
					"type":"image",
					"vertical_align":"bottom",
					
					"x":12,
					"y":18 + (32 * 8)+ 137,

					"image":"d:/ymir work/ui/ex_inven_cover_button_close.sub",
				},
				## Button1
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 12,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/bottone/button1.tga",
					"over_image" : "d:/ymir work/ui/game/windows/bottone/button2.tga",
					"down_image" : "d:/ymir work/ui/game/windows/bottone/button3.tga",

					"children" :
					(
						{
							"name" : "Text_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

					#		"text" : "I",
						},
					),
				},
				## Button2
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 12 + 40,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/bottone/button4.tga",
					"over_image" : "d:/ymir work/ui/game/windows/bottone/button5.tga",
					"down_image" : "d:/ymir work/ui/game/windows/bottone/button6.tga",

					"children" :
					(
						{
							"name" : "Text_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

					#		"text" : "II",
						},
					),
				},
				
				## Button3
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 12+80,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/bottone/button7.tga",
					"over_image" : "d:/ymir work/ui/game/windows/bottone/button8.tga",
					"down_image" : "d:/ymir work/ui/game/windows/bottone/button9.tga",

					"children" :
					(
						{
							"name" : "Text_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

					#		"text" : "III",
						},
					),
				},
				## Button4
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",

					"x" : 12 + 120,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/bottone/button10.tga",
					"over_image" : "d:/ymir work/ui/game/windows/bottone/button11.tga",
					"down_image" : "d:/ymir work/ui/game/windows/bottone/button12.tga",

					"children" :
					(
						{
							"name" : "Text_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

						#	"text" : "VI",
						},
					),
				},
				## CategoryButton1
				{
					"name" : "Cat_00",
					"type" : "radio_button",

					"x" : 12,
					"y" : 290+32+30,
					
					
					"tooltip_text" : uiscriptlocale.BOOKS_TITLE,

					"default_image" : "new/storage/skillbook_normal.tga",
					"over_image" : "new/storage/skillbook_hover.tga",
					"down_image" : "new/storage/skillbook_down.tga",
				},
				## CategoryButton2
				{
					"name" : "Cat_01",
					"type" : "radio_button",

					"x" : 12+40,
					"y" : 290+32+30,
					
					
					"tooltip_text" : uiscriptlocale.UPPGRADE_TITLE,

					"default_image" : "new/storage/upp_normal.tga",
					"over_image" : "new/storage/upp_hover.tga",
					"down_image" : "new/storage/upp_down.tga",					
				},
				## CategoryButton3
				{
					"name" : "Cat_02",
					"type" : "radio_button",

					"x" : 12+40+40,
					"y" : 290+32+30,
					
					
					"tooltip_text" : uiscriptlocale.STONES_TITLE,

					"default_image" : "new/storage/stone_normal.tga",
					"over_image" : "new/storage/stone_hover.tga",
					"down_image" : "new/storage/stone_down.tga",
				},
				## CategoryButton3
				{
					"name" : "Cat_03",
					"type" : "radio_button",

					"x" : 12+40+40+40,
					"y" : 290+32+30,
					
					
					"tooltip_text" : uiscriptlocale.COFFERS_TITLE,

					"default_image" : "new/storage/chest_normal.tga",
					"over_image" : "new/storage/chest_hover.tga",
					"down_image" : "new/storage/chest_down.tga",
				},
				## CategoryButton4
				{
					"name" : "Cat_04",
					"type" : "radio_button",

					"x" : 72,
					"y" : 290+32+30+40,
					
					
					"tooltip_text" : uiscriptlocale.ENCHANT_REINFORCE_TITLE,

					"default_image" : "new/storage/enchant_normal.tga",
					"over_image" : "new/storage/enchant_hover.tga",
					"down_image" : "new/storage/enchant_down.tga",
				},
				## CategoryButton 4 Safebox
				{
					"name" : "Safebox_cat",
					"type" : "button",

					"x" : 12 + 20,
					"y" : 290+32+30+40,
					
					
					"tooltip_text" : uiscriptlocale.SAFEBOX_TITLE,

					"default_image" : "new/storage/etc_normal.tga",
					"over_image" : "new/storage/etc_hover.tga",
					"down_image" : "new/storage/etc_down.tga",
				},
				
				# CategoryButton 5 Mall
				{
					"name" : "Mall_cat",
					"type" : "button",
					
					"x" : 112,
					"y" : 290+32+30+40,
					
					
					"tooltip_text" : uiscriptlocale.MALL_TITLE,

					"default_image" : "new/storage/itemshop_normal.tga",
					"over_image" : "new/storage/itemshop_hover.tga",
					"down_image" : "new/storage/itemshop_down.tga",
				},
			),	
		},
	),
}
