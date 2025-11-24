names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia','Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail','Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia','Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria','Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']

# Your code here
find_char = "am"

    
resulting_names = list(filter(lambda name: find_char in name.lower(), names))
#filtered = list(filter(lambda name: 'am' in name.lower(), names))
#resulting_names = list(filter(find_am,names))
print(resulting_names)