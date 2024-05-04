if __USE_DYNAMIC_MODULE__:
	import pyapi

import app
import player
import net
import ui
import mousemodule
import snd
import item
import chat
import grp
import uiscriptlocale
import uirefine
import uiattachmetin
import uipickmoney
import uicommon
import uiprivateshopbuilder
import constinfo
import ime
import uiinventory
import sys
import localeinfo

ITEM_FLAG_APPLICABLE = 1 << 14

# ��ȥ�� Vnum�� ���� comment
# ITEM VNUM�� 10�� �ڸ�����, FEDCBA��� �Ѵٸ�
# FE : ��ȥ�� ����.	D : ���
# C : �ܰ�			B : ��ȭ
# A : ������ ��ȣ��...

if app.ENABLE_DS_REFINE_ALL:
	ds_type_page = 0
	ds_grade_page = 0

class DragonSoulWindow(ui.ScriptWindow):
	MAX_VIEWBUTTON = 3
	MAX_VIEWBUTTON_TEXT = [uiscriptlocale.DS_GRADE3, uiscriptlocale.DS_GRADE4, uiscriptlocale.DS_GRADE5]
	KIND_TAP_TITLES = [uiscriptlocale.DRAGONSOUL_TAP_TITLE_1, uiscriptlocale.DRAGONSOUL_TAP_TITLE_2, uiscriptlocale.DRAGONSOUL_TAP_TITLE_3, uiscriptlocale.DRAGONSOUL_TAP_TITLE_4, uiscriptlocale.DRAGONSOUL_TAP_TITLE_5, uiscriptlocale.DRAGONSOUL_TAP_TITLE_6]
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.questionDialog = None
		self.tooltipItem = None
		self.sellingSlotNumber = -1
		self.isLoaded = 0
		self.isActivated = False
		self.DSKindIndex = 0
		self.tabDict = None
		self.tabButtonDict = None
		self.deckPageIndex = 0
		self.inventoryPageIndex = 0
		if app.ENABLE_DS_SET:
			self.bnsSetNo = None
			self.bnsSetYes = None
			self.setStat = 0
		
		self.SetWindowName("DragonSoulWindow")
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)
		self.RefreshDSSet()
		if app.ENABLE_DS_REFINE_ALL:
			global ds_type_page
			ds_type_page = self.DSKindIndex
			global ds_grade_page
			ds_grade_page = self.inventoryPageIndex

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return
		self.isLoaded = 1
		try:
			pyScrLoader = ui.PythonScriptLoader()
			if app.ENABLE_DS_GRADE_MYTH:
				pyScrLoader.LoadScriptFile(self, "uiscript/dragonsoulwindow.py")
			else:
				pyScrLoader.LoadScriptFile(self, "uiscript/dragonsoulwindow_c.py")

		except:
			import exception
			exception.Abort("dragonsoulwindow.LoadWindow.LoadObject")
		try:
			if localeinfo.IsARABIC():
				self.board = self.GetChild("Equipment_Base")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
				self.board = self.GetChild("Tab_01")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
				self.board = self.GetChild("Tab_02")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
				self.board = self.GetChild("Tab_03")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
				self.board = self.GetChild("Tab_04")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
				self.board = self.GetChild("Tab_05")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
				self.board = self.GetChild("Tab_06")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
			
			wndItem = self.GetChild("ItemSlot")
			wndEquip = self.GetChild("EquipmentSlot")
			self.activateButton = self.GetChild("activate")
			
			if app.__ENABLE_RANGE_ALCHEMY__:
				self.shopButton = self.GetChild("shop_open")
				
			if app.__ENABLE_REFINE_ALCHEMY__:
				self.refineButton = self.GetChild("refine_window_open")
				
			
			self.deckTab = []
			self.deckTab.append(self.GetChild("deck1"))
			self.deckTab.append(self.GetChild("deck2"))
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.inventoryTab = []
			for i in xrange(self.MAX_VIEWBUTTON):
				self.inventoryTab.append(self.GetChild("Inventory_Tab_0%d" % i))
			
			self.tabDict = {
				0	: self.GetChild("Tab_01"),
				1	: self.GetChild("Tab_02"),
				2	: self.GetChild("Tab_03"),
				3	: self.GetChild("Tab_04"),
				4	: self.GetChild("Tab_05"),
				5	: self.GetChild("Tab_06"),
			}
			self.tabButtonDict = {
				0	: self.GetChild("Tab_Button_01"),
				1	: self.GetChild("Tab_Button_02"),
				2	: self.GetChild("Tab_Button_03"),
				3	: self.GetChild("Tab_Button_04"),
				4	: self.GetChild("Tab_Button_05"),
				5	: self.GetChild("Tab_Button_06"),
			}
			self.tabText = self.GetChild("tab_text_area")
			
			if app.ENABLE_DS_SET:
				self.bnsSetNo = self.GetChild("bnsSetDeactivated")
				self.bnsSetYes = self.GetChild("bnsSetActivated")
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.BindObject")
		## DragonSoul Kind Tap
		for (tabKey, tabButton) in self.tabButtonDict.items():
			tabButton.SetEvent(ui.__mem_func__(self.SetDSKindIndex), tabKey)
		## Item
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))

		## Equipment
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptyEquipSlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectEquipItemSlot))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseEquipItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.UseEquipItemSlot))
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInEquipItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OverOutEquipItem))

		## Deck
		self.deckTab[0].SetToggleDownEvent(lambda arg=0: self.SetDeckPage(arg))
		self.deckTab[1].SetToggleDownEvent(lambda arg=1: self.SetDeckPage(arg))
		self.deckTab[0].SetToggleUpEvent(lambda arg=0: self.__DeckButtonDown(arg))
		self.deckTab[1].SetToggleUpEvent(lambda arg=1: self.__DeckButtonDown(arg))
		self.deckTab[0].Down()
		## Grade button
		for i in xrange(self.MAX_VIEWBUTTON):
			self.inventoryTab[i].SetEvent(lambda arg = i: self.SetInventoryPage(arg))
			if i == 0:
				self.inventoryTab[0].Down()
		## Etc
		self.wndItem = wndItem
		self.wndEquip = wndEquip

		self.dlgQuestion = uicommon.QuestionDialog2()
		self.dlgQuestion.Close()

		self.activateButton.SetToggleDownEvent(ui.__mem_func__(self.ActivateButtonClick))
		self.activateButton.SetToggleUpEvent(ui.__mem_func__(self.ActivateButtonClick))
		
		
		if app.__ENABLE_RANGE_ALCHEMY__:
			self.shopButton.SetEvent(ui.__mem_func__(self.__OpenShopWindow))
			
		if app.__ENABLE_REFINE_ALCHEMY__:
			self.refineButton.SetEvent(ui.__mem_func__(self.__OpenRefineAlchemyWindow))
		
		self.wndPopupDialog = uicommon.PopupDialog()
		
		##
		self.listHighlightedSlot = []

		## Refresh
		self.SetInventoryPage(0)
		self.RefreshItemSlot()
		self.RefreshEquipSlotWindow()
		self.RefreshBagSlotWindow()
		self.SetDSKindIndex(0)
		self.activateButton.Enable()
		self.deckTab[self.deckPageIndex].Down()
		self.activateButton.SetUp()
		if app.ENABLE_DS_SET:
			self.RefreshDSSet()
			self.bnsSetNo.SetStringEvent("MOUSE_OVER_IN", self.OnBnsSetIn)
			self.bnsSetNo.SetStringEvent("MOUSE_OVER_OUT", self.OnBnsSetOut)
			self.bnsSetYes.SetStringEvent("MOUSE_OVER_IN", self.OnBnsSetIn)
			self.bnsSetYes.SetStringEvent("MOUSE_OVER_OUT", self.OnBnsSetOut)

	def Destroy(self):
		self.ClearDictionary()
		self.tooltipItem = None
		self.wndItem = 0
		self.wndEquip = 0
		self.activateButton = 0
		if app.__ENABLE_RANGE_ALCHEMY__:
			self.shopButton = 0
			
		if app.__ENABLE_REFINE_ALCHEMY__:
			self.refineButton = 0
		
		self.questionDialog = None
		self.mallButton = None
		self.inventoryTab = []
		self.deckTab = []
		self.equipmentTab = []
		self.tabDict = None
		self.tabButtonDict = None

	def Close(self):
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()
		self.Hide()

	if app.ENABLE_DS_SET:
		def OnBnsSetIn(self):
			if self.tooltipItem:
				self.tooltipItem.ClearToolTip()
				self.tooltipItem.AppendDSSetInfo()

			if self.tooltipItem:
				self.tooltipItem.ShowToolTip()

		def OnBnsSetOut(self):
			if self.tooltipItem:
				self.tooltipItem.HideToolTip()

		def SetDSSet(self, idx):
			self.setStat = idx
			self.RefreshDSSet()

		def RefreshDSSet(self):
			if self.setStat == 0:
				self.bnsSetNo.Show()
				self.bnsSetYes.Hide()
			else:
				self.bnsSetNo.Hide()
				self.bnsSetYes.Show()

	def __DeckButtonDown(self, deck):
		self.deckTab[deck].Down()

	def SetInventoryPage(self, page):
		pageReal = page + 3
		if self.inventoryPageIndex != pageReal:
			self.__HighlightSlot_ClearCurrentPage()
		self.inventoryPageIndex = pageReal
		for i in xrange(self.MAX_VIEWBUTTON):
			if i == page:
				continue
			
			self.inventoryTab[i].SetUp()
		
		self.tabText.SetText(self.KIND_TAP_TITLES[self.DSKindIndex] % self.MAX_VIEWBUTTON_TEXT[self.inventoryPageIndex - 3])
		self.RefreshBagSlotWindow()
		if app.ENABLE_DS_REFINE_ALL:
			global ds_grade_page
			ds_grade_page = self.inventoryPageIndex

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def RefreshItemSlot(self):
		self.RefreshBagSlotWindow()
		self.RefreshEquipSlotWindow()

	def RefreshEquipSlotWindow(self):
		for i in xrange(6):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(player.INVENTORY, player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i)
			itemVnum = player.GetItemIndex(slotNumber)
			self.wndEquip.SetItemSlot(player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i, itemVnum, 0)
			self.wndEquip.EnableSlot(player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i)
			
			if itemVnum != 0:
				if self.isActivated:
					if not self.wndEquip.IsActiveSlot(player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i):
						self.wndEquip.ActivateSlot(player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i)
				else:
					self.wndEquip.DeactivateSlot(player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i)
				
				item.SelectItem(itemVnum)
				for j in xrange(item.LIMIT_MAX_NUM):
					(limitType, limitValue) = item.GetLimit(j)
					remain_time = 999
					if item.LIMIT_REAL_TIME == limitType:
						remain_time = player.GetItemMetinSocket(player.INVENTORY, slotNumber, 0) - app.GetGlobalTimeStamp()
					elif item.LIMIT_REAL_TIME_START_FIRST_USE == limitType:
						remain_time = player.GetItemMetinSocket(player.INVENTORY, slotNumber, 0) - app.GetGlobalTimeStamp()
					elif item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
						remain_time = player.GetItemMetinSocket(player.INVENTORY, slotNumber, 0)
					
					if remain_time <= 0:
						self.wndEquip.DisableSlot(player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i)
						break
		
		self.wndEquip.RefreshSlot()

	def RefreshStatus(self):
		self.RefreshItemSlot()

	def __InventoryLocalSlotPosToGlobalSlotPos(self, window_type, local_slot_pos):
		if player.INVENTORY == window_type:
			return self.deckPageIndex * player.DRAGON_SOUL_EQUIPMENT_FIRST_SIZE + local_slot_pos
		
		if app.ENABLE_DS_GRADE_MYTH:
			return 300 + ((self.DSKindIndex * player.DRAGON_SOUL_PAGE_COUNT * player.DRAGON_SOUL_PAGE_SIZE) + self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE + local_slot_pos)
		else:
			return 300 + ((self.DSKindIndex * 5 * player.DRAGON_SOUL_PAGE_SIZE) + self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE + local_slot_pos)

	def RefreshBagSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVnum=self.wndItem.SetItemSlot
		for i in xrange(player.DRAGON_SOUL_PAGE_SIZE):
			self.wndItem.EnableSlot(i)
			#<- dragon soul kind
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, i)

			itemCount = getItemCount(player.DRAGON_SOUL_INVENTORY, slotNumber)
			if 0 == itemCount:
				self.wndItem.ClearSlot(i)
				continue
			elif 1 == itemCount:
				itemCount = 0
			itemVnum = getItemVNum(player.DRAGON_SOUL_INVENTORY, slotNumber)

			setItemVnum(i, itemVnum, itemCount)

			if itemVnum != 0:
				item.SelectItem(itemVnum)
				for j in xrange(item.LIMIT_MAX_NUM):
					(limitType, limitValue) = item.GetLimit(j)

					# �ؿ��� remain_time�� �������� üũ �ϱ� ������ ������ ����� �ʱ�ȭ
					remain_time = 999
					if item.LIMIT_REAL_TIME == limitType:
						remain_time = player.GetItemMetinSocket(player.DRAGON_SOUL_INVENTORY, slotNumber, 0)
					elif item.LIMIT_REAL_TIME_START_FIRST_USE == limitType:
						remain_time = player.GetItemMetinSocket(player.DRAGON_SOUL_INVENTORY, slotNumber, 0)
					elif item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
						remain_time = player.GetItemMetinSocket(player.DRAGON_SOUL_INVENTORY, slotNumber, 0)

					if remain_time <= 0:
						self.wndItem.DisableSlot(i)
						break

		self.__HighlightSlot_RefreshCurrentPage()
		self.wndItem.RefreshSlot()

	def ShowToolTip(self, window_type, slotIndex):
		if None != self.tooltipItem:
			if player.INVENTORY == window_type:
				self.tooltipItem.SetInventoryItem(slotIndex)
			else:
				self.tooltipItem.SetInventoryItem(slotIndex, player.DRAGON_SOUL_INVENTORY)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnTop(self):
		if None != self.tooltipItem:
			self.tooltipItem.SetTop()

	# item slot ���� �Լ�
	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OverInItem(self, overSlotPos):
		self.wndItem.DeactivateSlot(overSlotPos)
		overSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, overSlotPos)
		try:
			self.listHighlightedSlot.remove(overSlotPos)
		except:
			pass
		
		self.wndItem.SetUsableItem(False)
		if mousemodule.mouseController.isAttached():
			attachedItemVID = mousemodule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedItemVID)
			if item.GetItemType(attachedItemVID) == 3 and item.GetItemSubType(attachedItemVID) == item.USE_DS_ENCHANT:
				targetIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, overSlotPos)
				iGrade = (targetIndex / 1000) % 10
				iStep = (targetIndex / 100) % 10;
				item.SelectItem(targetIndex)
				maxGrade = 4
				maxStep = 4
				if app.ENABLE_DS_GRADE_MYTH:
					maxGrade += 1
				
				if iGrade == maxGrade and iStep == maxStep:
					self.wndItem.SetUseMode(True)
					self.wndItem.SetUsableItem(True)
				else:
					self.wndItem.SetUseMode(False)
					self.wndItem.SetUsableItem(False)
			elif item.GetItemSubType(attachedItemVID) == item.USE_TIME_CHARGE_PER:
				self.wndItem.SetUseMode(True)
				self.wndItem.SetUsableItem(True)
		
		self.ShowToolTip(player.DRAGON_SOUL_INVENTORY, overSlotPos)

	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, slotIndex)
		if 0 == player.GetItemMetinSocket(player.DRAGON_SOUL_INVENTORY, slotIndex, 0):
			self.wndPopupDialog.SetText(localeinfo.DRAGON_SOUL_EXPIRED)
			self.wndPopupDialog.Open()
			return

		self.__EquipItem(slotIndex)

	def __EquipItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, slotIndex)
		item.SelectItem(ItemVNum)
		subType = item.GetItemSubType()
		equipSlotPos = player.DRAGON_SOUL_EQUIPMENT_SLOT_START + self.deckPageIndex * player.DRAGON_SOUL_EQUIPMENT_FIRST_SIZE + subType
		srcItemPos = (player.DRAGON_SOUL_INVENTORY, slotIndex)
		dstItemPos = (player.INVENTORY, equipSlotPos)
		self.__OpenQuestionDialog(True, srcItemPos, dstItemPos)

	def SelectItemSlot(self, itemSlotIndex):
		if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, itemSlotIndex)

		if mousemodule.mouseController.isAttached():
			attachedSlotType = mousemodule.mouseController.GetAttachedType()
			attachedSlotPos = mousemodule.mouseController.GetAttachedSlotNumber()
			attachedItemVID = mousemodule.mouseController.GetAttachedItemIndex()
			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			#@fixme011 BEGIN (changed behavior)
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				if player.IsDSEquipmentSlot(attachedInvenType, attachedSlotPos):
					srcItemPos = (attachedInvenType, attachedSlotPos)
					dstItemPos = (player.DRAGON_SOUL_INVENTORY, itemSlotIndex)
					self.__OpenQuestionDialog(False, srcItemPos, dstItemPos)
				else:
					ITEM_USE = 3
					ITEM_EXTRACT = 31
					item.SelectItem(attachedItemVID)
					if item.GetItemType(attachedItemVID) == ITEM_EXTRACT or\
						item.GetItemType(attachedItemVID) == ITEM_USE and\
						item.GetItemSubType(attachedItemVID) in (item.USE_TIME_CHARGE_PER, item.USE_TIME_CHARGE_FIX):
						net.SendItemUseToItemPacket(attachedInvenType, attachedSlotPos, player.DRAGON_SOUL_INVENTORY, itemSlotIndex)
			elif attachedSlotType == player.SLOT_TYPE_EXTRA_INVENTORY and app.ENABLE_DS_ENCHANT:
				item.SelectItem(attachedItemVID)
				if item.GetItemType(attachedItemVID) == 3 and item.GetItemSubType(attachedItemVID) == item.USE_DS_ENCHANT:
					net.SendItemUseToItemPacket(player.EXTRA_INVENTORY, attachedSlotPos, player.DRAGON_SOUL_INVENTORY, itemSlotIndex)
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedInvenType:
				net.SendItemUseToItemPacket(attachedInvenType, attachedSlotPos, player.DRAGON_SOUL_INVENTORY, itemSlotIndex)
			#@fixme011 END

			mousemodule.mouseController.DeattachObject()

		else:
			## �������� �ȵ��� �߰�
			## 20140220
			curCursorNum = app.GetCursor()

			if app.SELL == curCursorNum:
				self.__SellItem(itemSlotIndex)
			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.SHOP_BUY_INFO)
			elif app.IsPressed(app.DIK_LALT) and app.ENABLE_BUGFIXES:
				link = player.GetItemLink(player.DRAGON_SOUL_INVENTORY, itemSlotIndex)
				ime.PasteString(link)
			else:
				selectedItemVNum = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, itemSlotIndex)
				itemCount = player.GetItemCount(player.DRAGON_SOUL_INVENTORY, itemSlotIndex)
				mousemodule.mouseController.AttachObject(self, player.SLOT_TYPE_DRAGON_SOUL_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
				self.wndItem.SetUseMode(False)
				snd.PlaySound("sound/ui/pick.wav")

	## ������ �ȱ�
	## 2014.02.20 �߰�
	def __SellItem(self, itemSlotPos):
		if not player.IsDSEquipmentSlot(player.DRAGON_SOUL_INVENTORY, itemSlotPos):
			self.sellingSlotNumber = itemSlotPos
			itemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, itemSlotPos)
			itemCount = player.GetItemCount(player.DRAGON_SOUL_INVENTORY, itemSlotPos)

			item.SelectItem(itemIndex)

			if item.IsAntiFlag(item.ANTIFLAG_SELL):
				popup = uicommon.PopupDialog()
				popup.SetText(localeinfo.SHOP_CANNOT_SELL_ITEM)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return

			itemPrice = item.GetISellItemPrice()

			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 5
			else:
				itemPrice = itemPrice * itemCount / 5

			item.GetItemName(itemIndex)
			itemName = item.GetItemName()

			self.questionDialog = uicommon.QuestionDialog()
			self.questionDialog.SetText(localeinfo.DO_YOU_SELL_ITEM(itemName, itemCount, itemPrice))
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellItem))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.count = itemCount

	## ������ �ȱ�
	def SellItem(self):

		net.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count, player.DRAGON_SOUL_INVENTORY)
		snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	## ������ �ȱ�
	def OnCloseQuestionDialog(self):
		if self.questionDialog:
			self.questionDialog.Close()

		self.questionDialog = None

	## ������ �ȱ�
	def __OnClosePopupDialog(self):
		self.pop = None

	def SelectEmptySlot(self, selectedSlotPos):
		if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return
		
		selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, selectedSlotPos)
		if mousemodule.mouseController.isAttached():

			attachedSlotType = mousemodule.mouseController.GetAttachedType()
			attachedSlotPos = mousemodule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mousemodule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mousemodule.mouseController.GetAttachedItemIndex()

			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			if player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
				mousemodule.mouseController.RunCallBack("INVENTORY")

			elif player.SLOT_TYPE_SHOP == attachedSlotType:
				net.SendShopBuyPacket(attachedSlotPos)

			elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:
				if player.ITEM_MONEY == attachedItemIndex:
					net.SendSafeboxWithdrawMoneyPacket(mousemodule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					net.SendSafeboxCheckoutPacket(attachedSlotPos, player.DRAGON_SOUL_INVENTORY, selectedSlotPos)

			elif player.SLOT_TYPE_MALL == attachedSlotType:
				net.SendMallCheckoutPacket(attachedSlotPos, player.DRAGON_SOUL_INVENTORY, selectedSlotPos)

			#@fixme011 BEGIN (changed behavior)
			elif player.SLOT_TYPE_INVENTORY == attachedSlotType:
				if player.IsDSEquipmentSlot(attachedInvenType, attachedSlotPos):
					srcItemPos = (attachedInvenType, attachedSlotPos)
					dstItemPos = (player.DRAGON_SOUL_INVENTORY, selectedSlotPos)
					self.__OpenQuestionDialog(False, srcItemPos, dstItemPos)

			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedSlotType:
				itemCount = player.GetItemCount(attachedInvenType, attachedSlotPos)
				attachedCount = mousemodule.mouseController.GetAttachedItemCount()

				self.__SendMoveItemPacket(attachedInvenType, attachedSlotPos, player.DRAGON_SOUL_INVENTORY, selectedSlotPos, attachedCount)
			#@fixme011 END

			mousemodule.mouseController.DeattachObject()

	def UseItemSlot(self, slotIndex):
		if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return
		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, slotIndex)
		try:
			# ��ȥ�� ��ȭâ�� ����������, ������ ��Ŭ�� �� �ڵ����� ��ȭâ���� ��.
			if self.wndDragonSoulRefine.IsShow():
				if uiprivateshopbuilder.IsBuildingPrivateShop():
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
					return
				self.wndDragonSoulRefine.AutoSetItem((player.DRAGON_SOUL_INVENTORY, slotIndex), 1)
				return
		except:
			pass

		self.__UseItem(slotIndex)

		mousemodule.mouseController.DeattachObject()
		self.OverOutItem()

	def __SendMoveItemPacket(self, srcSlotWindow, srcSlotPos, dstSlotWindow, dstSlotPos, srcItemCount):
		if uiprivateshopbuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemMovePacket(srcSlotWindow , srcSlotPos, dstSlotWindow, dstSlotPos, srcItemCount)

	# equip ���� ���� �Լ���.
	def OverOutEquipItem(self):
		self.OverOutItem()

	def OverInEquipItem(self, overSlotPos):
		overSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(player.INVENTORY, overSlotPos)
		self.wndEquip.SetUsableItem(False)
		if mousemodule.mouseController.isAttached():
			attachedItemVID = mousemodule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedItemVID)
			if item.GetItemType(attachedItemVID) == 3 and item.GetItemSubType(attachedItemVID) == item.USE_DS_ENCHANT:
				self.wndEquip.SetUsableItem(True)
		
		self.ShowToolTip(player.INVENTORY, overSlotPos)

	def UseEquipItemSlot(self, slotIndex):
		if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return

		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(player.INVENTORY, slotIndex)

		self.__UseEquipItem(slotIndex)
		mousemodule.mouseController.DeattachObject()
		self.OverOutEquipItem()

	def __UseEquipItem(self, slotIndex):
		if uiprivateshopbuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		self.__OpenQuestionDialog(False, (player.INVENTORY, slotIndex), (1, 1))


	def SelectEquipItemSlot(self, itemSlotIndex):

		## ���콺 ��ư�� sell buy üũ �ؼ� return
		curCursorNum = app.GetCursor()
		if app.SELL == curCursorNum:
			return
		elif app.BUY == curCursorNum:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.SHOP_BUY_INFO)
			return

		if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(player.INVENTORY, itemSlotIndex)

		if mousemodule.mouseController.isAttached():
			attachedSlotType = mousemodule.mouseController.GetAttachedType()
			attachedSlotPos = mousemodule.mouseController.GetAttachedSlotNumber()
			# �ڱ� �ڽ��� �ڱ� �ڽſ��� �巡���ϴ� ���
			if player.SLOT_TYPE_INVENTORY == attachedSlotType and itemSlotIndex == attachedSlotPos:
				mousemodule.mouseController.DeattachObject() #@fixme011
				return

			#@fixme011 BEGIN (enable only the extract items so far)
			attachedItemVID = mousemodule.mouseController.GetAttachedItemIndex()
			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				ITEM_USE = 3
				ITEM_EXTRACT = 31
				item.SelectItem(attachedItemVID)
				if item.GetItemType(attachedItemVID) == ITEM_EXTRACT or\
					item.GetItemType(attachedItemVID) == ITEM_USE and\
					item.GetItemSubType(attachedItemVID) in (item.USE_TIME_CHARGE_PER, item.USE_TIME_CHARGE_FIX):
						net.SendItemUseToItemPacket(attachedInvenType, attachedSlotPos, player.INVENTORY, itemSlotIndex)
			elif attachedSlotType == player.SLOT_TYPE_EXTRA_INVENTORY and app.ENABLE_DS_ENCHANT:
				item.SelectItem(attachedItemVID)
				if item.GetItemType(attachedItemVID) == 3 and item.GetItemSubType(attachedItemVID) == item.USE_DS_ENCHANT:
					net.SendItemUseToItemPacket(attachedInvenType, attachedSlotPos, player.INVENTORY, itemSlotIndex)
			#@fixme011 END

			mousemodule.mouseController.DeattachObject()
		else:
			if app.IsPressed(app.DIK_LALT) and app.ENABLE_BUGFIXES:
				link = player.GetItemLink(player.INVENTORY, itemSlotIndex)
				ime.PasteString(link)
			else:
				selectedItemVNum = player.GetItemIndex(player.INVENTORY, itemSlotIndex)
				itemCount = player.GetItemCount(player.INVENTORY, itemSlotIndex)
				mousemodule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
				self.wndItem.SetUseMode(False)
				snd.PlaySound("sound/ui/pick.wav")

	def SelectEmptyEquipSlot(self, selectedSlot):
		if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(player.INVENTORY, selectedSlot)

		if mousemodule.mouseController.isAttached():
			attachedSlotType = mousemodule.mouseController.GetAttachedType()
			attachedSlotPos = mousemodule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mousemodule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mousemodule.mouseController.GetAttachedItemIndex()

			if player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedSlotType:
				if 0 == player.GetItemMetinSocket(player.DRAGON_SOUL_INVENTORY, attachedSlotPos, 0):
					self.wndPopupDialog.SetText(localeinfo.DRAGON_SOUL_EXPIRED)
					self.wndPopupDialog.Open()
					return

				item.SelectItem(attachedItemIndex)
				subType = item.GetItemSubType()
				if subType != (selectedSlot - player.DRAGON_SOUL_EQUIPMENT_SLOT_START):
					self.wndPopupDialog.SetText(localeinfo.DRAGON_SOUL_UNMATCHED_SLOT)
					self.wndPopupDialog.Open()
				else:
					srcItemPos = (player.DRAGON_SOUL_INVENTORY, attachedSlotPos)
					dstItemPos = (player.INVENTORY, selectedSlotPos)
					self.__OpenQuestionDialog(True, srcItemPos, dstItemPos)

			mousemodule.mouseController.DeattachObject()
	# equip ���� ���� �Լ��� ��.

	# ���â ����
	def __OpenQuestionDialog(self, Equip, srcItemPos, dstItemPos):
		self.srcItemPos = srcItemPos
		self.dstItemPos = dstItemPos

		self.dlgQuestion.SetAcceptEvent(ui.__mem_func__(self.__Accept))
		self.dlgQuestion.SetCancelEvent(ui.__mem_func__(self.__Cancel))

		if Equip:
			self.dlgQuestion.SetText1(localeinfo.DRAGON_SOUL_EQUIP_WARNING1)
			self.dlgQuestion.SetText2(localeinfo.DRAGON_SOUL_EQUIP_WARNING2)
		else:
			self.dlgQuestion.SetText1(localeinfo.DRAGON_SOUL_UNEQUIP_WARNING1)
			self.dlgQuestion.SetText2(localeinfo.DRAGON_SOUL_UNEQUIP_WARNING2)

		self.dlgQuestion.Open()

	def __Accept(self):
		if (-1, -1) == self.dstItemPos:
			net.SendItemUsePacket(*self.srcItemPos)
		else:
			self.__SendMoveItemPacket(*(self.srcItemPos + self.dstItemPos + (0,)))
		self.dlgQuestion.Close()

	def __Cancel(self):
		self.srcItemPos = (0, 0)
		self.dstItemPos = (0, 0)
		self.dlgQuestion.Close()

	# ���â ���� ��

	def SetDSKindIndex(self, kindIndex):
		if self.DSKindIndex != kindIndex:
			self.__HighlightSlot_ClearCurrentPage()

		self.DSKindIndex = kindIndex

		for (tabKey, tabButton) in self.tabButtonDict.items():
			if kindIndex!=tabKey:
				tabButton.SetUp()

		for tabValue in self.tabDict.itervalues():
			tabValue.Hide()

		self.tabDict[kindIndex].Show()
		self.tabText.SetText(DragonSoulWindow.KIND_TAP_TITLES[kindIndex] % self.MAX_VIEWBUTTON_TEXT[self.inventoryPageIndex - 3])

		self.RefreshBagSlotWindow()
		if app.ENABLE_DS_REFINE_ALL:
			global ds_type_page
			ds_type_page = kindIndex

	def SetDeckPage(self, page):
		if page == self.deckPageIndex:
			return

		if self.isActivated:
			self.DeactivateDragonSoul()
			net.SendChatPacket("/dragon_soul deactivate")
		self.deckPageIndex = page
		self.deckTab[page].Down()
		self.deckTab[(page+1)%2].SetUp()

		self.RefreshEquipSlotWindow()

	# ��ȥ�� Ȱ��ȭ ����
	def ActivateDragonSoulByExtern(self, deck):
		self.isActivated = True
		self.activateButton.Down()
		self.deckPageIndex = deck
		self.deckTab[deck].Down()
		self.deckTab[(deck+1)%2].SetUp()
		self.RefreshEquipSlotWindow()

	def DeactivateDragonSoul(self):
		self.isActivated = False
		self.activateButton.SetUp()
		self.RefreshEquipSlotWindow()

	if app.__ENABLE_RANGE_ALCHEMY__:
		def __OpenShopWindow(self):
			net.SendChatPacket("/open_range_npc " + str(51))
			
	if app.__ENABLE_REFINE_ALCHEMY__:
		def __OpenRefineAlchemyWindow(self):
			net.SendChatPacket("/open_refine_window_alchemy ")

	def ActivateButtonClick(self):
		self.isActivated = self.isActivated ^ True
		if self.isActivated:
			if self.__CanActivateDeck():
				net.SendChatPacket("/dragon_soul activate " + str(self.deckPageIndex))
			else:
				self.isActivated = False
				self.activateButton.SetUp()
		else:
			net.SendChatPacket("/dragon_soul deactivate")

	def __CanActivateDeck(self):
		canActiveNum = 0
		for i in xrange(6):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(player.INVENTORY, player.DRAGON_SOUL_EQUIPMENT_SLOT_START + i)
			itemVnum = player.GetItemIndex(slotNumber)

			if itemVnum != 0:
				item.SelectItem(itemVnum)
				isNoLimit = True
				for i in xrange(item.LIMIT_MAX_NUM):
					(limitType, limitValue) = item.GetLimit(i)

					# LIMIT_TIMER_BASED_ON_WEAR�� ����0�� ���� �ð��� �ڴ´�.
					# LIMIT_REAL_TIME�� �ð� �� �Ǹ� �������� ������Ƿ� �� �ʿ䰡 ����.
					# LIMIT_REAL_TIME_START_FIRST_USE�� ������ ����� ���ǵ��� �ʾ� �ϴ� ���д�.
					if item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
						isNoLimit = False
						remain_time = player.GetItemMetinSocket(player.INVENTORY, slotNumber, 0)
						if 0 != remain_time:
							canActiveNum += 1
							break
				# Ÿ�̸Ӱ� ���ٸ� Activate�� �� �ִ� ��ȥ��.
				if isNoLimit:
					canActiveNum += 1

		return canActiveNum > 0

	# Ȱ��ȭ ���� ��

	# ���� highlight ����
	def __HighlightSlot_ClearCurrentPage(self):
		for i in xrange(self.wndItem.GetSlotCount()):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, i)
			if slotNumber in self.listHighlightedSlot:
				self.wndItem.DeactivateSlot(i)
				self.listHighlightedSlot.remove(slotNumber)

	def __HighlightSlot_RefreshCurrentPage(self):
		for i in xrange(self.wndItem.GetSlotCount()):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, i)
			if slotNumber in self.listHighlightedSlot:
				self.wndItem.ActivateSlot(i)

	def HighlightSlot(self, slot):
		if not slot in self.listHighlightedSlot:
			self.listHighlightedSlot.append (slot)
	# ���� highlight ���� ��

	def SetDragonSoulRefineWindow(self, wndDragonSoulRefine):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			from _weakref import proxy
			self.wndDragonSoulRefine = proxy(wndDragonSoulRefine)

