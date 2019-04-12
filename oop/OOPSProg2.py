def message():
    print("Hello...")

class Info:
    def message(self):
        print("Member1:Message from class")
    def messages(self,name=""):
        print("Member2:Welcome to %s"%(name))

message()
inf =Info()  #instantiate
inf.message()
inf.messages("Kiran")