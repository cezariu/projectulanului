if __USE_DYNAMIC_MODULE__:
	import pyapi

import app
import localeinfo

app.ServerName = None

SRV1 = {
	"name":"Hypnotic2",
	"host":"81.180.202.36",
	"auth1":30052,
	"ch1":30054,
	"ch2":30058,
	"ch3":30062,
	"ch4":30066,
}

STATE_NONE = "|cFF17EA17Online"

STATE_DICT = {
	0 : "|cFFFF0000Non Disponibile",
	1 : "|cFF17EA17Online",
	2 : "|cFFFF4500Occupato",
	3 : "|cFFFF0000Pieno"
}

SERVER1_CHANNEL_DICT = {
	1:{"key":11,"name":"CH1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"CH2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":13,"name":"CH3","ip":SRV1["host"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
	4:{"key":14,"name":"CH4","ip":SRV1["host"],"tcp_port":SRV1["ch4"],"udp_port":SRV1["ch4"],"state":STATE_NONE,},
}

REGION_NAME_DICT = {
	1 : SRV1["name"],
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
	},
}

REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : SERVER1_CHANNEL_DICT, },
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
}

TESTADDR = { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "udp_port" : SRV1["ch1"], }