## ��ȭ�� �� ���� ��� ������ ����
#class DragonSoulRefineException(Exception):
	#pass

class DragonSoulRefineWindow(ui.ScriptWindow):
	REFINE_TYPE_GRADE, REFINE_TYPE_STEP, REFINE_TYPE_STRENGTH = xrange(3)
	DS_SUB_HEADER_DIC = {
		REFINE_TYPE_GRADE : player.DS_SUB_HEADER_DO_UPGRADE,
		REFINE_TYPE_STEP : player.DS_SUB_HEADER_DO_IMPROVEMENT,
		REFINE_TYPE_STRENGTH : player.DS_SUB_HEADER_DO_REFINE
	}
	REFINE_STONE_SLOT, DRAGON_SOUL_SLOT = xrange(2)

	INVALID_DRAGON_SOUL_INFO = -1

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = None
		self.sellingSlotNumber = -1
		self.isLoaded = 0
		self.refineChoiceButtonDict = None
		self.doRefineButton = None
		if app.ENABLE_DS_REFINE_ALL:
			self.doRefineAllButton = None
			#self.doSafeMode = None
		
		self.wndMoney = None
		self.SetWindowName("DragonSoulRefineWindow")
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		ui.ScriptWindow.Show(self)

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return
		self.isLoaded = 1
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/dragonsoulrefinewindow.py")

		except:
			import exception
			exception.Abort("dragonsoulrefinewindow.LoadWindow.LoadObject")
		try:
			if localeinfo.IsARABIC():
				self.board = self.GetChild("DragonSoulRefineWindowBaseImage")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)

			wndRefineSlot = self.GetChild("RefineSlot")
			wndResultSlot = self.GetChild("ResultSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.refineChoiceButtonDict = {
				self.REFINE_TYPE_GRADE	: self.GetChild("GradeButton"),
				self.REFINE_TYPE_STEP: self.GetChild("StepButton"),
				self.REFINE_TYPE_STRENGTH	: self.GetChild("StrengthButton"),
			}
			self.doRefineButton = self.GetChild("DoRefineButton")
			if app.ENABLE_DS_REFINE_ALL:
				self.doRefineAllButton = self.GetChild("DoRefineAllButton")
				#self.doSafeMode = ui.CheckBox()
				#self.doSafeMode.SetParent(self)
				#self.doSafeMode.SetPosition(10, 203)
				#self.doSafeMode.SetIndex(5)
				##self.doSafeMode.SetWindowHorizontalAlignCenter()
				#import systemSetting
				#if systemSetting.GetBiologistAlert() == True:
				#	self.doSafeMode.OnMouseLeftButtonUp()
				#self.doSafeMode.Show()
			
			self.wndMoney = self.GetChild("Money_Slot")

		except:
			import exception
			exception.Abort("DragonSoulRefineWindow.LoadWindow.BindObject")


		## Item Slots
		wndRefineSlot.SetOverInItemEvent(ui.__mem_func__(self.__OverInRefineItem))
		wndRefineSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutItem))
		wndRefineSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__SelectRefineEmptySlot))
		wndRefineSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectRefineItemSlot))
		wndRefineSlot.SetUseSlotEvent(ui.__mem_func__(self.__SelectRefineItemSlot))
		wndRefineSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.__SelectRefineItemSlot))

		wndResultSlot.SetOverInItemEvent(ui.__mem_func__(self.__OverInResultItem))
		wndResultSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutItem))
		self.wndRefineSlot = wndRefineSlot
		self.wndResultSlot = wndResultSlot

		## Button
		self.refineChoiceButtonDict[self.REFINE_TYPE_GRADE].SetToggleDownEvent(self.__ToggleDownGradeButton)
		self.refineChoiceButtonDict[self.REFINE_TYPE_STEP].SetToggleDownEvent(self.__ToggleDownStepButton)
		self.refineChoiceButtonDict[self.REFINE_TYPE_STRENGTH].SetToggleDownEvent(self.__ToggleDownStrengthButton)
		self.refineChoiceButtonDict[self.REFINE_TYPE_GRADE].SetToggleUpEvent(lambda : self.__ToggleUpButton(self.REFINE_TYPE_GRADE))
		self.refineChoiceButtonDict[self.REFINE_TYPE_STEP].SetToggleUpEvent(lambda : self.__ToggleUpButton(self.REFINE_TYPE_STEP))
		self.refineChoiceButtonDict[self.REFINE_TYPE_STRENGTH].SetToggleUpEvent(lambda : self.__ToggleUpButton(self.REFINE_TYPE_STRENGTH))
		self.doRefineButton.SetEvent(self.__PressDoRefineButton)
		if app.ENABLE_DS_REFINE_ALL:
			self.doRefineAllButton.SetEvent(self.__PressDoRefineAllButton)

		## Dialog
		self.wndPopupDialog = uicommon.PopupDialog()

		self.currentRefineType = self.REFINE_TYPE_GRADE
		self.refineItemInfo = {}
		self.resultItemInfo = {}
		self.currentRecipe = {}

		self.wndMoney.SetText(localeinfo.NumberToMoneyString(0))
		self.refineChoiceButtonDict[self.REFINE_TYPE_GRADE].Down()

		self.__Initialize()

	def Destroy(self):
		self.ClearDictionary()
		self.tooltipItem = None
		self.wndItem = 0
		self.wndEquip = 0
		self.activateButton = 0
		if app.__ENABLE_RANGE_ALCHEMY__:
			self.shopButton = 0
		self.questionDialog = None
		self.mallButton = None
		self.inventoryTab = []
		self.deckTab = []
		self.equipmentTab = []
		self.tabDict = None
		self.tabButtonDict = None

	def Close(self):
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.__FlushRefineItemSlot()
		player.SendDragonSoulRefine(player.DRAGON_SOUL_REFINE_CLOSE)
		self.Hide()

	def Show(self):
		self.currentRefineType = self.REFINE_TYPE_GRADE
		self.wndMoney.SetText(localeinfo.NumberToMoneyString(0))
		self.refineChoiceButtonDict[self.REFINE_TYPE_GRADE].Down()
		self.refineChoiceButtonDict[self.REFINE_TYPE_STEP].SetUp()
		self.refineChoiceButtonDict[self.REFINE_TYPE_STRENGTH].SetUp()

		self.Refresh()

		ui.ScriptWindow.Show(self)

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	# ��ư ���� �ִ� ���¸� ������ ��� ��ȭâ ���� �������� �ʱ�ȭ.
	def __Initialize(self):
		self.currentRecipe = {}
		self.refineItemInfo = {}
		self.resultItemInfo = {}

		if self.REFINE_TYPE_STRENGTH == self.currentRefineType:
			self.refineSlotLockStartIndex = 2
		else:
			self.refineSlotLockStartIndex = 1

		for i in xrange(self.refineSlotLockStartIndex):
			self.wndRefineSlot.HideSlotBaseImage(i)

		self.wndMoney.SetText(localeinfo.NumberToMoneyString(0))

	def __FlushRefineItemSlot(self):
		## Item slot settings
		# ���� �κ��� ������ ī��Ʈ ȸ��
		for invenType, invenPos, itemCount in self.refineItemInfo.values():
			remainCount = player.GetItemCount(invenType, invenPos)
			player.SetItemCount(invenType, invenPos, remainCount + itemCount)
		self.__Initialize()

	def __ToggleUpButton(self, idx):
		#if self.REFINE_TYPE_GRADE == self.currentRefineType:
		self.refineChoiceButtonDict[idx].Down()

	def __ToggleDownGradeButton(self):
		if self.REFINE_TYPE_GRADE == self.currentRefineType:
			return
		
		self.refineChoiceButtonDict[self.currentRefineType].SetUp()
		self.currentRefineType = self.REFINE_TYPE_GRADE
		self.__FlushRefineItemSlot()
		self.Refresh()

	def __ToggleDownStepButton(self):
		if self.REFINE_TYPE_STEP == self.currentRefineType:
			return
		self.refineChoiceButtonDict[self.currentRefineType].SetUp()
		self.currentRefineType = self.REFINE_TYPE_STEP
		self.__FlushRefineItemSlot()
		self.Refresh()

	def __ToggleDownStrengthButton(self):
		if self.REFINE_TYPE_STRENGTH == self.currentRefineType:
			return
		self.refineChoiceButtonDict[self.currentRefineType].SetUp()
		self.currentRefineType = self.REFINE_TYPE_STRENGTH
		self.__FlushRefineItemSlot()
		self.Refresh()

	def __PopUp(self, message):
		self.wndPopupDialog.SetText(message)
		self.wndPopupDialog.Open()

	def __SetItem(self, inven, dstSlotIndex, itemCount):
		invenType, invenPos = inven

		if dstSlotIndex >= self.refineSlotLockStartIndex:
			return False

		itemVnum = player.GetItemIndex(invenType, invenPos)
		maxCount = player.GetItemCount(invenType, invenPos)

		if itemCount > maxCount:
			raise Exception, ("Invalid attachedItemCount(%d). (base pos (%d, %d), base itemCount(%d))" % (itemCount, invenType, invenPos, maxCount))
			#return False

		# strength ��ȭ�� ���, 0���� ��ȭ��, 1���� ��ȥ���� ������ ������.
		if DragonSoulRefineWindow.REFINE_TYPE_STRENGTH == self.currentRefineType:
			if self.__IsDragonSoul(itemVnum):
				dstSlotIndex = 1
			else:
				dstSlotIndex = 0

		# �� �����̾����.
		if dstSlotIndex in self.refineItemInfo:
			return False

		# ��ȭâ�� �ø� �� �ִ� ���������� �˻�.
		if False == self.__CheckCanRefine(itemVnum):
			return False

		# ����� ���� ������ ī��Ʈ��ŭ ���� �ڸ��� ������ ī��Ʈ ����
		player.SetItemCount(invenType, invenPos, maxCount - itemCount)
		self.refineItemInfo[dstSlotIndex] = (invenType, invenPos, itemCount)
		self.Refresh()

		return True

	# ��ȭ ������ ���������� üũ
	# ��ȥ�� ��ȭ�� ��ȭ �����Ǹ� ���س��� �����ϴ� ���� �ƴ϶�,
	# ó���� ��ȭâ�� �ø� ��ȥ���� ���� ��ȭ �����ǰ� �����ȴ�.
	# �׷��� __CanRefineGrade, __CanRefineStep, __CanRefineStrength �Լ�����
	# ��ȭ �����ǰ� ���ٸ�(ó�� �ø��� �������̶��), ��ȭ �����Ǹ� �������ִ� ���ҵ� �Ѵ�.
	def __CheckCanRefine(self, vnum):
		if self.REFINE_TYPE_GRADE == self.currentRefineType:
			return self.__CanRefineGrade(vnum)

		elif self.REFINE_TYPE_STEP == self.currentRefineType:
			return self.__CanRefineStep(vnum)

		elif self.REFINE_TYPE_STRENGTH == self.currentRefineType:
			return self.__CanRefineStrength(vnum)

		else:
			return False

	def __CanRefineGrade(self, vnum):
		ds_info = self.__GetDragonSoulTypeInfo(vnum)

		if DragonSoulRefineWindow.INVALID_DRAGON_SOUL_INFO == ds_info:
			self.__PopUp(localeinfo.DRAGON_SOUL_IS_NOT_DRAGON_SOUL)
			return False

		if self.currentRecipe:
			ds_type, grade, step, strength = ds_info
			cur_refine_ds_type, cur_refine_grade, cur_refine_step, cur_refine_strength = self.currentRecipe["ds_info"]
			if not (cur_refine_ds_type == ds_type and cur_refine_grade == grade):
				self.__PopUp(localeinfo.DRAGON_SOUL_INVALID_DRAGON_SOUL)
				return False
		# ��ȭ â�� ó�� �������� �ø��� ���, ��ȭ ��ῡ ���� ������ ����.
		# ��ȥ�� ��ȭ��, �����Ǹ� ������ �����ϴ� ���� �ƴ϶�, ��ȭâ�� ó�� �ø��� �������� �����̳Ŀ� ����,
		# ������ ��ȭ�ϰ�, ��ᰡ ��������(���� ������)�� ��������.
		# �����ǰ� ���ٸ�, ó�� �ø� �������̶� �����ϰ�, vnum�� �������� �����Ǹ� ����.
		else:
			self.currentRecipe = self.__GetRefineGradeRecipe(vnum)

			if self.currentRecipe:
				self.refineSlotLockStartIndex = self.currentRecipe["need_count"]
				self.wndMoney.SetText(localeinfo.NumberToMoneyString(self.currentRecipe["fee"]))
				return True
			else:
			# ��ȭ ���� ���ÿ� �����ϸ� �ø� �� ���� ���������� �Ǵ�.
				self.__PopUp(localeinfo.DRAGON_SOUL_CANNOT_REFINE)
				return False

	def __CanRefineStep (self, vnum):
		ds_info = self.__GetDragonSoulTypeInfo(vnum)

		if DragonSoulRefineWindow.INVALID_DRAGON_SOUL_INFO == ds_info:
			self.__PopUp(localeinfo.DRAGON_SOUL_IS_NOT_DRAGON_SOUL)
			return False

		if self.currentRecipe:
			ds_type, grade, step, strength = ds_info
			cur_refine_ds_type, cur_refine_grade, cur_refine_step, cur_refine_strength = self.currentRecipe["ds_info"]
			if not (cur_refine_ds_type == ds_type and cur_refine_grade == grade and cur_refine_step == step):
				self.__PopUp(localeinfo.DRAGON_SOUL_INVALID_DRAGON_SOUL)
				return False
		# ��ȭ â�� ó�� �������� �ø��� ���, ��ῡ ���� ������ ����.
		# ��ȥ�� ��ȭ��, �����Ǹ� ������ �����ϴ� ���� �ƴ϶�, ��ȭâ�� ó�� �ø��� �������� �����̳Ŀ� ����,
		# ������ ��ȭ�ϰ�, ��ᰡ ��������(���� ������)�� ��������.
		# �����ǰ� ���ٸ�, ó�� �ø� �������̶� �����ϰ�, vnum�� �������� �����Ǹ� ����.
		else:
			self.currentRecipe = self.__GetRefineStepRecipe(vnum)

			if self.currentRecipe:
				self.refineSlotLockStartIndex = self.currentRecipe["need_count"]
				self.wndMoney.SetText(localeinfo.NumberToMoneyString(self.currentRecipe["fee"]))
				return True

			else:
			# ��ȭ ���� ���ÿ� �����ϸ� �ø� �� ���� ���������� �Ǵ�.
				self.__PopUp(localeinfo.DRAGON_SOUL_CANNOT_REFINE)
				return False

	def __CanRefineStrength (self, vnum):
		# ��ȥ���� ���, �� �̻� strength ��ȭ�� �� �� ������ üũ�ؾ���.
		if self.__IsDragonSoul(vnum):
			ds_type, grade, step, strength = self.__GetDragonSoulTypeInfo(vnum)

			import dragon_soul_refine_settings
			if strength >= dragon_soul_refine_settings.dragon_soul_refine_info[ds_type]["strength_max_table"][grade][step]:
				self.__PopUp(localeinfo.DRAGON_SOUL_CANNOT_REFINE_MORE)
				return False

			else:
				return True

		# strength ��ȭ�� ���, refine_recipe�� ��ȥ���� ������ �ƴ�, ��ȭ���� ������ ���� �޶�����.
		# ���� ��ȥ���� �ƴ϶��,
		# �̹� �����ǰ� �ִ� ����, ��ȭ���� ��ȭâ�� �ִٴ� ���̹Ƿ�, return False
		# �����ǰ� ���� ����, ��ȭ������ Ȯ���ϰ�, �����Ǹ� �����Ѵ�.
		else:
			if self.currentRecipe:
				self.__PopUp(localeinfo.DRAGON_SOUL_IS_NOT_DRAGON_SOUL)
				return False
			else:
				refineRecipe = self.__GetRefineStrengthInfo(vnum)
				if refineRecipe:
					self.currentRecipe = refineRecipe
					self.wndMoney.SetText(localeinfo.NumberToMoneyString(self.currentRecipe["fee"]))
					return True
				else:
				# �����Ǹ� ������ �� ���� ���
					self.__PopUp(localeinfo.DRAGON_SOUL_NOT_DRAGON_SOUL_REFINE_STONE)
					return False

	def __GetRefineGradeRecipe (self, vnum):
		ds_type, grade, step, strength = self.__GetDragonSoulTypeInfo(vnum)
		try:
			import dragon_soul_refine_settings

			return	{
				"ds_info"		: (ds_type, grade, step, strength),
				"need_count"	: dragon_soul_refine_settings.dragon_soul_refine_info[ds_type]["grade_need_count"][grade],
				"fee"			: dragon_soul_refine_settings.dragon_soul_refine_info[ds_type]["grade_fee"][grade]
					}
		except:
			return None

	def __GetRefineStepRecipe (self, vnum):
		ds_type, grade, step, strength = self.__GetDragonSoulTypeInfo(vnum)
		try:
			import dragon_soul_refine_settings

			return	{
				"ds_info"		: (ds_type, grade, step, strength),
				"need_count"	: dragon_soul_refine_settings.dragon_soul_refine_info[ds_type]["step_need_count"][step],
				"fee"			: dragon_soul_refine_settings.dragon_soul_refine_info[ds_type]["step_fee"][step]
					}
		except:
			return None

	# strength ��ȭ�� ���, refineInfo�� ��ȭ���� ���� �޶�����.
	def __GetRefineStrengthInfo (self, itemVnum):
		try:
			# �̳��� ��ġ�� ��������....
			# ��ȭ���� �ƴϸ� �ȵ�.
			item.SelectItem(itemVnum)
			if not (item.ITEM_TYPE_MATERIAL == item.GetItemType() \
					and (item.MATERIAL_DS_REFINE_NORMAL <= item.GetItemSubType() and item.GetItemSubType() <= item.MATERIAL_DS_REFINE_HOLLY)):
				return None

			import dragon_soul_refine_settings
			return { "fee" : dragon_soul_refine_settings.strength_fee[item.GetItemSubType()] }
		except:
			return None

	def __IsDragonSoul(self, vnum):
		item.SelectItem(vnum)
		return item.GetItemType() == item.ITEM_TYPE_DS

	# ��ȥ�� Vnum�� ���� comment
	# ITEM VNUM�� 10�� �ڸ�����, FEDCBA��� �Ѵٸ�
	# FE : ��ȥ�� ����.	D : ���
	# C : �ܰ�			B : ��ȭ
	# A : ������ ��ȣ��...
	def __GetDragonSoulTypeInfo(self, vnum):
		if not self.__IsDragonSoul(vnum):
			return DragonSoulRefineWindow.INVALID_DRAGON_SOUL_INFO
		ds_type = vnum / 10000
		grade = vnum % 10000 /1000
		step = vnum % 1000 / 100
		strength = vnum % 100 / 10

		return (ds_type, grade, step, strength)

	def __MakeDragonSoulVnum(self, ds_type, grade, step, strength):
		return ds_type * 10000 + grade * 1000 + step * 100 + strength * 10

	## �� ���� ���� Event
	def __SelectRefineEmptySlot(self, selectedSlotPos):
		try:
			if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
				return

			if selectedSlotPos >= self.refineSlotLockStartIndex:
				return

			if mousemodule.mouseController.isAttached():
				attachedSlotType = mousemodule.mouseController.GetAttachedType()
				attachedSlotPos = mousemodule.mouseController.GetAttachedSlotNumber()
				attachedItemCount = mousemodule.mouseController.GetAttachedItemCount()
				attachedItemIndex = mousemodule.mouseController.GetAttachedItemIndex()
				mousemodule.mouseController.DeattachObject()

				if uiprivateshopbuilder.IsBuildingPrivateShop():
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
					return

				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)

				if app.ENABLE_EXTRA_INVENTORY:
					if player.INVENTORY == attachedInvenType and player.EXTRA_INVENTORY == attachedInvenType and player.IsEquipmentSlot(attachedSlotPos):
						return
				else:
					if player.INVENTORY == attachedInvenType and player.IsEquipmentSlot(attachedSlotPos):
						return

				if app.ENABLE_EXTRA_INVENTORY:
					if attachedInvenType != player.INVENTORY and attachedInvenType != player.DRAGON_SOUL_INVENTORY and attachedInvenType != player.EXTRA_INVENTORY:
						return
				else:
					if player.INVENTORY != attachedInvenType and player.DRAGON_SOUL_INVENTORY != attachedInvenType:
						return

				if True == self.__SetItem((attachedInvenType, attachedSlotPos), selectedSlotPos, attachedItemCount):
					self.Refresh()

		except Exception, e:
			import dbg
			dbg.TraceError("Exception : __SelectRefineEmptySlot, %s" % e)

	# Ŭ������ ���Կ��� ����.
	def __SelectRefineItemSlot(self, selectedSlotPos):
		if constinfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		try:
			if not selectedSlotPos in self.refineItemInfo:
				# ���ο� �������� ��ȭâ�� �ø��� �۾�.
				if mousemodule.mouseController.isAttached():
					attachedSlotType = mousemodule.mouseController.GetAttachedType()
					attachedSlotPos = mousemodule.mouseController.GetAttachedSlotNumber()
					attachedItemCount = mousemodule.mouseController.GetAttachedItemCount()
					attachedItemIndex = mousemodule.mouseController.GetAttachedItemIndex()
					mousemodule.mouseController.DeattachObject()

					if uiprivateshopbuilder.IsBuildingPrivateShop():
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
						return

					attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)

					if app.ENABLE_EXTRA_INVENTORY:
						if player.INVENTORY == attachedInvenType and player.EXTRA_INVENTORY == attachedInvenType and player.IsEquipmentSlot(attachedSlotPos):
							return

						if player.INVENTORY != attachedInvenType and player.EXTRA_INVENTORY != attachedInvenType and player.DRAGON_SOUL_INVENTORY != attachedInvenType:
							return
					else:
						if player.INVENTORY == attachedInvenType and player.IsEquipmentSlot(attachedSlotPos):
							return

						if player.INVENTORY != attachedInvenType and player.DRAGON_SOUL_INVENTORY != attachedInvenType:
							return

					self.AutoSetItem((attachedInvenType, attachedSlotPos), 1)
				return
			elif mousemodule.mouseController.isAttached():
				return

			attachedInvenType, attachedSlotPos, attachedItemCount = self.refineItemInfo[selectedSlotPos]
			selectedItemVnum = player.GetItemIndex(attachedInvenType, attachedSlotPos)

			# ��ȭâ���� ���� �� ���� �κ��� ������ ī��Ʈ ȸ��
			invenType, invenPos, itemCount = self.refineItemInfo[selectedSlotPos]
			remainCount = player.GetItemCount(invenType, invenPos)
			player.SetItemCount(invenType, invenPos, remainCount + itemCount)
			del self.refineItemInfo[selectedSlotPos]

			# ��ȭâ�� ����ٸ�, �ʱ�ȭ
			if not self.refineItemInfo:
				self.__Initialize()
			else:
				item.SelectItem(selectedItemVnum)
				# ���� �������� ��ȭ���̾��ٸ� ��ȭ ���ǽ� �ʱ�ȭ
				if (item.ITEM_TYPE_MATERIAL == item.GetItemType() \
					and (item.MATERIAL_DS_REFINE_NORMAL <= item.GetItemSubType() and item.GetItemSubType() <= item.MATERIAL_DS_REFINE_HOLLY)):
					self.currentRecipe = {}
					self.wndMoney.SetText(localeinfo.NumberToMoneyString(0))
				# ��ȥ���̾��ٸ�,
				# strength��ȭ�� �ƴ� ���, ��ȭâ�� �ٸ� ��ȥ���� ���������Ƿ�, �����Ǹ� �ʱ�ȭ�ϸ� �ȵ�.
				# strength��ȭ�� ���, ��ȭ �����Ǵ� ��ȭ���� ���ӵ� ���̹Ƿ� �ٸ� ó���� �ʿ䰡 ����.
				else:
					pass

		except Exception, e:
			import dbg
			dbg.TraceError("Exception : __SelectRefineItemSlot, %s" % e)

		self.Refresh()

	def __OverInRefineItem(self, slotIndex):
		if self.refineItemInfo.has_key(slotIndex):
			inven_type, inven_pos, item_count = self.refineItemInfo[slotIndex]
			self.tooltipItem.SetInventoryItem(inven_pos, inven_type)

	def __OverInResultItem(self, slotIndex):
		if self.resultItemInfo.has_key(slotIndex):
			inven_type, inven_pos, item_count = self.resultItemInfo[slotIndex]
			self.tooltipItem.SetInventoryItem(inven_pos, inven_type)

	def __OverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def __PressDoRefineButton(self):
		for i in xrange(self.refineSlotLockStartIndex):
			if not i in self.refineItemInfo:
				self.wndPopupDialog.SetText(localeinfo.DRAGON_SOUL_NOT_ENOUGH_MATERIAL)
				self.wndPopupDialog.Open()

				return

		player.SendDragonSoulRefine(DragonSoulRefineWindow.DS_SUB_HEADER_DIC[self.currentRefineType], self.refineItemInfo)

	if app.ENABLE_DS_REFINE_ALL:
		def __PressDoRefineAllButton(self):
			global ds_type_page
			global ds_grade_page
			player.SendDragonSoulRefineAll(DragonSoulRefineWindow.DS_SUB_HEADER_DIC[self.currentRefineType], ds_type_page, ds_grade_page)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Refresh(self):
		if app.ENABLE_DS_REFINE_ALL:
			if self.currentRefineType == self.REFINE_TYPE_STRENGTH or self.currentRefineType == self.REFINE_TYPE_STEP:
				#self.doSafeMode.Hide()
				self.doRefineAllButton.Hide()
				self.doRefineButton.SetPosition(188, 200)
			else:
				#self.doSafeMode.Show()
				self.doRefineButton.SetPosition(98, 200)
				self.doRefineAllButton.SetPosition(188, 200)
				self.doRefineAllButton.Show()
		
		self.__RefreshRefineItemSlot()
		self.__ClearResultItemSlot()

	def __RefreshRefineItemSlot(self):
		try:
			for slotPos in xrange(self.wndRefineSlot.GetSlotCount()):
				self.wndRefineSlot.ClearSlot(slotPos)
				if slotPos < self.refineSlotLockStartIndex:
					# self.refineItemInfo[slotPos]�� ����Ȯ��
					# (������ �������� �����ϴ��� Ȯ��)
					# ���� -> ������ �������� ���Կ� ����.
					# ������ -> �������� �����Ƿ� ��ȭâ���� ����.
					if slotPos in self.refineItemInfo:
						invenType, invenPos, itemCount = self.refineItemInfo[slotPos]
						itemVnum = player.GetItemIndex(invenType, invenPos)

						# if itemVnum:
						if itemVnum:
							self.wndRefineSlot.SetItemSlot(slotPos, player.GetItemIndex(invenType, invenPos), itemCount)
						else:
							del self.refineItemInfo[slotPos]

					# �� ���Կ� reference �������� alpha 0.5�� ����.
					if not slotPos in self.refineItemInfo:
						try:
							reference_vnum = 0
							# strength ��ȭ�� ����,
							# 0�� ���Կ� ��ȭ����, 1�� ���Կ� ��ȥ���� ���´�.
							if DragonSoulRefineWindow.REFINE_TYPE_STRENGTH == self.currentRefineType:
								if DragonSoulRefineWindow.REFINE_STONE_SLOT == slotPos:
									reference_vnum = 100300
							else:
								reference_vnum = self.__MakeDragonSoulVnum(*self.currentRecipe["ds_info"])
							if 0 != reference_vnum:
								item.SelectItem(reference_vnum)
								itemIcon = item.GetIconImage()
								(width, height) = item.GetItemSize()
								self.wndRefineSlot.SetSlot(slotPos, 0, width, height, itemIcon, (1.0, 1.0, 1.0, 0.5))
								# slot ���� �ϴܿ� ���� �߸� �� ����...
								self.wndRefineSlot.SetSlotCount(slotPos, 0)
						except:
							pass
					# refineSlotLockStartIndex ���� ���� ������ ���� �̹����� �����ָ� �ȵ�.
					self.wndRefineSlot.HideSlotBaseImage(slotPos)
				# slotPos >= self.refineSlotLockStartIndex:
				else:
					# �������� ����� �� if���� �� ���� ��������,
					# (���ʿ� �ε����� refineSlotLockStartIndex �̻��� ���Կ��� �������� ���� ���ϰ� �߱� ����)
					# Ȥ�� �� ������ �����.
					if slotPos in self.refineItemInfo:
						invenType, invenPos, itemCount = self.refineItemInfo[slotPos]
						remainCount = player.GetItemCount(invenType, invenPos)
						player.SetItemCount(invenType, invenPos, remainCount + itemCount)
						del self.refineItemInfo[slotPos]
					# refineSlotLockStartIndex �̻��� ������ ���� �̹����� ���������.
					self.wndRefineSlot.ShowSlotBaseImage(slotPos)

			# ��ȭâ�� �ƹ��� �������� ���ٸ�, �ʱ�ȭ����.
			# ������ �߰� �߰��� "del self.refineItemInfo[slotPos]"�� �߱� ������,
			# ���⼭ �ѹ� üũ�������.
			if not self.refineItemInfo:
				self.__Initialize()

			self.wndRefineSlot.RefreshSlot()
		except Exception, e:
			import dbg
			dbg.TraceError("Exception : __RefreshRefineItemSlot, %s" % e)

	def __GetEmptySlot(self, itemVnum = 0):
		# STRENGTH ��ȭ�� ���, ��ȥ�� ���԰� ��ȭ�� ������ ���еǾ��ֱ� ������
		# vnum�� �˾ƾ� �Ѵ�.
		if DragonSoulRefineWindow.REFINE_TYPE_STRENGTH == self.currentRefineType:
			if 0 == itemVnum:
				return -1

			if self.__IsDragonSoul(itemVnum):
				if not DragonSoulRefineWindow.DRAGON_SOUL_SLOT in self.refineItemInfo:
					return DragonSoulRefineWindow.DRAGON_SOUL_SLOT
			else:
				if not DragonSoulRefineWindow.REFINE_STONE_SLOT in self.refineItemInfo:
					return DragonSoulRefineWindow.REFINE_STONE_SLOT
		else:
			for slotPos in xrange(self.wndRefineSlot.GetSlotCount()):
				if not slotPos in self.refineItemInfo:
					return slotPos

		return -1

	def AutoSetItem(self, inven, itemCount):
		invenType, invenPos = inven
		itemVnum = player.GetItemIndex(invenType, invenPos)
		emptySlot = self.__GetEmptySlot(itemVnum)
		if -1 == emptySlot:
			return

		self.__SetItem((invenType, invenPos), emptySlot, itemCount)

	def __ClearResultItemSlot(self):
		self.wndResultSlot.ClearSlot(0)
		self.resultItemInfo = {}

	def RefineSucceed(self, inven_type, inven_pos):
		self.__Initialize()
		self.Refresh()

		itemCount = player.GetItemCount(inven_type, inven_pos)
		if itemCount > 0:
			self.resultItemInfo[0] = (inven_type, inven_pos, itemCount)
			self.wndResultSlot.SetItemSlot(0, player.GetItemIndex(inven_type, inven_pos), itemCount)

	def	RefineFail(self, reason, inven_type, inven_pos):
		if net.DS_SUB_HEADER_REFINE_FAIL == reason:
			self.__Initialize()
			self.Refresh()
			itemCount = player.GetItemCount(inven_type, inven_pos)
			if itemCount > 0:
				self.resultItemInfo[0] = (inven_type, inven_pos, itemCount)
				self.wndResultSlot.SetItemSlot(0, player.GetItemIndex(inven_type, inven_pos), itemCount)
		else:
			self.Refresh()

	def SetInventoryWindows(self, wndInventory, wndDragonSoul):
		self.wndInventory = wndInventory
		self.wndDragonSoul = wndDragonSoul
