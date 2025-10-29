# Remember to import random function here
import random
my_list = [4, 5, 734, 43, 45]

# The magic goes below
ini_list = 10
# random.randint(0,1000):
comp_list = [random.randint(0,1000) for _ in range(ini_list)]
my_list.extend(comp_list)
print(my_list)