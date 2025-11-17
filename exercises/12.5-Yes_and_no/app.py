the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def wiki_swap(bool):
    ki = "wiki"
    ko = "woko"
    if bool == 0:
        return ko
    else:
        return ki

new_list = list(map(wiki_swap,the_bools))
print(new_list)