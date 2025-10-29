my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

# Your code here
num_elementos=len(my_list)
s_total=0
#v_promedio = s_total % num_elementos 
for i in my_list:
    s_total += i
v_promedio = s_total / num_elementos
print(v_promedio)
