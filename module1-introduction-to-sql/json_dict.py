import json 
with open('testdata.json') as json_file:
    data = json.load(json_file)

modelkeys= []
for i in data:
    if i['model'] not in modelkeys:
        modelkeys.append(i['model'])

count_chars = 0
subchar_counts = {} # {'name': count}
armory_item_count = 0 
weapon_type_count = 0
for i in data:
    name =  i['model']
    if 'charactercreator'in name:        # look at just characters now
        if name == 'charactercreator.character': # count the total characters  
            count_chars += 1  
        else:                                    # work with character subclasses
            if name in subchar_counts:
                subchar_counts[name] += 1
            else: 
                subchar_counts[name] = 1
    elif 'armory.item' in name:
        armory_item_count += 1
    elif'armory.weapon' in name:
        weapon_type_count += 1
        
print( f"total character count : {count_chars}\n\n" 
        f"characters by type : {subchar_counts}\n\n"
        f"item type count  {armory_item_count}\n" 
        f"weapon type count {weapon_type_count}\n"        
     )