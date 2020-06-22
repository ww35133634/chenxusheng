"""
演示成员方法调用成员方法
"""
class Man:
    def sing(self):
        print("今天唱了一首歌")

    def dance(self):
        print("今天跳了一支舞")

    def run(self):
        print("今天跑了三千米")

    def man(self):
        self.sing()
        self.dance()
        self.run()

man1 = Man()
man1.man()


















































