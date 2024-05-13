#include "stdafx.h"
#include "constants.h"
#include "item.h"
#include "item_manager.h"
#include "unique_item.h"
#include "packet.h"
#include "desc.h"
#include "char.h"
#include "dragon_soul_table.h"
#include "log.h"
#include "DragonSoul.h"
#include <boost/lexical_cast.hpp>

template <typename T> T MINMAX(T min, T value, T max)
{
	T tv;

	tv = (min > value ? min : value);
	return (max < tv) ? max : tv;
}

typedef std::vector <std::string> TTokenVector;

int Gamble(std::vector<float>& vec_probs)
{
	float range = 0.f;
	for (size_t i = 0; i < vec_probs.size(); i++)
	{
		range += vec_probs[i];
	}
	float fProb = fnumber(0.f, range);
	float sum = 0.f;
	for (size_t idx = 0; idx < vec_probs.size(); idx++)
	{
		sum += vec_probs[idx];
		if (sum >= fProb)
			return idx;
	}
	return -1;
}

// ����ġ ���̺�(prob_lst)�� �޾� random_set.size()���� index�� �����Ͽ� random_set�� return
bool MakeDistinctRandomNumberSet(std::list <float> prob_lst, OUT std::vector<int>& random_set)
{
	int size = prob_lst.size();
	int n = random_set.size();
	if (size < n)
		return false;

	std::vector <int> select_bit(size, 0);
	for (int i = 0; i < n; i++)
	{
		float range = 0.f;
		for (std::list <float>::iterator it = prob_lst.begin(); it != prob_lst.end(); it++)
		{
			range += *it;
		}
		float r = fnumber (0.f, range);
		float sum = 0.f;
		int idx = 0;
		for (std::list <float>::iterator it = prob_lst.begin(); it != prob_lst.end(); it++)
		{
			while (select_bit[idx++]);

			sum += *it;
			if (sum >= r)
			{
				select_bit[idx - 1] = 1;
				random_set[i] = idx - 1;
				prob_lst.erase(it);
				break;
			}
		}
	}
	return true;
}

/* ��ȥ�� Vnum�� ���� comment
 * ITEM VNUM�� 10�� �ڸ�����, FEDCBA��� �Ѵٸ�
 * FE : ��ȥ�� ����.	D : ���
 * C : �ܰ�			B : ��ȭ
 * A : ������ ��ȣ��...
 */

BYTE GetType(DWORD dwVnum)
{
	return (dwVnum / 10000);
}

BYTE GetGradeIdx(DWORD dwVnum)
{
	return (dwVnum / 1000) % 10;
}

BYTE GetStepIdx(DWORD dwVnum)
{
	return (dwVnum / 100) % 10;
}

BYTE GetStrengthIdx(DWORD dwVnum)
{
	return (dwVnum / 10) % 10;
}

bool DSManager::ReadDragonSoulTableFile(const char * c_pszFileName)
{
	m_pTable = new DragonSoulTable();
	return m_pTable->ReadDragonSoulTableFile(c_pszFileName);
}

void DSManager::GetDragonSoulInfo(DWORD dwVnum, BYTE& bType, BYTE& bGrade, BYTE& bStep, BYTE& bStrength) const
{
	bType = GetType(dwVnum);
	bGrade = GetGradeIdx(dwVnum);
	bStep = GetStepIdx(dwVnum);
	bStrength = GetStrengthIdx(dwVnum);
}

bool DSManager::IsValidCellForThisItem(const LPITEM pItem, const TItemPos& Cell) const
{
	if (NULL == pItem)
		return false;

	WORD wBaseCell = GetBasePosition(pItem);
	if (WORD_MAX == wBaseCell)
		return false;

	if (Cell.window_type != DRAGON_SOUL_INVENTORY
		|| (Cell.cell < wBaseCell || Cell.cell >= wBaseCell + DRAGON_SOUL_BOX_SIZE))
	{
		return false;
	}
	else
		return true;

}

WORD DSManager::GetBasePosition(const LPITEM pItem) const
{
	if (NULL == pItem)
		return WORD_MAX;

	BYTE type, grade_idx, step_idx, strength_idx;
	GetDragonSoulInfo(pItem->GetVnum(), type, grade_idx, step_idx, strength_idx);

	BYTE col_type = pItem->GetSubType();
	BYTE row_type = grade_idx;
	if (row_type > DRAGON_SOUL_GRADE_MAX)
		return WORD_MAX;

#ifdef ENABLE_DS_GRADE_MYTH
	return 300 + (col_type * DRAGON_SOUL_GRADE_MAX * DRAGON_SOUL_BOX_SIZE + row_type * DRAGON_SOUL_BOX_SIZE);
#else
	return 300 + (col_type * DRAGON_SOUL_STEP_MAX * DRAGON_SOUL_BOX_SIZE + row_type * DRAGON_SOUL_BOX_SIZE);
#endif
}

