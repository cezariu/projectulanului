import uiscriptlocale

IMG_DIR = "d:/ymir work/ui/game/gameoption/"

TITLE_IMAGE_TEXT_X = 5
TITLE_IMAGE_TEXT_Y = 4
ROOT_PATH = "d:/ymir work/ui/public/"

OPTION_START_X = 17
SLIDER_POSITION_X = 50

SLIDER_START_Y = 40
BUTTON_START_Y = 33
BUTTON_NEXT_Y = 20

RADIO_BUTTON_RANGE_X = 65
TOGGLE_BUTTON_RANGE_X = 65

RADIO_BUTTON_TEXT_X = 25
TOGGLE_BUTTON_TEXT_X = 20

SMALL_OPTION_HEIGHT = 65
NORMAL_OPTION_HEIGHT = 80
SLIDER_OPTION_HEIGHT = 65

window = {
	"name" : "GameOptionDialog",
	# Dont touch these lines!
	"style" : (),
	"x" : 171,
	"y" : 3,
	"width" : 300,
	"height" : 324,
	# Dont touch these lines!
	"children" :
	(
		{
			"name" : "show_name_window",
			"type" : "window",
			"x" : 0,
			"y" : 0,
			"width":304,
			"height":SMALL_OPTION_HEIGHT,
			"children":
			(
				{
					"name" : "show_name_title_img",
					"type" : "expanded_image",
					"x" : 0,
					"y" : 0,
					"image" : IMG_DIR+"option_title.tga",
					"children":
					(
						{
							"name" : "title_show_name",
							"type" : "text",
							"x" : TITLE_IMAGE_TEXT_X,
							"y" : TITLE_IMAGE_TEXT_Y,
							"text_horizontal_align":"left",
							"text" : uiscriptlocale.OPTION_ALWAYS_SHOW_NAME,
						},
					),
				},
				{
					"name" : "always_show_name_on_button",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : 33,
					"text" : uiscriptlocale.OPTION_ALWAYS_SHOW_NAME_ON,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},

				{
					"name" : "always_show_name_off_button",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*1,
					"y" : 33,
					"text" : uiscriptlocale.OPTION_ALWAYS_SHOW_NAME_OFF,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
			),
		},
		{
			"name" : "dogmode_window",
			"type" : "window",
			"x" : 0,
			"y" : SMALL_OPTION_HEIGHT,
			"width":304,
			"height":SMALL_OPTION_HEIGHT,
			"children":
			(
				{
					"name" : "dogmode_title_img",
					"type" : "expanded_image",
					"x" : 0,
					"y" : 0,
					"image" : IMG_DIR+"option_title.tga",
					"children":
					(
						{
							"name" : "title_dogmode",
							"type" : "text",
							"x" : TITLE_IMAGE_TEXT_X,
							"y" : TITLE_IMAGE_TEXT_Y,
							"text_horizontal_align":"left",
							"text" : uiscriptlocale.DOGMODE,
						},
					),
				},
				{
					"name" : "dog_mode_0",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : 33,
					"text" : uiscriptlocale.AUTO_ON,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},

				{
					"name" : "dog_mode_1",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*1,
					"y" : 33,
					"text" : uiscriptlocale.AUTO_OFF,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
			),
		},
		{
			"name" : "hide_window",
			"type" : "window",
			"x" : 0,
			"y" : SMALL_OPTION_HEIGHT*2,
			"width":304,
			"height":SMALL_OPTION_HEIGHT+(33*6),
			"children":
			(
				{
					"name" : "hide_title_img",
					"type" : "expanded_image",
					"x" : 0,
					"y" : 0,
					"image" : IMG_DIR+"option_title.tga",
					"children":
					(
						{
							"name" : "title_hide",
							"type" : "text",
							"x" : TITLE_IMAGE_TEXT_X,
							"y" : TITLE_IMAGE_TEXT_Y,
							"text_horizontal_align":"left",
							"text" : uiscriptlocale.HIDE_OPTION,
						},
					),
				},
				{
					"name" : "hidemode_0",
					"type" : "toggle_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : 33,
					"text" : uiscriptlocale.HIDE_OPTION0,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "hidemode_1",
					"type" : "toggle_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*1,
					"y" : 33,
					"text" : uiscriptlocale.HIDE_OPTION1,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "hidemode_2",
					"type" : "toggle_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*2+(5),
					"y" : 33,
					"text" : uiscriptlocale.HIDE_OPTION2,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "hidemode_3",
					"type" : "toggle_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : (33*2),
					"text" : uiscriptlocale.HIDE_OPTION3,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "hidemode_4",
					"type" : "toggle_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*1,
					"y" : (33*2),
					"text" : uiscriptlocale.HIDE_OPTION4,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "hidemode_5",
					"type" : "toggle_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*2+(5),
					"y" : (33*2),
					"text" : uiscriptlocale.HIDE_OPTION5,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "hidemode_6",
					"type" : "toggle_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : (33*3),
					"text" : uiscriptlocale.GRAPHICONOFF_EFFECT_LEVEL,
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "fps_title_img",
					"type" : "expanded_image",
					"x" : 0,
					"y" : 33*4,
					"image" : IMG_DIR+"option_title.tga",
					"children":
					(
						{
							"name" : "title_fps",
							"type" : "text",
							"x" : TITLE_IMAGE_TEXT_X,
							"y" : TITLE_IMAGE_TEXT_Y,
							"text_horizontal_align":"left",
							"text" : uiscriptlocale.AEON_PERFORMANCE,
						},
					),
				},
				{
					"name" : "fpsmode_0",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : 33*5,
					"text" : "30 FPS",
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "fpsmode_1",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*1,
					"y" : 33*5,
					"text" : "60 FPS",
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "fpsmode_2",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*2+(5),
					"y" : 33*5,
					"text" : "90 FPS",
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "fpsmode_3",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : (33*6),
					"text" : "120 FPS",
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "fpsmode_4",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*1,
					"y" : (33*6),
					"text" : "150 FPS",
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "fpsmode_5",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*2+(5),
					"y" : (33*6),
					"text" : "180 FPS",
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
				{
					"name" : "fpsmode_6",
					"type" : "radio_button",
					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
					"y" : (33*7),
					"text" : "220 FPS",
					"text_x" : RADIO_BUTTON_TEXT_X,
					"default_image" : IMG_DIR + "radio_unselected.tga",
					"over_image" : IMG_DIR + "radio_unselected.tga",
					"down_image" : IMG_DIR + "radio_selected.tga",
				},
			),
		},
#		{
#			"name" : "hide2_window",
#			"type" : "window",
#			"x" : 0,
#			"y" : SMALL_OPTION_HEIGHT*2+(33*3),
#			"width":304,
#			"height":SMALL_OPTION_HEIGHT+(33*2),
#			"children":
#			(
#				{
#					"name" : "hide2_title_img",
#					"type" : "expanded_image",
#					"x" : 0,
#					"y" : 0,
#					"image" : IMG_DIR+"option_title.tga",
#					"children":
#					(
#						{
#							"name" : "title_hide2",
#							"type" : "text",
#							"x" : TITLE_IMAGE_TEXT_X,
#							"y" : TITLE_IMAGE_TEXT_Y,
#							"text_horizontal_align":"left",
#							"text" : uiscriptlocale.HIDE_2_OPTION,
#						},
#					),
#				},
#				{
#					"name" : "hide2mode_0",
#					"type" : "toggle_button",
#					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
#					"y" : 33,
#					"text" : uiscriptlocale.HIDE_2_OPTION0,
#					"text_x" : RADIO_BUTTON_TEXT_X,
#					"default_image" : IMG_DIR + "radio_unselected.tga",
#					"over_image" : IMG_DIR + "radio_unselected.tga",
#					"down_image" : IMG_DIR + "radio_selected.tga",
#				},
#				{
#					"name" : "hide2mode_1",
#					"type" : "toggle_button",
#					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*2,
#					"y" : 33,
#					"text" : uiscriptlocale.HIDE_2_OPTION2,
#					"text_x" : RADIO_BUTTON_TEXT_X,
#					"default_image" : IMG_DIR + "radio_unselected.tga",
#					"over_image" : IMG_DIR + "radio_unselected.tga",
#					"down_image" : IMG_DIR + "radio_selected.tga",
#				},
#				{
#					"name" : "hide2mode_2",
#					"type" : "toggle_button",
#					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*0,
#					"y" : (33*2),
#					"text" : uiscriptlocale.HIDE_2_OPTION1,
#					"text_x" : RADIO_BUTTON_TEXT_X,
#					"default_image" : IMG_DIR + "radio_unselected.tga",
#					"over_image" : IMG_DIR + "radio_unselected.tga",
#					"down_image" : IMG_DIR + "radio_selected.tga",
#				},
#				{
#					"name" : "hide2mode_3",
#					"type" : "toggle_button",
#					"x" : OPTION_START_X+RADIO_BUTTON_RANGE_X*2,
#					"y" : (33*2),
#					"text" : uiscriptlocale.HIDE_2_OPTION3,
#					"text_x" : RADIO_BUTTON_TEXT_X,
#					"default_image" : IMG_DIR + "radio_unselected.tga",
#					"over_image" : IMG_DIR + "radio_unselected.tga",
#					"down_image" : IMG_DIR + "radio_selected.tga",
#				},
#			),
#		},
	),
}
