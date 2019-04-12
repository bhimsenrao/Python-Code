class Parent:
    """ Test """
    def view(self):
        print("View from Parent")
    def hi(self):
        print("Hi to ALL")

class Child(Parent):
    def view(self):
        print("Hi iam child Member")

ch=Child()
ch.view()
ch.hi()