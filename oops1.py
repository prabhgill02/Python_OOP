# initiate a class
class employee:
    #special method/magic method/constructor
    def __init__(self):
        print(id(self))
        print("started executed constructor")
        self.id = 23
        self.salary = 50000
        self.designation = "SDE"
        print("constructor executed")

    def travel(self, destination):
        print("called manually")
        print(f"Employee is now travelling to {destination}")




# create instance
sam = employee()

sam.name = "Sam Kumar" # --- Creating attribute outside the class 
print(sam.name)
print(sam.id)
print(sam.salary)
print(sam.travel("Himalya"))

print(type(sam))



# when we are calling sam.travel("Himalay") --- then bydefault the self method is going inside self means
# the object itself here it is sam, so if you remove self from method definition it will give error.
# self goes into method by default

shaktimaan = employee()
print(id(shaktimaan))