bool DSManager::RefreshItemAttributes(LPITEM pDS)
{
	if (!pDS->IsDragonSoul())
	{
		sys_err ("This item(ID : %d) is not DragonSoul.", pDS->GetID());
		return false;
	}

	BYTE ds_type, grade_idx, step_idx, strength_idx;
	GetDragonSoulInfo(pDS->GetVnum(), ds_type, grade_idx, step_idx, strength_idx);

	DragonSoulTable::TVecApplys vec_basic_applys;
	DragonSoulTable::TVecApplys vec_addtional_applys;

	if (!m_pTable->GetBasicApplys(ds_type, vec_basic_applys))
	{
		sys_err ("There is no BasicApply about %d type dragon soul.", ds_type);
		return false;
	}

	if (!m_pTable->GetAdditionalApplys(ds_type, vec_addtional_applys))
	{
		sys_err ("There is no AdditionalApply about %d type dragon soul.", ds_type);
		return false;
	}

	// add_min�� add_max�� ���̷� ����.
	int basic_apply_num, add_min, add_max;
	if (!m_pTable->GetApplyNumSettings(ds_type, grade_idx, basic_apply_num, add_min, add_max))
	{
		sys_err ("In ApplyNumSettings, INVALID VALUES Group type(%d), GRADE idx(%d)", ds_type, grade_idx);
		return false;
	}

	float fWeight = 0.f;
	if (!m_pTable->GetWeight(ds_type, grade_idx, step_idx, strength_idx, fWeight))
	{
		return false;
	}
	fWeight /= 100.f;

	int n = MIN(basic_apply_num, vec_basic_applys.size());
	for (int i = 0; i < n; i++)
	{
		const SApply& basic_apply = vec_basic_applys[i];
		BYTE bType = basic_apply.apply_type;
		short sValue = (short)(ceil((float)basic_apply.apply_value * fWeight - 0.01f));

		pDS->SetForceAttribute(i, bType, sValue);
	}

	for (int i = DRAGON_SOUL_ADDITIONAL_ATTR_START_IDX; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
	{
		BYTE bType = pDS->GetAttributeType(i);
		short sValue = 0;
		if (APPLY_NONE == bType)
			continue;
		for (size_t j = 0; j < vec_addtional_applys.size(); j++)
		{
			if (vec_addtional_applys[j].apply_type == bType)
			{
				sValue = vec_addtional_applys[j].apply_value;
				break;
			}
		}
		pDS->SetForceAttribute(i, bType, (short)(ceil((float)sValue * fWeight - 0.01f)));
	}
	return true;
}

bool DSManager::PutAttributes(LPITEM pDS)
{
	if (!pDS->IsDragonSoul())
	{
		sys_err ("This item(ID : %d) is not DragonSoul.", pDS->GetID());
		return false;
	}

	BYTE ds_type, grade_idx, step_idx, strength_idx;
	GetDragonSoulInfo(pDS->GetVnum(), ds_type, grade_idx, step_idx, strength_idx);

	DragonSoulTable::TVecApplys vec_basic_applys;
	DragonSoulTable::TVecApplys vec_addtional_applys;

	if (!m_pTable->GetBasicApplys(ds_type, vec_basic_applys))
	{
		sys_err ("There is no BasicApply about %d type dragon soul.", ds_type);
		return false;
	}
	if (!m_pTable->GetAdditionalApplys(ds_type, vec_addtional_applys))
	{
		sys_err ("There is no AdditionalApply about %d type dragon soul.", ds_type);
		return false;
	}


	int basic_apply_num, add_min, add_max;
	if (!m_pTable->GetApplyNumSettings(ds_type, grade_idx, basic_apply_num, add_min, add_max))
	{
		sys_err ("In ApplyNumSettings, INVALID VALUES Group type(%d), GRADE idx(%d)", ds_type, grade_idx);
		return false;
	}

	float fWeight = 0.f;
	if (!m_pTable->GetWeight(ds_type, grade_idx, step_idx, strength_idx, fWeight))
	{
		return false;
	}
	fWeight /= 100.f;

	int n = MIN(basic_apply_num, vec_basic_applys.size());
	for (int i = 0; i < n; i++)
	{
		const SApply& basic_apply = vec_basic_applys[i];
		BYTE bType = basic_apply.apply_type;
		short sValue = (short)(ceil((float)basic_apply.apply_value * fWeight - 0.01f));

		pDS->SetForceAttribute(i, bType, sValue);
	}

	BYTE additional_attr_num = MIN(number (add_min, add_max), 4);

	std::vector <int> random_set;
	if (additional_attr_num > 0)
	{
		random_set.resize(additional_attr_num);
		std::list <float> list_probs;
		for (size_t i = 0; i < vec_addtional_applys.size(); i++)
		{
			list_probs.push_back(vec_addtional_applys[i].prob);
		}
		if (!MakeDistinctRandomNumberSet(list_probs, random_set))
		{
			sys_err ("MakeDistinctRandomNumberSet error.");
			return false;
		}

		for (int i = 0; i < additional_attr_num; i++)
		{
			int r = random_set[i];
			const SApply& additional_attr = vec_addtional_applys[r];
			BYTE bType = additional_attr.apply_type;
			short sValue = (short)(ceil((float)additional_attr.apply_value * fWeight - 0.01f));

			pDS->SetForceAttribute(DRAGON_SOUL_ADDITIONAL_ATTR_START_IDX + i, bType, sValue);
		}
	}

	return true;
}

bool DSManager::DragonSoulItemInitialize(LPITEM pItem)
{
	if (NULL == pItem || !pItem->IsDragonSoul())
		return false;
	PutAttributes(pItem);
	int time = DSManager::instance().GetDuration(pItem);
	if (time > 0)
		pItem->SetSocket(ITEM_SOCKET_REMAIN_SEC, time);
	return true;
}

DWORD DSManager::MakeDragonSoulVnum(BYTE bType, BYTE grade, BYTE step, BYTE refine)
{
	return bType * 10000 + grade * 1000 + step * 100 + refine * 10;
}

int DSManager::GetDuration(const LPITEM pItem) const
{
	return pItem->GetDuration();
}

// ��ȥ���� �޾Ƽ� ����� �����ϴ� �Լ�
bool DSManager::ExtractDragonHeart(LPCHARACTER ch, LPITEM pItem, LPITEM pExtractor)
{
	if (NULL == ch || NULL == pItem)
		return false;
	if (pItem->IsEquipped())
	{
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 623, "");
#endif
		return false;
	}

	DWORD dwVnum = pItem->GetVnum();
	BYTE ds_type, grade_idx, step_idx, strength_idx;
	GetDragonSoulInfo(dwVnum, ds_type, grade_idx, step_idx, strength_idx);

	int iBonus = 0;

	if (NULL != pExtractor)
	{
		iBonus = pExtractor->GetValue(0);
	}

	std::vector <float> vec_chargings;
	std::vector <float> vec_probs;

	if (!m_pTable->GetDragonHeartExtValues(ds_type, grade_idx, vec_chargings, vec_probs))
	{
		return false;
	}

	int idx = Gamble(vec_probs);

	//float sum = 0.f;
	if (-1 == idx)
	{
		sys_err ("Gamble is failed. ds_type(%d), grade_idx(%d)", ds_type, grade_idx);
		return false;
	}

	float fCharge = vec_chargings[idx] * (100 + iBonus) / 100.f;
#ifdef ENABLE_DS_EDITS
	fCharge = float(iBonus);
#else
	fCharge = MINMAX <float> (0.f, fCharge, 100.f);
#endif
	if (fCharge < FLT_EPSILON)
	{
		pItem->SetCount(pItem->GetCount() - 1);
		if (NULL != pExtractor)
		{
			pExtractor->SetCount(pExtractor->GetCount() - 1);
		}
		LogManager::instance().ItemLog(ch, pItem, "DS_HEART_EXTRACT_FAIL", "");
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 624, "");
#endif
		return false;
	}
	else
	{
		LPITEM pDH = ITEM_MANAGER::instance().CreateItem(DRAGON_HEART_VNUM);

		if (NULL == pDH)
		{
			sys_err ("Cannot create DRAGON_HEART(%d).", DRAGON_HEART_VNUM);
			return false;
		}

		pItem->SetCount(pItem->GetCount() - 1);
		if (NULL != pExtractor)
		{
			pExtractor->SetCount(pExtractor->GetCount() - 1);
		}

		int iCharge = (int)(fCharge + 0.5f);
		pDH->SetSocket(ITEM_SOCKET_CHARGING_AMOUNT_IDX, iCharge);
		ch->AutoGiveItem(pDH, true);

		std::string s = boost::lexical_cast <std::string> (iCharge);
		s += "%s";
		LogManager::instance().ItemLog(ch, pItem, "DS_HEART_EXTRACT_SUCCESS", s.c_str());
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 624, "");
#endif
		return true;
	}
}

