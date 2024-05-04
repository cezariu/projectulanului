#blackdragonx61 (28.11.21)
import ui
import item
import uitooltip
import app
import net
import player
import uiscriptlocale
import uiprivateshopbuilder

class ChestDropInfoWindow(ui.ScriptWindow):
	DROP_SLOT_SIZE = 5 * 8
	ITEM = 0
	COUNT = 1

	def __init__(self) :
		ui.ScriptWindow.__init__(self)	
		self.isLoaded = False
		self.ItemVnum = -1
		self.PageCount = 0
		self.CurrentPage = 0
		self.DropDict = dict()
		self.MainItemSlot = None
		self.DropItemSlot = None
		self.prevButton = None
		self.nextButton = None
		self.currentPageText = None
		self.openController = None
		self.openButton = None
		self.openAmount = 0
		self.totalAmount = 0
		self.slotPos = 0
		self.slotWindow = 0
		self.tooltipitem = None

	def __del__(self) :
		ui.ScriptWindow.__del__(self)
		self.DropDict = None
		self.MainItemSlot = None
		self.DropItemSlot = None
		self.prevButton = None
		self.nextButton = None
		self.currentPageText = None
		self.tooltipitem = None
		self.openController = None
		self.openButton = None
		self.openAmount = 0
		self.slotPos = 0
		self.slotWindow = 0

	def __LoadWindow(self):
		if self.isLoaded:
			return

		self.isLoaded = True

		# script
		try:
			self.__LoadScript("UIScript/ChestDropInfoWindow.py")
		except:
			import exception
			exception.Abort("ChestDropInfoWindow.__LoadWindow.__LoadScript")

		# object
		try:
			self.__BindObject()
		except:
			import exception
			exception.Abort("ChestDropInfoWindow.__LoadWindow.__BindObject")

		# event
		try:
			self.__BindEvent()
		except:
			import exception
			exception.Abort("ChestDropInfoWindow.__LoadWindow.__BindEvent")
		
		self.tooltipitem = uitooltip.ItemToolTip()
		self.OverOutItem()

	def __LoadScript(self, fileName):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, fileName)

	def __BindObject(self):
		self.MainItemSlot		= self.GetChild("main_item_slot")
		self.DropItemSlot		= self.GetChild("drop_item_slot")
		self.prevButton			= self.GetChild("prev_button")
		self.nextButton			= self.GetChild("next_button")
		self.currentPageText	= self.GetChild("CurrentPage")
		self.openController = self.GetChild("OpenController")
		self.openButton = self.GetChild("OpenButton")

	def __BindEvent(self):
		self.GetChild("board").SetCloseEvent(ui.__mem_func__(self.Close))
		
		self.MainItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInMainItemSlot))
		self.MainItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.DropItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInDropItemSlot))
		self.DropItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.prevButton.SetEvent(ui.__mem_func__(self.SetPage), -1)
		self.nextButton.SetEvent(ui.__mem_func__(self.SetPage), +1)
		self.openController.SetEvent(ui.__mem_func__(self.OnChangeController))
		self.openButton.SetEvent(ui.__mem_func__(self.OnOpenButton))

	def SetOpenAmount(self, amount):
		if self.slotPos == -1:
			return
		
		self.openAmount = amount
		self.openButton.SetText(uiscriptlocale.OPTION_SETTING + " (" + str(amount) + ") ")

	def OnChangeController(self):
		if self.slotPos == -1:
			return
		
		openTemp = int(self.openController.GetSliderPos() * 10)
		if openTemp == 0:
			self.SetOpenAmount(1)
		else:
			self.SetOpenAmount(openTemp)

	def OnOpenButton(self):
		if self.slotPos == -1:
			return
		
		if uiprivateshopbuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return
		
		itemCount = player.GetItemCount(self.slotWindow, self.slotPos)
		if itemCount >= self.openAmount:
			for i in xrange(self.openAmount):
				net.SendItemUsePacket(self.slotWindow, self.slotPos)
				if itemCount == 1:
					self.Close()
					break
				
				itemCount = itemCount - 1
		else:
			for i in xrange(itemCount):
				net.SendItemUsePacket(self.slotWindow, self.slotPos)
				if itemCount == 1:
					self.Close()
					break
				
				itemCount = itemCount - 1

	def UpdateItems(self):
		for i in range(ChestDropInfoWindow.DROP_SLOT_SIZE):
			self.DropItemSlot.ClearSlot(i)

		if self.CurrentPage in self.DropDict:
			for pos in self.DropDict[self.CurrentPage]:
				data = self.DropDict[self.CurrentPage][pos]
				self.DropItemSlot.SetItemSlot(pos, data[ChestDropInfoWindow.ITEM], data[ChestDropInfoWindow.COUNT])
		
		self.DropItemSlot.RefreshSlot()
	
	def SetPage(self, page):
		nextpage = page + self.CurrentPage
		if 0 <= nextpage <= self.PageCount:
			self.CurrentPage = nextpage
			self.currentPageText.SetText(str(self.CurrentPage + 1))
			self.UpdateItems()
	
	def SetUp(self, itemVnum, isMain):
		self.ItemVnum = itemVnum
		self.MainItemSlot.SetItemSlot(0, self.ItemVnum, 0)
		self.MainItemSlot.RefreshSlot()

		(self.PageCount, DropList) = item.GetDropInfo(self.ItemVnum, isMain)

		self.DropDict.clear()
		for i in range(self.PageCount + 1):
			self.DropDict[i] = dict()

		for page, pos, vnum, count in DropList:
			self.DropDict[page][pos] = (vnum, count)

		self.CurrentPage = 0
		self.SetPage(0)

	def Open(self, itemVnum, isMain, slotPos, slotWindow):
		if self.IsShow():
			return
		
		self.__LoadWindow()
		self.slotPos = slotPos
		self.slotWindow = slotWindow
		if slotPos == -1:
			self.openController.Hide()
			self.openButton.Hide()
		else:
			self.openController.Show()
			self.openButton.Show()
		
		self.SetUp(itemVnum, isMain)
		self.SetOpenAmount(1)
		self.openController.SetSliderPos(0.0)

		self.SetCenterPosition()
		self.SetTop()
		self.Show()
	
	def OverInMainItemSlot(self, slotIndex):
		if self.tooltipitem:
			self.tooltipitem.SetItemToolTip(self.ItemVnum)

	def OverInDropItemSlot(self, slotIndex):
		if self.tooltipitem:
			if self.CurrentPage in self.DropDict:
				if slotIndex in self.DropDict[self.CurrentPage]:
					data = self.DropDict[self.CurrentPage][slotIndex]
					self.tooltipitem.SetItemToolTip(data[ChestDropInfoWindow.ITEM])

	def OverOutItem(self):
		if self.tooltipitem:
			self.tooltipitem.HideToolTip()
			self.tooltipitem.ClearToolTip()

	def Close(self):
		self.OverOutItem()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True