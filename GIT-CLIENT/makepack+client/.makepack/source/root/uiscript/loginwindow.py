import localeinfo

ROOT = "grafica/login/"
LOCALE_PATH = "grafica/login/"

ID_LIMIT_COUNT = 30
PW_LIMIT_COUNT = 30
MIDDLE_WIDTH = SCREEN_WIDTH / 2
MIDLLE_HEIGHT = SCREEN_HEIGHT / 2

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		{
			"name" : "bg1", "type" : "ani_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"delay": 1,
			"images" : (
				LOCALE_PATH + "bg/1.tga",

				),
		},
		
		{
			"name" : "logo", "type" : "expanded_image", "x" : 490, "y" : 40,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : LOCALE_PATH + "logo.png",
		},

		{
			"name" : "SaveBoard",
			"type" : "image",


			"x" : (SCREEN_WIDTH - 27) / 2,
			"y" : (SCREEN_HEIGHT - 300) / 2,
			

			"image" : LOCALE_PATH + "fereastra_fundal2.png",

			"children" :
			(

				{
					"name" : "loadacc_btn1",
					"type" : "button",

					"x" : 19,
					"y" : 73,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt1",
					"type" : "text",
					"x" : 19+6,
					"y" : 73+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn2",
					"type" : "button",

					"x" : 19,
					"y" : 111,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt2",
					"type" : "text",
					"x" : 19 +6,
					"y" : 111+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn3",
					"type" : "button",

					"x" : 19,
					"y" : 149,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt3",
					"type" : "text",
					"x" : 19 +6,
					"y" : 149+7,

					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn4",
					"type" : "button",

					"x" : 19,
					"y" : 187,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt4",
					"type" : "text",
					"x" : 19 +6,
					"y" : 187+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn5",
					"type" : "button",

					"x" : 19,
					"y" : 225,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt5",
					"type" : "text",
					"x" : 19 +6,
					"y" : 225+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn6",
					"type" : "button",

					"x" : 19,
					"y" : 263,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt6",
					"type" : "text",
					"x" : 19 +6,
					"y" : 263+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn7",
					"type" : "button",

					"x" : 19,
					"y" : 301,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt7",
					"type" : "text",
					"x" : 19 +6,
					"y" : 301+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn8",
					"type" : "button",

					"x" : 162,
					"y" : 73,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt8",
					"type" : "text",
					"x" : 162+6,
					"y" : 73 +7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn9",
					"type" : "button",

					"x" : 162,
					"y" : 111,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt9",
					"type" : "text",
					"x" : 162+6,
					"y" : 111+7,

					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn10",
					"type" : "button",

					"x" : 162,
					"y" : 149,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt10",
					"type" : "text",
					"x" : 162+6,
					"y" : 149+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn11",
					"type" : "button",

					"x" : 162,
					"y" : 187,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt11",
					"type" : "text",
					"x" : 162+6,
					"y" : 187+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn12",
					"type" : "button",

					"x" : 162,
					"y" : 225,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt12",
					"type" : "text",
					"x" : 162+6,
					"y" : 225+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn13",
					"type" : "button",

					"x" : 162,
					"y" : 263,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt13",
					"type" : "text",
					"x" : 162+6,
					"y" : 263+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},

				{
					"name" : "loadacc_btn14",
					"type" : "button",

					"x" : 162,
					"y" : 301,

					"default_image" : LOCALE_PATH + "save_account.png",
					"over_image" : LOCALE_PATH + "save_account_over.png",
					"down_image" : LOCALE_PATH + "save_account_down.png",
				},
				{
					"name" : "save_txt14",
					"type" : "text",
					"x" : 162+6,
					"y" : 301+7,
					"text" : localeinfo.EMPTY_SLOT,
					"color" : 0xFF544D43,
				},
				
				
				{
					"name" : "deleteacc_btn1",
					"type" : "button",

					"x" : 132,
					"y" : 82,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn2",
					"type" : "button",

					"x" : 132,
					"y" : 120,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn3",
					"type" : "button",

					"x" : 132,
					"y" : 158,

					"default_image" : LOCALE_PATH + "delete_account.png",
					# "over_image" : LOCALE_PATH + "delete_account_over.png",
					# "down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn4",
					"type" : "button",

					"x" : 132,
					"y" : 196,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn5",
					"type" : "button",

					"x" : 132,
					"y" : 234,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn6",
					"type" : "button",

					"x" : 132,
					"y" : 272,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				
				{
					"name" : "deleteacc_btn7",
					"type" : "button",

					"x" : 132,
					"y" : 310,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn8",
					"type" : "button",

					"x" : 276,
					"y" : 82,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn9",
					"type" : "button",

					"x" : 276,
					"y" : 120,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn10",
					"type" : "button",

					"x" : 276,
					"y" : 158,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn11",
					"type" : "button",

					"x" : 276,
					"y" : 196,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn12",
					"type" : "button",

					"x" : 276,
					"y" : 234,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn13",
					"type" : "button",

					"x" : 276,
					"y" : 272,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
				
				{
					"name" : "deleteacc_btn14",
					"type" : "button",

					"x" : 276,
					"y" : 310,

					"default_image" : LOCALE_PATH + "delete_account.png",
					"over_image" : LOCALE_PATH + "delete_account_over.png",
					"down_image" : LOCALE_PATH + "delete_account_down.png",
				},
			),
		},
		{
			"name" : "LinkButton",

			"x" : (SCREEN_WIDTH - 27) / 2,
			"y" : (SCREEN_HEIGHT - 300) / 2,
			

			"width" : 312,
			"height" : 53,

			"children" :
			(

				{
					"name" : "facebook_btn",
					"type" : "button",

					"x" : 15+10,
					"y" : 11,

				#	"default_image" : LOCALE_PATH + "button/fb.png",
				#	"over_image" : LOCALE_PATH + "button/fb_over.png",
				#	"down_image" : LOCALE_PATH + "button/fb_down.png",
				},
				
				{
					"name" : "youtube_btn",
					"type" : "button",

					"x" : 76+10+10,
					"y" : 11,

				#	"default_image" : LOCALE_PATH + "button/yt.png",
				#	"over_image" : LOCALE_PATH + "button/yt_over.png",
				#	"down_image" : LOCALE_PATH + "button/yt_down.png",
				},
				
				{
					"name" : "discord_btn",
					"type" : "button",

					"x" : 138+10+20+10,
					"y" : 11,

				#	"default_image" : LOCALE_PATH + "button/disc.png",
				#	"over_image" : LOCALE_PATH + "button/disc_over.png",
				#	"down_image" : LOCALE_PATH + "button/disc_down.png",
				},
				
				{
					"name" : "WikiButton",
					"type" : "button",

					"x" : 198+10+30+10,
					"y" : 11,

				#	"default_image" : LOCALE_PATH + "button/wk.png",
				#	"over_image" : LOCALE_PATH + "button/wk_over.png",
				#	"down_image" : LOCALE_PATH + "button/wk_down.png",
				},
				


			),
		},
		

		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : (SCREEN_WIDTH - 652) / 2,
			"y" : (SCREEN_HEIGHT - 300) / 2,
			

			"image" : LOCALE_PATH + "fereastra_fundal1.png",
			
			"width" : 382,
			"height" : 402,

			"children" :
			(
		
				
				{
					"name" : "ID_Back",
					"type" : "image",

					"x" : 26,
					"y" : 126,

					"width" : 213,
					"height" : 54,
					
					"image" : LOCALE_PATH + "username.png",

					"children" :
					(
						{
							"name" : "ID_EditLine",
							"type" : "editline",
		
							"x" : 20,
							"y" : 12,
		
							"width" : 281,
							"height" : 35,
							
							"vertical_align" : "center",
		
							"input_limit" : ID_LIMIT_COUNT,
							"enable_codepage" : 0,
		
							"r" : 1.0,
							"g" : 1.0,
							"b" : 1.0,
							"a" : 1.0,
						},

					),
				},
				{
					"name" : "Password_Back",
					"type" : "image",

					"x" : 26,
					"y" : 171,

					"width" : 313,
					"height" : 54,
					
					"image" : LOCALE_PATH + "password.png",

					"children" :
					(
						{
							"name" : "Password_EditLine",
							"type" : "editline",
		
							"x" : 20,
							"y" : 12,
		
							"width" : 281,
							"height" : 35,
							
							"vertical_align" : "center",
		
							"input_limit" : PW_LIMIT_COUNT,
							"secret_flag" : 1,
							"enable_codepage" : 0,
		
							"r" : 1.0,
							"g" : 1.0,
							"b" : 1.0,
							"a" : 1.0,
						},
						

					),
				},
				
				{
					"name" : "LoginButton",
					"type" : "button",

					"x" : 26,
					"y" : 231,

					"default_image" : LOCALE_PATH + "login_def.png",
					"over_image" : LOCALE_PATH + "login_over.png",
					"down_image" : LOCALE_PATH + "login_down.png",
					

				},
				{
					"name" : "exit_button",
					"type" : "button",

					"x" : 26,
					"y" : 407,

					"default_image" : LOCALE_PATH + "exit.png",
					"over_image" : LOCALE_PATH + "exit_over.png",
					"down_image" : LOCALE_PATH + "exi_downt.png",
				},
				
				
				{
					"name" : "btn_lang_ro",
					"type" : "button",

					"x" : 36,
					"y" : 340,

					"tooltip_text" : "RO",

					"default_image" : LOCALE_PATH + "flag/ro_normal.png",
					"over_image" : LOCALE_PATH + "flag/ro_select.png",
					"down_image" : LOCALE_PATH + "flag/ro_select.png",

				},
				{
					"name" : "btn_lang_en",
					"type" : "button",

					"x" : 36 + 81,
					"y" : 340,

					"tooltip_text" : "EN",

					"default_image" : LOCALE_PATH + "flag/en_normal.png",
					"over_image" : LOCALE_PATH + "flag/en_select.png",
					"down_image" : LOCALE_PATH + "flag/en_select.png",

				},
				{
					"name" : "btn_lang_de",
					"type" : "button",

					"x" : 36 + 81 + 81,
					"y" : 340,
					
					"tooltip_text" : "DE",

					"default_image" : LOCALE_PATH + "flag/de_normal.png",
					"over_image" : LOCALE_PATH + "flag/de_select.png",
					"down_image" : LOCALE_PATH + "flag/de_select.png",
					

				},
				{
					"name" : "btn_lang_tr",
					"type" : "button",

					"x" : 158,
					"y" : 340,
					
			#		"tooltip_text" : "TR",

			#		"default_image" : LOCALE_PATH + "flag/turky.sub",
			#		"over_image" : LOCALE_PATH + "flag/turky_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/turky_down.sub",

				},
				{
					"name" : "btn_lang_pl",
					"type" : "button",

					"x" : 199,
					"y" : 340,
					
			#		"tooltip_text" : "PL",

			#		"default_image" : LOCALE_PATH + "flag/poland.sub",
			#		"over_image" : LOCALE_PATH + "flag/poland_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/poland_down.sub",
				},
				{
					"name" : "btn_lang_pt",
					"type" : "button",

					"x" : 239,
					"y" : 340,
					
			#		"tooltip_text" : "PT",

			#		"default_image" : LOCALE_PATH + "flag/portugal.sub",
			#		"over_image" : LOCALE_PATH + "flag/portugal_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/portugal_down.sub",
				},
				{
					"name" : "btn_lang_es",
					"type" : "button",

					"x" : 36,
					"y" : 367,

			#		"tooltip_text" : "ES",

			#		"default_image" : LOCALE_PATH + "flag/spain.sub",
			#		"over_image" : LOCALE_PATH + "flag/spain_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/spain_down.sub",
				},
				
				{
					"name" : "btn_lang_fr",
					"type" : "button",

					"x" : 77,
					"y" : 367,
					
			#		"tooltip_text" : "FR",

			#		"default_image" : LOCALE_PATH + "flag/france.sub",
			#		"over_image" : LOCALE_PATH + "flag/france_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/france_down.sub",
				},
				
				{
					"name" : "btn_lang_it",
					"type" : "button",

					"x" : 117,
					"y" : 367,
					
			#		"tooltip_text" : "IT",

			#		"default_image" : LOCALE_PATH + "flag/italy.sub",
			#		"over_image" : LOCALE_PATH + "flag/italy_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/italy_down.sub",
				},
				
				{
					"name" : "btn_lang_gr",
					"type" : "button",

					"x" : 158,
					"y" : 367,

			#		"tooltip_text" : "GR",

			#		"default_image" : LOCALE_PATH + "flag/greece.sub",
			#		"over_image" : LOCALE_PATH + "flag/greece_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/greece_down.sub",
				},
				
				{
					"name" : "btn_lang_hu",
					"type" : "button",

					"x" : 199,
					"y" : 367,

			#		"tooltip_text" : "HU",

			#		"default_image" : LOCALE_PATH + "flag/ungary.sub",
			#		"over_image" : LOCALE_PATH + "flag/ungary_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/ungary_down.sub",
				},
				
				{
					"name" : "btn_lang_cz",
					"type" : "button",

					"x" : 239,
					"y" : 367,
					
			#		"tooltip_text" : "CZ",

			#		"default_image" : LOCALE_PATH + "flag/czech.sub",
			#		"over_image" : LOCALE_PATH + "flag/czech_over.sub",
			#		"down_image" : LOCALE_PATH + "flag/czech_down.sub",
				},

			),
		},
		{
			"name" : "bg_top",
			"type" : "bar",
			"x" : MIDDLE_WIDTH,
			"y" : MIDLLE_HEIGHT,

			"color" : 0x00000000,
		},
		{
			"name" : "popupMSG",
			"type" : "bar",

			"x" : MIDDLE_WIDTH,
			"y" : MIDLLE_HEIGHT,

		},
		{
			"name" : "chstatus",
			"type" : "text",
			"x" : SCREEN_WIDTH /2-295,
			"y" : (MIDLLE_HEIGHT)-42,
			"text" : "##########",
		},
	),
}