class Animal(object):#Animal类
    def run(self):
        print('Animal is running')
    def jump(self):
        print('Animal can jump...')

class Dog(Animal):#Animal子类 父类于子类都有run（）时调用子类的
    def run(self):
        print('Dog is running')
    def eat(self):
        print('Dog eat meat')
    def jump(self):
        print('Dog can jump')


def run_twice(animal):#这里不太懂，把两个run（）换成一个run一个eat后
    animal.run()
    #animal.run()      #Dog（）Cat（）一样可以输出但Timer（）不能
    animal.eat()      #可父类Animal并没有eat（）

class Timer(object):
    def run(self):
        print('start...')

class Cat(Timer):
    
    def run(self):
        print('Cat is running')
    def eat(self):
        print('Cat eat meat')






dog = Dog()
dog.run()
dog.eat()
dog.jump()

run_twice(Dog())

cat = Cat()
cat.run()
cat.eat()
run_twice(Cat())

Dog().run()
run_twice(Timer())
Timer().run()
