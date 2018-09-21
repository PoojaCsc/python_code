class Human():
    NUM_OF_LIMBS = 4     # Class variable
    def __init__(self,name,gender):
        self.name = name      # instance var
        self.gender = gender  # instance var



pooja  = Human("Pooja","Female")
akash = Human("Akash", "Male")
print(pooja.name)      # instance var. Has to be accessed using instance name
print(akash.name)
print(Human.NUM_OF_LIMBS)    # class var . Can be accessed using class name
# print(Human.name)             # error as name is an instance var
print(pooja.NUM_OF_LIMBS)     # class var. Can also be accessed using instance name coz it is available to all instances
print(akash.NUM_OF_LIMBS)