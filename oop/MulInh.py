class First:
    def f1(self):
        print("From first Base")
class Second:
    def f2(self):
        print("From Second Base")

class Child(First,Second):
    def member(self):
        super().f1()
        super().f2()
        print("From Child")
obj=Child()
obj.member()
 