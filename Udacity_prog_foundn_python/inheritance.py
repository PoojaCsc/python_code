class Parent():
    def __init__(self,last_name , eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("last name - " + self.last_name)
        print("eye  color -  " + self.eye_color)

class Child(Parent):
    def __init__(self,last_name, eye_color, num_of_toys):
        print("Child constructor called")
        Parent.__init__(self,last_name,eye_color)           #reusing parent class constructor
        self.num_of_toys = num_of_toys
    def show_info(self):
        Parent.show_info(self)
        print("Num of toys - " + str(self.num_of_toys))


#Billy_Cyrus = Parent("Cyrus", "Blue")
#print(Billy_Cyrus.last_name)
#Billy_Cyrus.show_info()

Miley_Cyrus =Child("Cyrus", "Green", "5")
#print(Miley_Cyrus.last_name)
#print(Miley_Cyrus.num_of_toys)
Miley_Cyrus.show_info()