// Ư�� ��ȥ���� ���â���� ������ ���� ���� ���θ� �����ϰ�, ���н� �λ깰�� �ִ� �Լ�.
bool DSManager::PullOut(LPCHARACTER ch, TItemPos DestCell, LPITEM& pItem, LPITEM pExtractor)
{
	if (NULL == ch || NULL == pItem)
	{
		sys_err ("NULL POINTER. ch(%p) or pItem(%p)", ch, pItem);
		return false;
	}

	// ��ǥ ��ġ�� valid���� �˻� ��, valid���� �ʴٸ� ������ �� ������ ã�´�.
	if (!IsValidCellForThisItem(pItem, DestCell))
	{
		int iEmptyCell = ch->GetEmptyDragonSoulInventory(pItem);
		if (iEmptyCell < 0)
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 626, "");
#endif
			return false;
		}
		else
		{
			DestCell.window_type = DRAGON_SOUL_INVENTORY;
			DestCell.cell = iEmptyCell;
		}
	}

	if (!pItem->IsEquipped() || !pItem->RemoveFromCharacter())
		return false;

	bool bSuccess;
	DWORD dwByProduct = 0;
	int iBonus = 0;
	float fProb;
	float fDice;
	// ��ȥ�� ���� ���� ���� ����.
	{
		//DWORD dwVnum = pItem->GetVnum();

		BYTE ds_type, grade_idx, step_idx, strength_idx;
		GetDragonSoulInfo(pItem->GetVnum(), ds_type, grade_idx, step_idx, strength_idx);

		// ���� ������ ���ٸ� �ϴ� ������ �����ϴ� ���̶� ��������.
		if (!m_pTable->GetDragonSoulExtValues(ds_type, grade_idx, fProb, dwByProduct))
		{
			pItem->AddToCharacter(ch, DestCell);
			return true;
		}
		
		fDice = fnumber(0.f, 100.f);
		bSuccess = fDice <= (fProb * (100 + iBonus) / 100.f);
		if (NULL != pExtractor)
		{
			iBonus = pExtractor->GetValue(ITEM_VALUE_DRAGON_SOUL_POLL_OUT_BONUS_IDX);
			pExtractor->SetCount(pExtractor->GetCount() - 1);
			bSuccess = number(1, 100) <= iBonus ? true : false;
		}
	}

	// ĳ������ ��ȥ�� ���� �� �߰� Ȥ�� ����. �λ깰 ����.
	{
		char buf[128];

		if (bSuccess)
		{
			if (pExtractor)
			{
				sprintf(buf, "dice(%d) prob(%d + %d) EXTR(VN:%d)", (int)fDice, (int)fProb, iBonus, pExtractor->GetVnum());
			}
			else
			{
				sprintf(buf, "dice(%d) prob(%d)", (int)fDice, (int)fProb);
			}
			
			LogManager::instance().ItemLog(ch, pItem, "DS_PULL_OUT_SUCCESS", buf);
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 534, "%s", pItem->GetName(ch->GetDesc() ? ch->GetDesc()->GetLanguage() : 0));
#endif
			pItem->AddToCharacter(ch, DestCell);
			return true;
		}
		else
		{
			if (pExtractor)
			{
				sprintf(buf, "dice(%d) prob(%d + %d) EXTR(VN:%d) ByProd(VN:%d)", (int)fDice, (int)fProb, iBonus, pExtractor->GetVnum(), dwByProduct);
			}
			else
			{
				sprintf(buf, "dice(%d) prob(%d) ByProd(VNUM:%d)", (int)fDice, (int)fProb, dwByProduct);
			}
			
			LogManager::instance().ItemLog(ch, pItem, "DS_PULL_OUT_FAILED", buf);
			M2_DESTROY_ITEM(pItem);
			pItem = NULL;
			if (dwByProduct)
			{
				LPITEM pByProduct = ch->AutoGiveItem(dwByProduct);
#ifdef TEXTS_IMPROVEMENT
				if (pByProduct) {
					ch->ChatPacketNew(CHAT_TYPE_INFO, 535, "%s", pByProduct->GetName(ch->GetDesc() ? ch->GetDesc()->GetLanguage() : 0));
				} else {
					ch->ChatPacketNew(CHAT_TYPE_INFO, 536, "");
				}
#endif
			}
#ifdef TEXTS_IMPROVEMENT
			else {
				ch->ChatPacketNew(CHAT_TYPE_INFO, 537, "");
			}
#endif
		}
	}

	return bSuccess;
}

