class  First:
    def fn1(self):
        print("From parent1")
class Second:
    def fn2(self):
        print("From parent2")

class  Child(First,Second):
    def fn3(self):
        print("Child application")

ch = Child();
ch.fn1()
ch.fn2()
ch.fn3()