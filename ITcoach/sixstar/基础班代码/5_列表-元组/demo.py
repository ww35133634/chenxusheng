class Man:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Man)
        return cls.__instance

    def __init__(self,name,age):
        self.name = name
        self.age = age


man1 = Man('bobo', 18)
man2 = Man('lala', 20)
# man1 = Man()
# man2 = Man()
print(id(man1))

print(id(man2))

print(man1.name)