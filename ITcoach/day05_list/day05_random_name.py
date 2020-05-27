import random
def get_name(num:int):
    first_name = ['张', '金', '李', '王', '赵','陈','刘']
    mid_name = ['玉', '明', '龙', '芳', '军', '玲']
    last_name = ['', '立', '玲', '', '国', '','山']
    name = set()
    for i in range(num):
        while len(name) < num:
            st = random.choice(first_name) + random.choice(mid_name) + random.choice(last_name)
            name.add(st)
    return name