import uiscriptlocale

BUTTONS_COUNT = 4
BOARD_WIDTH = 37
BOARD_HEIGHT = (38 * BUTTONS_COUNT)

window = {
	"name" : "InventoryMenuWindow",
	"x" : 0,
	"y" : 0,
	"style" : ("movable", "float",),
	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,
	"children" :
	(
		{
			"name" : "board",
			"type" : "bar",
			"x" : 0,
			"y" : 0,
			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			"color" : 0x00000000,
			"children" : 
			(
				{
					"name" : "button1",
					"type" : "button",
					"x" : 5,
					"y" : 0,
					"tooltip_text" : uiscriptlocale.EXTRA_INVENTORY,
					"tooltip_x" : -70,
					"tooltip_y" : 10,
					"default_image" : "new/storage_normal.png",
					"over_image" : "new/storage_hover.png",
					"down_image" : "new/storage_down.png",
				},	
				{
					"name" : "button2",
					"type" : "button",
					"x" : 5,
					"y" : BOARD_WIDTH,
					"tooltip_text" : uiscriptlocale.SWITCH_BOT,
					"tooltip_x" : -59,
					"tooltip_y" : 10,
					"default_image" : "new/switch_normal.png",
					"over_image" : "new/switch_hover.png",
					"down_image" : "new/switch_down.png",
				},
				{
					"name" : "button3",
					"type" : "button",
					"x" : 5,
					"y" : (BOARD_WIDTH * 2),
					"tooltip_text" : uiscriptlocale.CLASSIFICA_GILDA,
					"tooltip_x" : -67,
					"tooltip_y" : 10,
					"default_image" : "new/breasla_normal.png",
					"over_image" : "new/breasla_hover.png",
					"down_image" : "new/breasla_down.png",
				},
				{
					"name" : "button4",
					"type" : "button",
					"x" : 5,
					"y" : (BOARD_WIDTH * 3),
					"tooltip_text" : "Reward System",
					"tooltip_x" : -67,
					"tooltip_y" : 10,
					"default_image" : "new/pass_normal.png",
					"over_image" : "new/pass_hover.png",
					"down_image" : "new/pass_down.png",
				},
				{
					"name" : "button5",
					"type" : "button",
					"x" : 5,
					"y" : (BOARD_WIDTH * 4),
					"tooltip_text" : "Rune System",
					"tooltip_x" : -67,
					"tooltip_y" : 10,
					"default_image" : "new/rune_normal.png",
					"over_image" : "new/rune_hover.png",
					"down_image" : "new/rune_down.png",
				}				
			),
		},
	),
}
