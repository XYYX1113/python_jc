class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18
        print(self.name,self.__age)

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))
    def secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d  输出的方法是 %s" % (self.name, self.__age,"secret"))


xiaofang = Women("小芳")
xiaofang.secret()
# 私有属性，在外界不能够被直接访问
# print(xiaofang.__age)
# 私有方法，同样不允许在外界直接访问
# xiaofang.__secret()
