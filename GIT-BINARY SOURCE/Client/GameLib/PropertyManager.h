#pragma once

class CPropertyManager : public CSingleton<CPropertyManager>
{
	public:
		CPropertyManager();
		virtual ~CPropertyManager();

		void Clear();

		bool Initialize(const std::string& listFileName);
		bool Register(const char* c_pszFileName, CProperty** ppProperty = NULL);

		bool Get(DWORD dwCRC, CProperty** ppProperty);
		bool Get(const char* c_pszFileName, CProperty** ppProperty);

	protected:
		typedef std::map<DWORD, CProperty*> TPropertyCRCMap;
		typedef std::set<DWORD> TCRCSet;

		bool m_isFileMode;
		TPropertyCRCMap m_PropertyByCRCMap;
		TCRCSet m_ReservedCRCSet;
};
