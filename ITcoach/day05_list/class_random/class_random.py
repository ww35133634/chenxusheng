import random

class Random_name():
    def __init__(self,num):
        self.num = num
        self.name = set()
        # 自动执行
        self.get_name()
    def get_name(self):
        first_name = ['张', '金', '李', '王', '赵', '陈', '刘']
        mid_name = ['玉', '明', '龙', '芳', '军', '玲']
        last_name = ['', '立', '玲', '', '国', '', '山']
        for i in range(self.num):
            while len(self.name) < self.num:
                st = random.choice(first_name) + random.choice(mid_name) + random.choice(last_name)
                self.name.add(st)

class Random_result():
    def __init__(self,begin:int,end:int,num):
        self.begin = begin
        self.end = end
        self.num = num
        self.one_repetition_result = list()
        self.one_distinc_result = set()
        # 自动执行
        self.get_repetition_result()
        self.get_distinc_result()

    def get_repetition_result(self):
        while len(self.one_repetition_result) <= self.num:
            result = random.randint(self.begin, self.end)
            self.one_repetition_result.append(result)

    def get_distinc_result(self):
        while len(self.one_distinc_result) <= self.num:
            result = random.randint(self.begin, self.end)
            self.one_distinc_result.add(result)

