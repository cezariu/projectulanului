if __USE_DYNAMIC_MODULE__:
	import pyapi

import app
import chrmgr
import player
import net
import ui
import uiscriptlocale
import dbg
import background
import wndMgr

import localeinfo
import colorinfo
import constinfo

import playersettingmodule
import stringcommander
import emotion

####################################
# ���� ������ ���� ��� �ε� �д�
####################################
#import uirefine
#import uitooltip
#import uiattachmetin
#import uipickmoney
#import uichat
#import uimessenger
#import uiwhisper
#import uipointreset
#import uishop
#import uiexchange
#import uisystem
#import uioption
#import uirestart
####################################

class LoadingWindow(ui.ScriptWindow):
	def __init__(self, stream):
		print "NEW LOADING WINDOW -------------------------------------------------------------------------------"
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, self)

		self.stream=stream
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.update=0
		self.playerX=0
		self.playerY=0
		self.loadStepList=[]

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE LOADING WINDOW"
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, 0)
		ui.Window.__del__(self)

	def Open(self):
		app.SetFrameSkip(0)
		self.SetSize(wndMgr.GetScreenWidth(),wndMgr.GetScreenHeight())
		#try:
		#	pyScrLoader = ui.PythonScriptLoader()
		#	pyScrLoader.LoadScriptFile(self, "UIScript/LoadingWindow.py")
		#except:
		#	exception.Abort("LodingWindow.Open - LoadScriptFile Error")
		#try:
		#	self.loadingImage=self.GetChild("BackGround")
		#except:
		#	exception.Abort("LodingWindow.Open - LoadScriptFile Error")

		#self.loadingImage.SetSize(150,150)
		#self.loadingImage.SetWindowHorizontalAlignCenter()
		#self.loadingImage.SetWindowVerticalAlignCenter()
		#self.loadingImage.SetPosition(0,0)
		#self.Show()

		self.Show()

		self.imgWaiting = ui.AniImageBox()
		self.imgWaiting.SetParent(self)
		self.imgWaiting.SetSize(150,150)
		self.imgWaiting.SetDelay(2)
		for i in xrange(24):
			self.imgWaiting.AppendImage("d:/ymir work/ui/loading_progres/img00%02d.tga" % (i+1))

		self.imgWaiting.Show()
		self.imgWaiting.SetPosition(0,0)
		self.imgWaiting.SetWindowHorizontalAlignCenter()
		self.imgWaiting.SetWindowVerticalAlignCenter()
		self.imgWaiting.SetPosition(0,0)

		chrSlot=self.stream.GetCharacterSlot()
		net.SendSelectCharacterPacket(chrSlot)
		app.SetFrameSkip(1)

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE LOADING WINDOW"

		app.SetFrameSkip(1)

		self.loadStepList=[]
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.ClearDictionary()
		self.Hide()

	def OnPressEscapeKey(self):
		app.SetFrameSkip(1)
		self.stream.SetLoginPhase()
		return True

	def __SetNext(self, next):
		if next:
			self.update=ui.__mem_func__(next)
		else:
			self.update=0

	def __SetProgress(self, p):
		if self.loadingGage:
			self.loadingGage.SetPercentage(2+98*p/100, 100)

	if app.ENABLE_RACE_HEIGHT:
		def __LoadRaceHeight(self):
			playersettingmodule.LoadGameData("RACE_HEIGHT")

	def LoadData(self, playerX, playerY):
		self.playerX=playerX
		self.playerY=playerY

		self.RegisterSkill() ## �ε� �߰��� ���� �ϸ� ���� �߻�
		self.__RegisterTitleName()
		
		self.__RegisterColor()
		self.__RegisterEmotionIcon()

		self.loadStepList=[
			(50, ui.__mem_func__(self.__LoadWarrior)),
			(60, ui.__mem_func__(self.__LoadAssassin)),
			(70, ui.__mem_func__(self.__LoadSura)),
			(80, ui.__mem_func__(self.__LoadShaman)),
			(90, ui.__mem_func__(self.__LoadSkill)),
			(100, ui.__mem_func__(self.__StartGame)),
		]
		
		if app.ENABLE_WOLFMAN_CHARACTER:
			self.loadStepList+=[(100, ui.__mem_func__(self.__LoadWolfman)),]
		if app.ENABLE_RACE_HEIGHT:
			self.loadStepList+=[(98, ui.__mem_func__(self.__LoadRaceHeight)),]
		
		self.__SetProgress(0)

	def OnUpdate(self):
		if len(self.loadStepList)>0:
			(progress, runFunc)=self.loadStepList[0]

			try:
				runFunc()
			except:
				self.errMsg.Show()
				self.loadStepList=[]

				## �̰����� syserr.txt �� ������.

				import dbg
				dbg.TraceError(" !!! Failed to load game data : STEP [%d]" % (progress))

				#import shutil
				#import os
				#shutil.copyfile("syserr.txt", "errorlog.txt")
				#os.system("errorlog.exe")

				app.Exit()

				return

			self.loadStepList.pop(0)

			self.__SetProgress(progress)

	def RegisterSkill(self):
		playersettingmodule.RegisterSkill(net.GetMainActorRace(), net.GetMainActorSkillGroup(), net.GetMainActorEmpire())

	def __RegisterTitleName(self):
		for i in xrange(len(localeinfo.TITLE_NAME_LIST)):
			chrmgr.RegisterTitleName(i, localeinfo.TITLE_NAME_LIST[i], localeinfo.TITLE_NAME_LIST[i])

	def __RegisterColor(self):

		## Name
		NAME_COLOR_DICT = {
			chrmgr.NAMECOLOR_PC : colorinfo.CHR_NAME_RGB_PC,
			chrmgr.NAMECOLOR_NPC : colorinfo.CHR_NAME_RGB_NPC,
			chrmgr.NAMECOLOR_MOB : colorinfo.CHR_NAME_RGB_MOB,
			chrmgr.NAMECOLOR_PVP : colorinfo.CHR_NAME_RGB_PVP,
			chrmgr.NAMECOLOR_PK : colorinfo.CHR_NAME_RGB_PK,
			chrmgr.NAMECOLOR_PARTY : colorinfo.CHR_NAME_RGB_PARTY,
			chrmgr.NAMECOLOR_WARP : colorinfo.CHR_NAME_RGB_WARP,
			chrmgr.NAMECOLOR_WAYPOINT : colorinfo.CHR_NAME_RGB_WAYPOINT,

			chrmgr.NAMECOLOR_EMPIRE_MOB : colorinfo.CHR_NAME_RGB_EMPIRE_MOB,
			chrmgr.NAMECOLOR_EMPIRE_NPC : colorinfo.CHR_NAME_RGB_EMPIRE_NPC,
			chrmgr.NAMECOLOR_EMPIRE_PC+1 : colorinfo.CHR_NAME_RGB_EMPIRE_PC_A,
			chrmgr.NAMECOLOR_EMPIRE_PC+2 : colorinfo.CHR_NAME_RGB_EMPIRE_PC_B,
			chrmgr.NAMECOLOR_EMPIRE_PC+3 : colorinfo.CHR_NAME_RGB_EMPIRE_PC_C,
		}
		for name, rgb in NAME_COLOR_DICT.items():
			chrmgr.RegisterNameColor(name, rgb[0], rgb[1], rgb[2])

		## Title
		TITLE_COLOR_DICT = (	colorinfo.TITLE_RGB_GOOD_4,
								colorinfo.TITLE_RGB_GOOD_3,
								colorinfo.TITLE_RGB_GOOD_2,
								colorinfo.TITLE_RGB_GOOD_1,
								colorinfo.TITLE_RGB_NORMAL,
								colorinfo.TITLE_RGB_EVIL_1,
								colorinfo.TITLE_RGB_EVIL_2,
								colorinfo.TITLE_RGB_EVIL_3,
								colorinfo.TITLE_RGB_EVIL_4,	)
		
		count = 0
		for rgb in TITLE_COLOR_DICT:
			chrmgr.RegisterTitleColor(count, rgb[0], rgb[1], rgb[2])
			count += 1

	def __RegisterEmotionIcon(self):
		emotion.RegisterEmotionIcons()

	def __LoadWarrior(self):
		playersettingmodule.LoadGameData("WARRIOR")
	
	def __LoadAssassin(self):
		playersettingmodule.LoadGameData("ASSASSIN")
	
	def __LoadSura(self):
		playersettingmodule.LoadGameData("SURA")
	
	def __LoadShaman(self):
		playersettingmodule.LoadGameData("SHAMAN")

	if app.ENABLE_WOLFMAN_CHARACTER:
		def __LoadWolfman(self):
			playersettingmodule.LoadGameData("WOLFMAN")

	def __LoadSkill(self):
		playersettingmodule.LoadGameData("SKILL")

	def __StartGame(self):
		background.SetViewDistanceSet(background.DISTANCE0, 25600)
		"""
		background.SetViewDistanceSet(background.DISTANCE1, 19200)
		background.SetViewDistanceSet(background.DISTANCE2, 12800)
		background.SetViewDistanceSet(background.DISTANCE3, 9600)
		background.SetViewDistanceSet(background.DISTANCE4, 6400)
		"""
		background.SelectViewDistanceNum(background.DISTANCE0)
		app.SetGlobalCenterPosition(self.playerX, self.playerY)
		net.StartGame()
		#import dbg
		#dbg.TraceError("finish %s" % (str(app.GetGlobalTimeStamp())))

