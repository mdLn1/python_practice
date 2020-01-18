values = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# print(values["birth"]) -- returns error if failes
print(values.get("birth", "default")) # returns none if not found, a default val can be provided
# data can be changed
values["name"] = " new jack"
# new fields can be added
values["birth"] = "Jan 10 1997"
print(values["birth"])

phone = input("Phone ")
translate = {
    "1": 'One',
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
val = ""
for ch in phone:
    val += translate.get(ch, "!") + "  "

print(val)

message = input("> ")
message = message.split(" ")
emojis = {
    ":)": "😄",
    ":(": "😒"
}
text = ""
for word in message:
    text += emojis.get(word, word) + " "

print(text)