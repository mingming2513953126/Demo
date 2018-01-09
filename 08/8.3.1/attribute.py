class Fruit:
    price = 0                   # 类属性

    def __init__(self):
        self.color = "red"      # 实力属性
        zone = "China"          # 局部变量
        
if __name__ == "__main__":
    print Fruit.price           #输出类属性price的值，输出结果：0
    apple = Fruit()             #对fruit实例化，生成对象apple
    print apple.color                                   #代码输出实例属性color的值，输出结果为：red
    Fruit.price = Fruit.price + 10                      #设置类属性price的值为：10
    print "apple's price:" + str(apple.price)           #输出Apple对象的属性price的值。输出结果：Apple‘s price：10
    banana = Fruit()                                    #对fruit类实例化，生成对象banana
    print "banana's price:" + str(banana.price)         #输出banana对象的属性price的值。输出结果：banana‘s price：10
    #python的类和对象都可以访问类属性

# 访问私有属性
class Fruit:
    def __init__(self):
        self.__color = "red"        # 私有属性
        
if __name__ == "__main__":
    apple = Fruit()
    print apple._Fruit__color       #输出私有属性color的值。结果：red
