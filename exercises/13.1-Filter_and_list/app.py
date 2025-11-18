all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
find_char = "R"
resulting_names = list(filter(lambda name: find_char in name, all_names))

print(resulting_names)