bool DSManager::DoRefineGrade(LPCHARACTER ch, TItemPos (&aItemPoses)[DRAGON_SOUL_REFINE_GRID_SIZE])
{
	if (NULL == ch)
		return false;

	if (NULL == aItemPoses)
	{
		return false;
	}

	if (!ch->DragonSoul_RefineWindow_CanRefine()) {
		return false;
	}

	// Ȥ�ó� �� �ߺ��Ǵ� item pointer ���ֱ� ���ؼ� set ���
	// �̻��� ��Ŷ�� ���� ���, �ߺ��� TItemPos�� ���� ���� �ְ�, �߸��� TItemPos�� ���� ���� �ִ�.
	std::set <LPITEM> set_items;
	for (int i = 0; i < DRAGON_SOUL_REFINE_GRID_SIZE; i++)
	{
		if (aItemPoses[i].IsEquipPosition())
			return false;
		LPITEM pItem = ch->GetItem(aItemPoses[i]);
		if (NULL != pItem)
		{
			// ��ȥ���� �ƴ� �������� ����â�� ���� �� ����.
			if (!pItem->IsDragonSoul())
			{
#ifdef TEXTS_IMPROVEMENT
				ch->ChatPacketNew(CHAT_TYPE_INFO, 628, "");
#endif
				SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));
				return false;
			}

			set_items.insert(pItem);
		}
	}

	if (set_items.size() == 0)
	{
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL, NPOS);
		return false;
	}

	int count = set_items.size();
	int need_count = 0;
	int fee = 0;
	std::vector <float> vec_probs;
	//float prob_sum;

	BYTE ds_type, grade_idx, step_idx, strength_idx;
	int result_grade;

	// ���� ó�� ���� ��ȭ�� �������� ��´�.
	std::set <LPITEM>::iterator it = set_items.begin();
	{
		LPITEM pItem = *it;

		GetDragonSoulInfo(pItem->GetVnum(), ds_type, grade_idx, step_idx, strength_idx);

		if (!m_pTable->GetRefineGradeValues(ds_type, grade_idx, need_count, fee, vec_probs))
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 627, "");
#endif
			SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));

			return false;
		}
	}
	while (++it != set_items.end())
	{
		LPITEM pItem = *it;

		// Ŭ�� ui���� ������ �������� ����â�� �ø� �� ������ ���ұ� ������,
		// ������ �˸� ó���� ����.
		if (pItem->IsEquipped())
		{
			return false;
		}

		if (ds_type != GetType(pItem->GetVnum()) || grade_idx != GetGradeIdx(pItem->GetVnum()))
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 628, "");
#endif
			SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));

			return false;
		}
	}

	// Ŭ�󿡼� �ѹ� ���� üũ�� �ϱ� ������ count != need_count��� invalid Ŭ���� ���ɼ��� ũ��.
	if (count != need_count)
	{
		sys_err ("Possiblity of invalid client. Name %s", ch->GetName());
		BYTE bSubHeader = count < need_count? DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL : DS_SUB_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL;
		SendRefineResultPacket(ch, bSubHeader, NPOS);
		return false;
	}

	if (ch->GetGold() < fee)
	{
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 232, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY, NPOS);
		return false;
	}

	if (-1 == (result_grade = Gamble(vec_probs)))
	{
		sys_err ("Gamble failed. See RefineGardeTables' probabilities");
		return false;
	}

	LPITEM pResultItem = ITEM_MANAGER::instance().CreateItem(MakeDragonSoulVnum(ds_type, (BYTE)result_grade, 0, 0));

	if (NULL == pResultItem)
	{
		sys_err ("INVALID DRAGON SOUL(%d)", MakeDragonSoulVnum(ds_type, (BYTE)result_grade, 0, 0));
		return false;
	}

	ch->PointChange(POINT_GOLD, -fee);
	int left_count = need_count;

	for (std::set <LPITEM>::iterator it = set_items.begin(); it != set_items.end(); it++)
	{
		LPITEM pItem = *it;
		int n = pItem->GetCount();
		if (left_count > n)
		{
			pItem->RemoveFromCharacter();
			M2_DESTROY_ITEM(pItem);
			left_count -= n;
		}
		else
		{
			pItem->SetCount(n - left_count);
		}
	}

	ch->AutoGiveItem(pResultItem, true);

	if (result_grade > grade_idx)
	{
		char buf[128];
		sprintf(buf, "GRADE : %d -> %d", grade_idx, result_grade);
		LogManager::instance().ItemLog(ch, pResultItem, "DS_GRADE_REFINE_SUCCESS", buf);
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 629, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_SUCCEED, TItemPos (pResultItem->GetWindow(), pResultItem->GetCell()));
		return true;
	}
	else
	{
		char buf[128];
		sprintf(buf, "GRADE : %d -> %d", grade_idx, result_grade);
		LogManager::instance().ItemLog(ch, pResultItem, "DS_GRADE_REFINE_FAIL", buf);
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 630, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL, TItemPos (pResultItem->GetWindow(), pResultItem->GetCell()));
		return false;
	}
}

