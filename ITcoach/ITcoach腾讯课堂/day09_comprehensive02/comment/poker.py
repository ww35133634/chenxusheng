import random
import time
class Poker():
    def __init__(self,pare_num:int=1,people_num:int=4):
        num_tuple = tuple("3、4、5、6、7、8、9、10、J、Q、K、A、2".split("、"))
        type_tuple = tuple("♠、♥、♣、♦".split("、"))
        self.poker_dit = {"num": num_tuple, "type": type_tuple}    #基础数据
        self.pare_num = pare_num            #几付牌
        self.people_num = people_num        #玩家人数
        self.all_poker_list = []            #存放生成的牌
        self.all_people_poker_list = []     #存放生成的每一个玩家的牌
    def start(self):
        while True:
            input_num = input("请选择要执行的操作【1-生成牌 2-打印所有牌 3-打印玩家牌 4-发牌 5-洗牌 6-整理牌 7-退出】:")
            if input_num =="1":
                """生成牌"""
                print("正在生成%d付扑克牌..." % self.pare_num)
                time.sleep(1)
                self.produce_poker()
                print("扑克牌生成完毕！")
            elif input_num =="2":
                """打印所有牌"""
                print("正在打印所有的牌...")
                self.print_poker(self.all_poker_list)
                print("所有的牌打印完毕！")
            elif input_num == "3":
                """打印玩家牌"""
                print("正在打印玩家的牌...")
                self.print_people_poker(self.all_people_poker_list)
                print("玩家的牌打印完毕！")
            elif input_num == "4":
                """发牌"""
                print("正在发牌...")
                self.deal_poker()
                print("发牌完毕！")
            elif input_num == "5":
                """洗牌"""
                print("正在洗牌...")
                random.shuffle(self.all_poker_list)
                print("洗牌完毕...")
            elif input_num == "6":
                """整理牌"""
                print("正在整理牌...")
                for one_people_poker in self.all_people_poker_list:
                    one_people_poker.sort()
                print("整理完毕！")
            elif input_num == "7":
                """退出"""
                print("游戏已退出，再见！")
                break
            else:
                print("输入的数字不符合要求，请重新输入！")

    def produce_poker(self):
        one_poker_list = []
        one_poker_list_type = []
        for i_num ,v_num in enumerate(self.poker_dit["num"]):
            for i_type,v_type in enumerate(self.poker_dit["type"]):
                st = str("%02d" % i_num) + str("%02d" % i_type)
                one_poker_list.append(st)
                one_poker_list_type.append(v_type+v_num)
        self.all_poker_list = one_poker_list *self.pare_num
        # print(self.all_poker_list)

    def print_poker(self,contents:list):
        for content in contents:
            print("%s%s" %(self.poker_dit["type"][int(content[2:])],self.poker_dit["num"][int(content[:2])]),end="\t")
        print()

    def deal_poker(self):
        self.all_people_poker_list = []
        for one_people_num in range(self.people_num):
            one_people_poker_list = []
            for i_all_poker_list,v_all_poker_list in enumerate(self.all_poker_list):
                if i_all_poker_list % self.people_num == one_people_num:
                    one_people_poker_list.append(v_all_poker_list)
            self.all_people_poker_list.append(one_people_poker_list)
        # print(self.all_people_poker_list)

    def print_people_poker(self,contents:list):
        for i_content,v_content in enumerate(contents):
            print("第%d个玩家的牌：" % (i_content + 1))
            self.print_poker(v_content)