class First:
    def member(self):
        print("First class member")

class Second:       # behaves like a container
    f=First()   # instantiate first class here
    def member(self):
        self.f.member()    # reference global property of current class
        print("Second class member")

s= Second()
s.member()

