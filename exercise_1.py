#========= DICTIONARY =======
response = {
"success" : True,
"message" : "Welcome",
"data" : ["email", "username"]
}
print(type(response))
print(response.keys())
 
first, *second = response
print(first)
print(second)

print(response["message"] + " " + response["data"][1])  
response["success"] = False
print(response)
 



print(type([{"data" : [( )]}],))

import pprint
response = {
    "success" : True,
    "message" : "Login successful",
    "data" : [
        "blaise@example.com",
        "macho",
        "blaise"
    ]
}
pprint.pprint(response)
print(response)
print(type(response))


#Another
import pprint
oxford = {
    "apple" : "common fruit",
    "ball" : "a round object",
    "cat" : " an ainmal of the family of Felidae",
    "egg" : "a spherical object",
    "fish" : "a cold blooded vertebrate",
    "goat" : "Sharp animal",
    "house" : "a building",
    "idiot" : "a wild animal",
    "jackal" : "a wild animal in the bush"
}
pprint.pprint(oxford)
print("The meaning of ball is : " + oxford["ball"])
oxford["kettle"] = "a vessel for boiling stuffs"
pprint.pprint(oxford)
print(oxford.keys(), "\n", type(oxford.keys()))
print(oxford.values(), "\n", type(oxford.values()))

