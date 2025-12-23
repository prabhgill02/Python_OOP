from oops_proj import chatbook

user1 = chatbook()
print(user1.id)
# print(user1._chatbook__name) # to access hidden variable outside we have to add class name as well

chatbook.set_id(10) # Added static method access in between,  We can directly access it no need of object
#---- global hidden variable
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)




# --- getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())





# 2:22

# function vs method below
# lst = [1,2,3]

# # function
# a1 = len(lst)
# print(a1)

# # method
# user1 = chatbook()
