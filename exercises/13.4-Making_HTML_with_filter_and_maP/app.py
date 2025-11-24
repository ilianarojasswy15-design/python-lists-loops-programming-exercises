all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def filter_colors(item):
	if item["sexy"] == True:
		return True
	else:
		return False
		
done_sexy = list(filter(filter_colors,all_colors))

def generate_li(color):
    shade = color["label"]
    return f"<li>{shade}</li>"
    
color_list = list(map(generate_li, done_sexy))

print (color_list)







#print(done_sexy)

