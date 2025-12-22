# initiate a class
class employee:
    #special method/magic method/constructor
    def __init__(self):
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
print(sam.id)
print(sam.salary)
print(sam.travel("Himalya"))

print(type(sam))