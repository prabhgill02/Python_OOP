from oops_proj import chatbook

user1 = chatbook()
# print(chatbook._chatbook__user_id) -- this is the way to access hidden variable or the one mentioned below
# but the best practice is using the concept of getter and setter usingg decorator either @classmethod
#  or @staticmethod decorators
print(user1.id)
# print(user1._chatbook__name) # to access hidden variable outside we have to add class name as well

chatbook.set_id(10) # Added static method access in between,  We can directly access it no need of object
#---- global hidden variable
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

print(user3._chatbook__name)  #---- This is a way to access the hidden variable outside 
# --- getter and setter # -- using getter and setter, we can directly access inside the method using self
print(user1.get_name())
user1.set_name("Agent X")
print(user1.get_name())





# 2:22

# function vs method below
# lst = [1,2,3]

# # function
# a1 = len(lst)
# print(a1)

# # method
# user1 = chatbook()
