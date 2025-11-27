def lyrics_generator(input_list):
    llyric = ""
    bo="Boom "
    dr="Drop the bass "
    third_one="!!!Break the bass!!! "
    count = 0

    for num in input_list:
        if num == 0:
            llyric += bo
            count = 0
        elif num == 1:
            llyric += dr
            count +=1
            if count ==3:
                llyric += third_one
                count ==0
    return llyric 
    #else:
    #    return dr
# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
