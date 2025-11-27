par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
par_low = par.lower().split()
#print(par_low)
for words in par_low:
    for letter in words:
        if letter.isalpha():
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

print(counts)