bool DSManager::DoRefineStep(LPCHARACTER ch, TItemPos (&aItemPoses)[DRAGON_SOUL_REFINE_GRID_SIZE])
{
	if (NULL == ch)
		return false;
	if (NULL == aItemPoses)
	{
		return false;
	}

	if (!ch->DragonSoul_RefineWindow_CanRefine()) {
		return false;
	}

	// Ȥ�ó� �� �ߺ��Ǵ� item pointer ���ֱ� ���ؼ� set ���
	// �̻��� ��Ŷ�� ���� ���, �ߺ��� TItemPos�� ���� ���� �ְ�, �߸��� TItemPos�� ���� ���� �ִ�.
	std::set <LPITEM> set_items;
	for (int i = 0; i < DRAGON_SOUL_REFINE_GRID_SIZE; i++)
	{
		LPITEM pItem = ch->GetItem(aItemPoses[i]);
		if (NULL != pItem)
		{
			// ��ȥ���� �ƴ� �������� ����â�� ���� �� ����.
			if (!pItem->IsDragonSoul())
			{
#ifdef TEXTS_IMPROVEMENT
				ch->ChatPacketNew(CHAT_TYPE_INFO, 628, "");
#endif
				SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));
				return false;
			}
			set_items.insert(pItem);
		}
	}

	if (set_items.size() == 0)
	{
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL, NPOS);
		return false;
	}

	std::string stGroupName;
	int count = set_items.size();
	int need_count = 0;
	int fee = 0;
	std::vector <float> vec_probs;

	BYTE ds_type, grade_idx, step_idx, strength_idx;
	int result_step;

	// ���� ó�� ���� ��ȭ�� �������� ��´�.
	std::set <LPITEM>::iterator it = set_items.begin();
	{
		LPITEM pItem = *it;
		GetDragonSoulInfo(pItem->GetVnum(), ds_type, grade_idx, step_idx, strength_idx);

		if (!m_pTable->GetRefineStepValues(ds_type, step_idx, need_count, fee, vec_probs))
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 627, "");
#endif
			SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));
			return false;
		}
	}

	while(++it != set_items.end())
	{
		LPITEM pItem = *it;
		// Ŭ�� ui���� ������ �������� ����â�� �ø� �� ������ ���ұ� ������,
		// ������ �˸� ó���� ����.
		if (pItem->IsEquipped())
		{
			return false;
		}
		if (ds_type != GetType(pItem->GetVnum()) || grade_idx != GetGradeIdx(pItem->GetVnum()) || step_idx != GetStepIdx(pItem->GetVnum()))
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 628, "");
#endif
			SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));
			return false;
		}
	}

	// Ŭ�󿡼� �ѹ� ���� üũ�� �ϱ� ������ count != need_count��� invalid Ŭ���� ���ɼ��� ũ��.
	if (count != need_count)
	{
		sys_err ("Possiblity of invalid client. Name %s", ch->GetName());
		BYTE bSubHeader = count < need_count? DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL : DS_SUB_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL;
		SendRefineResultPacket(ch, bSubHeader, NPOS);
		return false;
	}

	if (ch->GetGold() < fee)
	{
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 232, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY, NPOS);
		return false;
	}

	//float sum = 0.f;

	if (-1 == (result_step = Gamble(vec_probs)))
	{
		sys_err ("Gamble failed. See RefineStepTables' probabilities");
		return false;
	}

	LPITEM pResultItem = ITEM_MANAGER::instance().CreateItem(MakeDragonSoulVnum(ds_type, grade_idx, (BYTE)result_step, 0));

	if (NULL == pResultItem)
	{
		sys_err ("INVALID DRAGON SOUL(%d)", MakeDragonSoulVnum(ds_type, grade_idx, (BYTE)result_step, 0));
		return false;
	}

	ch->PointChange(POINT_GOLD, -fee);
	int left_count = need_count;
	for (std::set <LPITEM>::iterator it = set_items.begin(); it != set_items.end(); it++)
	{
		LPITEM pItem = *it;
		int n = pItem->GetCount();
		if (left_count > n)
		{
			pItem->RemoveFromCharacter();
			M2_DESTROY_ITEM(pItem);
			left_count -= n;
		}
		else
		{
			pItem->SetCount(n - left_count);
		}
	}

	ch->AutoGiveItem(pResultItem, true);
	if (result_step > step_idx)
	{
		char buf[128];
		sprintf(buf, "STEP : %d -> %d", step_idx, result_step);
		LogManager::instance().ItemLog(ch, pResultItem, "DS_STEP_REFINE_SUCCESS", buf);
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 629, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_SUCCEED, TItemPos (pResultItem->GetWindow(), pResultItem->GetCell()));
		return true;
	}
	else
	{
		char buf[128];
		sprintf(buf, "STEP : %d -> %d", step_idx, result_step);
		LogManager::instance().ItemLog(ch, pResultItem, "DS_STEP_REFINE_FAIL", buf);
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 630, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL, TItemPos (pResultItem->GetWindow(), pResultItem->GetCell()));
		return false;
	}
}

bool IsDragonSoulRefineMaterial(LPITEM pItem)
{
	if (pItem->GetType() != ITEM_MATERIAL)
		return false;
	return (pItem->GetSubType() == MATERIAL_DS_REFINE_NORMAL ||
		pItem->GetSubType() == MATERIAL_DS_REFINE_BLESSED ||
		pItem->GetSubType() == MATERIAL_DS_REFINE_HOLLY);
}

