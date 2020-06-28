"""
单位采购一批办公家具有,共有一万元资金,买100件家具
高级桌子每张 500
普通桌子每张 300
椅子三把 100
要求:把资金刚好花完,并且所有家具的数量加起来是100件
请设计一个软件系统来给出采购方案
只是用一次for循环且循环次数不大于5
"""
price_senior_desk = 500
price_general_desk = 300
price_chair = 100/3
total_money = 10000
total_number = 100

for i in range(1,int(total_money/price_senior_desk)+1):
    for j  in range(1,int(total_money/price_general_desk)+1):
        for k  in range(1,int(total_money/price_chair)+1):
            if i + j + k ==total_number and price_senior_desk*i + price_general_desk*j + price_chair*k == total_money:
                print(i,j,k)



