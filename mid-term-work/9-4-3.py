# -*- coding: utf-8 -*-
with open('balance_sheet.txt',encoding='utf8') as f:
    balance_sheet = f.readlines()
with open('daily_check.txt',encoding='utf8') as g:
    daily_check = g.readlines()

balance = [x.split() for x in balance_sheet]
daily_check = [x.split() for x in daily_check]

choose_s = input('1.查账；2.记账\n请选择服务：')
if int(choose_s) == 1:
    check_account = int(input('查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债状况\n请选择服务'))
    if check_account == 1:
        print(daily_check[0])

    elif check_account == 2:
        input('请输入公司名：\n')
        for x in balance:
            print('与%s共有%d笔交易\n交易时间：%s\n收入：%s\n支出：%s\n应收款项：%s\n应出款项：%s')
    # elif check_account == 3:


elif int(choose_s) == 2:
    trade_name = input('交易对象：')
    trade_input = input('收入/万：')
    trade_output = input('支出/万：')
    need_input = input('应收款项/万：')
    need_output = input('应出款项/万：')
else:
    print