bool DSManager::DoRefineStrength(LPCHARACTER ch, TItemPos (&aItemPoses)[DRAGON_SOUL_REFINE_GRID_SIZE])
{
	if (NULL == ch)
		return false;
	if (NULL == aItemPoses)
	{
		return false;
	}

	if (!ch->DragonSoul_RefineWindow_CanRefine()) {
		return false;
	}

	// Ȥ�ó� �� �ߺ��Ǵ� item pointer ���ֱ� ���ؼ� set ���
	// �̻��� ��Ŷ�� ���� ���, �ߺ��� TItemPos�� ���� ���� �ְ�, �߸��� TItemPos�� ���� ���� �ִ�.
	std::set <LPITEM> set_items;
	for (int i = 0; i < DRAGON_SOUL_REFINE_GRID_SIZE; i++)
	{
		LPITEM pItem = ch->GetItem(aItemPoses[i]);
		if (pItem)
		{
			set_items.insert(pItem);
		}
	}
	if (set_items.size() == 0)
	{
		return false;
	}

	int fee;

	LPITEM pRefineStone = NULL;
	LPITEM pDragonSoul = NULL;
	for (std::set <LPITEM>::iterator it = set_items.begin(); it != set_items.end(); it++)
	{
		LPITEM pItem = *it;
		// Ŭ�� ui���� ������ �������� ����â�� �ø� �� ������ ���ұ� ������,
		// ������ �˸� ó���� ����.
		if (pItem->IsEquipped())
		{
			return false;
		}

		// ��ȥ���� ��ȭ������ ����â�� ���� �� �ִ�.
		// �׸��� �ϳ����� �־���Ѵ�.
		if (pItem->IsDragonSoul())
		{
			if (pDragonSoul != NULL)
			{
				SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));
				return false;
			}
			pDragonSoul = pItem;
		}
		else if(IsDragonSoulRefineMaterial(pItem))
		{
			if (pRefineStone != NULL)
			{
				SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));
				return false;
			}
			pRefineStone = pItem;
		}
		else
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 628, "");
#endif
			SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem->GetWindow(), pItem->GetCell()));
			return false;
		}
	}

	BYTE bType, bGrade, bStep, bStrength;

	if (!pDragonSoul || !pRefineStone)
	{
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL, NPOS);

		return false;
	}

	if (NULL != pDragonSoul)
	{
		GetDragonSoulInfo(pDragonSoul->GetVnum(), bType, bGrade, bStep, bStrength);

		float fWeight = 0.f;
		// ����ġ ���� ���ٸ� ��ȭ�� �� ���� ��ȥ��
		if (!m_pTable->GetWeight(bType, bGrade, bStep, bStrength + 1, fWeight))
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 627, "");
#endif
			SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_MAX_REFINE, TItemPos(pDragonSoul->GetWindow(), pDragonSoul->GetCell()));
			return false;
		}
		// ��ȭ���� �� ����ġ�� 0�̶�� �� �̻� ��ȭ�Ǽ��� �ȵȴ�.
		if (fWeight < FLT_EPSILON)
		{
#ifdef TEXTS_IMPROVEMENT
			ch->ChatPacketNew(CHAT_TYPE_INFO, 627, "");
#endif
			SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_MAX_REFINE, TItemPos(pDragonSoul->GetWindow(), pDragonSoul->GetCell()));
			return false;
		}
	}

	float fProb;
	if (!m_pTable->GetRefineStrengthValues(bType, pRefineStone->GetSubType(), bStrength, fee, fProb))
	{
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 627, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pDragonSoul->GetWindow(), pDragonSoul->GetCell()));

		return false;
	}

	if (ch->GetGold() < fee)
	{
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 232, "");
#endif
		SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY, NPOS);
		return false;
	}

	ch->PointChange(POINT_GOLD, -fee);
	LPITEM pResult = NULL;
	BYTE bSubHeader;

	if (fnumber(0.f, 100.f) <= fProb)
	{
		pResult = ITEM_MANAGER::instance().CreateItem(MakeDragonSoulVnum(bType, bGrade, bStep, bStrength + 1));
		if (NULL == pResult)
		{
			sys_err ("INVALID DRAGON SOUL(%d)", MakeDragonSoulVnum(bType, bGrade, bStep, bStrength + 1));
			return false;
		}
		pDragonSoul->RemoveFromCharacter();

		pDragonSoul->CopyAttributeTo(pResult);
		RefreshItemAttributes(pResult);

		pDragonSoul->SetCount(pDragonSoul->GetCount() - 1);
		pRefineStone->SetCount(pRefineStone->GetCount() - 1);

		char buf[128];
		sprintf(buf, "STRENGTH : %d -> %d", bStrength, bStrength + 1);
		LogManager::instance().ItemLog(ch, pDragonSoul, "DS_STRENGTH_REFINE_SUCCESS", buf);
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 629, "");
#endif
		ch->AutoGiveItem(pResult, true);
		bSubHeader = DS_SUB_HEADER_REFINE_SUCCEED;
	}
	else
	{
		if (bStrength != 0)
		{
			pResult = ITEM_MANAGER::instance().CreateItem(MakeDragonSoulVnum(bType, bGrade, bStep, bStrength - 1));
			if (NULL == pResult)
			{
				sys_err ("INVALID DRAGON SOUL(%d)", MakeDragonSoulVnum(bType, bGrade, bStep, bStrength - 1));
				return false;
			}
			pDragonSoul->CopyAttributeTo(pResult);
			RefreshItemAttributes(pResult);
		}
		bSubHeader = DS_SUB_HEADER_REFINE_FAIL;

		char buf[128];
		sprintf(buf, "STRENGTH : %d -> %d", bStrength, bStrength - 1);
		// strength��ȭ�� ���н� ���� ���� �־�, ���� �������� �������� �α׸� ����.
		LogManager::instance().ItemLog(ch, pDragonSoul, "DS_STRENGTH_REFINE_FAIL", buf);
#ifdef TEXTS_IMPROVEMENT
		ch->ChatPacketNew(CHAT_TYPE_INFO, 630, "");
#endif
		pDragonSoul->SetCount(pDragonSoul->GetCount() - 1);
		pRefineStone->SetCount(pRefineStone->GetCount() - 1);
		if (NULL != pResult)
			ch->AutoGiveItem(pResult, true);

	}

	SendRefineResultPacket(ch, bSubHeader, NULL == pResult? NPOS : TItemPos (pResult->GetWindow(), pResult->GetCell()));

	return true;
}

