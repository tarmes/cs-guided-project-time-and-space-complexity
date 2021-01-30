# MUTABLE

my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = my_list1

# how would you verify both lists have the same identity?

print(my_list1 is my_list2)
print(my_list1)


my_list1.append(7)

# Check if lists still have the same identity
# If they do, why is that?

print(my_list1)
print(my_list2)
print(my_list1 is my_list2)


# Example two, immutable

my_text1 = "Lambda School"
my_text2 = my_text1

print(my_text1 is my_text2)

my_text1 += " is awesome!"

print(my_text1 is my_text2)
print(my_text1)
print(my_text2)
print(my_text1 == my_text2)




# Example Three, tuples are immutable 

produce = ["Apple", "Banana", "Carrot"]
store = ("Bill's Grocery", produce)
print(store)
print(id(store))

produce.append("Dragonfruit")
produce = ['totally new list']
print(store)
store = ("Bill's Grocery", produce)
print(id(store))