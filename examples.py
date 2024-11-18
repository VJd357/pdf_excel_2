class Example:
    def get_examples():
        Input_text = 'ABU DHABI COMMERCIAL BANK PJSC\n\nCondensed consolidated interim statement of financial position\n\nAs at June 30, 2024 a ee\n\nAs at As at\nJune 30 December 31\n2024 2023\nunaudited audited\nNotes AED’000 AED’000\n\nAssets\nCash and balances with central banks, net 4 38,963,801 45,375,462\nDeposits and balances due from banks, net 5 42,657,799 37,624,694\nFinancial assets at fair value through profit or loss 6 11,944,358 10,063,020\nDerivative financial instruments 7 17,504,385 13,859,086\nInvestment securities, net 8 132,609,377 128,268,397\nLoans and advances to customers, net 9 332,158,291 301,994,599\nInvestment in associates 374,005 370,622\nInvestment properties 11 1,699,491 1,741,460\nOther assets, net 12 25,487,090 18,960,358\nProperty and equipment, net 1,843,715 1,887,596\nIntangible assets, net 6,999,903 7,049,191\nTotal assets 612,242,215 567,194,485\n\nLiabilities\n\nDue to banks 13 10,809,164 8,794,968\nDerivative financial instruments 7 20,017,103 16,239,495\nDeposits from customers 14 389,960,558 362,905,039\nEuro commercial paper 15 5,736,502 7,777,699\nBorrowings 16 82,849,138 76,653,334\nOther liabilities 17 32,162,293 23,570,527\nTotal liabilities 541,534,758 495,941,018\n\nEquity\nShare capital 18 7,319,947 7,319,947\nShare premium 17,878,882 17,878,882\nOther reserves 19 10,477,140 10,591,907\nRetained earnings 26,271,817 26,701,111\nCapital notes 20 8,754,750 8,754,750\nEquity attributable to equity holders of the Bank 70,702,536 71,246,597\nNon-controlling interests 4,921 6,870\nTotal equity 70,707,457 71,253,467\nTotal liabilities and equity 612,242,215 567,194,485\n\nThis condensed consolidated-interim financial information was approved by the Board of Directors and\nauthorised for issue on July 18, 2024 and signed on its behalf by:\n\n   \n\n \n\nCe * Veh\nKhaldoon Khalifa Al Mubarak Ala’a Eraigat Deepak Khullar —~\nChairman Group Chief Executive Officer Group Chief Financial Officer\n\nThe accompanying notes -1 to 34 form an integral part of this condensed consolidated interim financial\ninformation.\n\x0c'
        Output_json = """[
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Assets\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":null,
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":null
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Cash and balances with central banks, net\"",
        "\"Notes\"":"\"4\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"38,963,801\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"45,375,462\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Deposits and balances due from banks, net\"",
        "\"Notes\"":"\"5\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"42,657,799\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"37,624,694\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Financial assets at fair value through profit or loss\"",
        "\"Notes\"":"\"6\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"11,944,358\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"10,063,020\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Derivative financial instruments\"",
        "\"Notes\"":"\"7\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"17,504,385\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"13,859,086\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Investment securities, net\"",
        "\"Notes\"":"\"8\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"132,609,377\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"128,268,397\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Loans and advances to customers, net\"",
        "\"Notes\"":"\"9\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"332,158,291\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"301,994,599\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Investment in associates\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"374,005\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"370,622\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Investment properties\"",
        "\"Notes\"":"\"11\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"1,699,491\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"1,741,460\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Other assets, net\"",
        "\"Notes\"":"\"12\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"25,487,090\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"18,960,358\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Property and equipment, net\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"1,843,715\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"1,887,596\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Intangible assets, net\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"6,999,903\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"7,049,191\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Total assets\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"612,242,215\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"567,194,485\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Liabilities\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":null,
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":null
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Due to banks\"",
        "\"Notes\"":"\"13\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"10,809,164\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"8,794,968\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Derivative financial instruments\"",
        "\"Notes\"":"\"7\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"20,017,103\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"16,239,495\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Deposits from customers\"",
        "\"Notes\"":"\"14\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"389,960,558\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"362,905,039\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Euro commercial paper\"",
        "\"Notes\"":"\"15\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"5,736,502\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"7,777,699\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Borrowings\"",
        "\"Notes\"":"\"16\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"82,849,138\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"76,653,334\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Other liabilities\"",
        "\"Notes\"":"\"17\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"32,162,293\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"23,570,527\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Total liabilities\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"541,534,758\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"495,941,018\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Equity\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":null,
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":null
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Share capital\"",
        "\"Notes\"":"\"18\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"7,319,947\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"7,319,947\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Share premium\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"17,878,882\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"17,878,882\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Other reserves\"",
        "\"Notes\"":"\"19\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"10,477,140\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"10,591,907\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Retained earnings\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"26,271,817\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"26,701,111\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Capital notes\"",
        "\"Notes\"":"\"20\"",
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":"\"8,754,750\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"8,754,750\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Equity attributable to equity holders of the Bank\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"70,702,536\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"71,246,597\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Non-controlling interests\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"4,921\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"6,870\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Total equity\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"70,707,457\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"71,253,467\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"\"Total liabilities and equity\"",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":" \"612,242,215\"",
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":"\"567,194,485\""
    },
    {
        "\"Condensed Consolidated Interim Statement of Financial Position\"":"-----",
        "\"Notes\"":null,
        "\"As at June 30\\n2024\\nunaudited\" \"AED\u0092000\"":null,
        "\"As at December 31\\n2023\\naudited\" \"AED\u0092000\"":null
    }
]"""
        
        examples = {"example_1": {"Input_Text": Input_text, "Output_Json": Output_json}}
        return examples