#ifdef ENABLE_DS_REFINE_ALL
void DSManager::DoRefineAll(LPCHARACTER ch, uint8_t subheader, uint8_t type, uint8_t grade) {
	if (!ch || subheader != DS_SUB_HEADER_DO_REFINE_GRADE) {
		return;
	}

	if (ch->IsDSRefiningAll()) {
		return;
	}

	if (!(type >= 0 && type <= 5) || 
		!(grade >= (uint8_t)(DRAGON_SOUL_GRADE_NORMAL) && grade < (uint8_t)(DRAGON_SOUL_GRADE_MAX - 1))) {
		return;
	}

	if (!ch->DragonSoul_RefineWindow_CanRefine()) {
		return;
	}

	ch->SetDSRefiningAll(true);

	WORD wBaseCell = 300 + (192 * type) + (grade * DRAGON_SOUL_BOX_SIZE);

	uint8_t i = 0;

	LPITEM pDragonSoul1 = NULL, pDragonSoul2 = NULL;

	uint8_t ds_type, grade_idx, step_idx, strength_idx;
	int32_t result_grade;

	int32_t need_count = 0;
	int32_t fee = 0;
	std::vector <float> vec_probs;

	do {
		if (!pDragonSoul1) {
			if ((pDragonSoul1 = ch->GetItem(TItemPos(DRAGON_SOUL_INVENTORY, wBaseCell + i))) != NULL) {
				if (pDragonSoul1->IsEquipped() || 
					pDragonSoul1->IsExchanging() || 
					pDragonSoul1->isLocked()) {
					i++;
					continue;
				}

				pDragonSoul1->Lock(true);
			}
		} else if (!pDragonSoul2) {
			if ((pDragonSoul2 = ch->GetItem(TItemPos(DRAGON_SOUL_INVENTORY, wBaseCell + i))) != NULL) {
				if (pDragonSoul2->IsEquipped() || 
					pDragonSoul2->IsExchanging() || 
					pDragonSoul2->isLocked()) {
					i++;
					continue;
				}

				pDragonSoul2->Lock(true);
			}
		}

		if (pDragonSoul1 && pDragonSoul2) {
			GetDragonSoulInfo(pDragonSoul1->GetVnum(), ds_type, grade_idx, step_idx, strength_idx);
			if (!m_pTable->GetRefineGradeValues(ds_type, grade_idx, need_count, fee, vec_probs)) {
				pDragonSoul1->Lock(false);
				pDragonSoul2->Lock(false);

#ifdef TEXTS_IMPROVEMENT
				ch->ChatPacketNew(CHAT_TYPE_INFO, 627, "");
#endif
				SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pDragonSoul1->GetWindow(), pDragonSoul1->GetCell()));
				break;
			}

			if (need_count != 2) {
				pDragonSoul1->Lock(false);
				pDragonSoul2->Lock(false);
				sys_err("The item (%u) require more than 2 materials.", pDragonSoul1->GetVnum());
				break;
			}

			if (ds_type != GetType(pDragonSoul2->GetVnum()) || grade_idx != GetGradeIdx(pDragonSoul2->GetVnum())) {
				pDragonSoul1->Lock(false);
				pDragonSoul2->Lock(false);

#ifdef TEXTS_IMPROVEMENT
				ch->ChatPacketNew(CHAT_TYPE_INFO, 628, "");
#endif
				SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pDragonSoul2->GetWindow(), pDragonSoul2->GetCell()));
				break;
			}

			if (ch->GetGold() < fee) {
#ifdef TEXTS_IMPROVEMENT
				ch->ChatPacketNew(CHAT_TYPE_INFO, 232, "");
#endif
				SendRefineResultPacket(ch, DS_SUB_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY, NPOS);
				break;
			}

			if ((result_grade = Gamble(vec_probs)) == -1) {
				sys_err("Gamble failed. Check the RefineGardeTables probabilities.");
				break;
			}

			LPITEM pResultItem = ITEM_MANAGER::instance().CreateItem(MakeDragonSoulVnum(ds_type, (uint8_t)result_grade, 0, 0));
			if (!pResultItem) {
				sys_err("INVALID DRAGON SOUL(%d)", MakeDragonSoulVnum(ds_type, (uint8_t)result_grade, 0, 0));
				break;
			}

			ch->PointChange(POINT_GOLD, -fee);

			ch->AutoGiveItem(pResultItem, true);

			char log[128];
			sprintf(log, "GRADE : %d -> %d", grade_idx, result_grade);

			if (result_grade > grade_idx)
			{
				LogManager::instance().ItemLog(ch, pResultItem, "DS_GRADE_REFINE_SUCCESS", log);

#ifdef TEXTS_IMPROVEMENT
				ch->ChatPacketNew(CHAT_TYPE_INFO, 629, "");
#endif
			}
			else
			{
				LogManager::instance().ItemLog(ch, pResultItem, "DS_GRADE_REFINE_FAIL", log);

#ifdef TEXTS_IMPROVEMENT
				ch->ChatPacketNew(CHAT_TYPE_INFO, 630, "");
#endif
			}

			pDragonSoul1->RemoveFromCharacter();
			M2_DESTROY_ITEM(pDragonSoul1);
			pDragonSoul1 = NULL;

			pDragonSoul2->RemoveFromCharacter();
			M2_DESTROY_ITEM(pDragonSoul2);
			pDragonSoul2 = NULL;
		}

		i++;
	} while (i < DRAGON_SOUL_BOX_SIZE);

	if (pDragonSoul1) {
		pDragonSoul1->Lock(false);
	}

	if (pDragonSoul2) {
		pDragonSoul2->Lock(false);
	}

	ch->SetDSRefiningAll(false);
}
#endif

