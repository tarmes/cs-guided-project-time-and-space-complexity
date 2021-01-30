# CONSTANT TIME, O(1)

def print_one_item(items):
   print(items[0])


# LINEAR TIME, O(n)

def print_every_item(items):
   for item in items:
      print(item)

# QUADRATIC TIME, O(n^2)

def print_pairs(items):
   for item_one in items:
      for item_two in items:
         print(item_one, item_two)

# LOGARITHMIC TIME, O(log n)

def number_of_steps(num):
   steps = 0
   while num > 0:
      if num % 2 == 0:
         num = num // 2
      else:
         num = num - 1 
      steps = steps + 1
   return steps