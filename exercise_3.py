contact_list = {
    "Jane" : "07034",
    "Favour" : "0812",
    "Tom" : "0703",
    "Jerry" : "0803"
}

print(contact_list)

print(contact_list["Favour"])
print(contact_list.keys())
print(contact_list.values())
print(contact_list.items())
print(contact_list.get("Jane"))

# update method

contact_list.update({"Jane" : "1223"})
print(contact_list)
del contact_list["Jane"]
contact_list.popitem()
print(contact_list)

#new_dict = contact_list.copy()
new = contact_list
new.popitem()
print(new)
print(contact_list)

new = contact_list.copy()
new.popitem()
print(new)
print(contact_list)