void DSManager::SendRefineResultPacket(LPCHARACTER ch, BYTE bSubHeader, const TItemPos& pos)
{
	TPacketGCDragonSoulRefine pack;
	pack.bSubType = bSubHeader;

	if (pos.IsValidItemPosition())
	{
		pack.Pos = pos;
	}
	LPDESC d = ch->GetDesc();
	if (NULL == d)
	{
		return ;
	}
	else
	{
		d->Packet(&pack, sizeof(pack));
	}
}

int DSManager::LeftTime(LPITEM pItem) const
{
	if (pItem == NULL)
		return false;

	// �ϴ��� timer based on wear�� ��ȥ���� �ð� �� �Ǿ �� ��������.
	if (pItem->GetProto()->cLimitTimerBasedOnWearIndex >= 0)
	{
		return pItem->GetSocket(ITEM_SOCKET_REMAIN_SEC);
	}
	// �ٸ� limit type�� ��ȥ������ �ð� �Ǹ� ��� ������� ������ ���� ���� �������� �ϴ� �ð��� ���Ҵٰ� �Ǵ�.
	else
	{
		return INT_MAX;
	}
}

bool DSManager::IsTimeLeftDragonSoul(LPITEM pItem) const
{
	if (pItem == NULL)
		return false;

	// �ϴ��� timer based on wear�� ��ȥ���� �ð� �� �Ǿ �� ��������.
	if (pItem->GetProto()->cLimitTimerBasedOnWearIndex >= 0)
	{
		return pItem->GetSocket(ITEM_SOCKET_REMAIN_SEC) > 0;
	}
	// �ٸ� limit type�� ��ȥ������ �ð� �Ǹ� ��� ������� ������ ���� ���� �������� �ϴ� �ð��� ���Ҵٰ� �Ǵ�.
	else
	{
		return true;
	}
}

bool DSManager::IsActiveDragonSoul(LPITEM pItem) const
{
	return pItem->GetSocket(ITEM_SOCKET_DRAGON_SOUL_ACTIVE_IDX);
}

bool DSManager::ActivateDragonSoul(LPITEM pItem)
{
	if (NULL == pItem)
		return false;
	LPCHARACTER pOwner = pItem->GetOwner();
	if (NULL == pOwner)
		return false;

	int deck_idx = pOwner->DragonSoul_GetActiveDeck();

	if (deck_idx < 0)
		return false;

	if (DRAGON_SOUL_EQUIP_SLOT_START + DS_SLOT_MAX * deck_idx <= pItem->GetCell() &&
			pItem->GetCell() < DRAGON_SOUL_EQUIP_SLOT_START + DS_SLOT_MAX * (deck_idx + 1))
	{
		if (IsTimeLeftDragonSoul(pItem) && !IsActiveDragonSoul(pItem))
		{
			char buf[128];
			sprintf (buf, "LEFT TIME(%d)", LeftTime(pItem));
			LogManager::instance().ItemLog(pOwner, pItem, "DS_ACTIVATE", buf);
			pItem->ModifyPoints(true);
			pItem->SetSocket(ITEM_SOCKET_DRAGON_SOUL_ACTIVE_IDX, 1);

			pItem->StartTimerBasedOnWearExpireEvent();
		}
		return true;
	}
	else
		return false;
}

bool DSManager::DeactivateDragonSoul(LPITEM pItem, bool bSkipRefreshOwnerActiveState)
{
	if (NULL == pItem)
		return false;

	LPCHARACTER pOwner = pItem->GetOwner();
	if (NULL == pOwner)
		return false;

	if (!IsActiveDragonSoul(pItem))
		return false;

	char buf[128];
	pItem->StopTimerBasedOnWearExpireEvent();
	pItem->SetSocket(ITEM_SOCKET_DRAGON_SOUL_ACTIVE_IDX, 0);
	pItem->ModifyPoints(false);

	sprintf (buf, "LEFT TIME(%d)", LeftTime(pItem));
	LogManager::instance().ItemLog(pOwner, pItem, "DS_DEACTIVATE", buf);

	if (false == bSkipRefreshOwnerActiveState)
		RefreshDragonSoulState(pOwner);

	return true;
}

void DSManager::RefreshDragonSoulState(LPCHARACTER ch)
{
	if (NULL == ch)
		return ;
	for (int i = WEAR_MAX_NUM; i < WEAR_MAX_NUM + DS_SLOT_MAX * DRAGON_SOUL_DECK_MAX_NUM; i++)
	{
		LPITEM pItem = ch->GetWear(i);
		if (pItem != NULL)
		{
			if(IsActiveDragonSoul(pItem))
			{
				return;
			}
		}
	}
	ch->DragonSoul_DeactivateAll();
}

DSManager::DSManager()
{
	m_pTable = NULL;
}

DSManager::~DSManager()
{
	if (m_pTable)
		delete m_pTable;
}
