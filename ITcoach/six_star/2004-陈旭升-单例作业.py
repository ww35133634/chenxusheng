class Single_Model:

    instance = None
    t_list = []
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(Single_Model)
        return cls.instance


    def __init__(self, t):
        self.t = t
        self.merge_list()

    def merge_list(self):
        self.t_list.append(self.t)

    def print_list(self):
        print(self.t_list)

if __name__ == '__main__':
    obj01 = Single_Model("张三")
    obj02 = Single_Model("xt四")
    obj01.print_list()
    obj02.print_list()
    print(id(obj01))
    print(id(obj01))