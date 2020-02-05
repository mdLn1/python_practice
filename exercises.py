token = "p"
sentence = "padsrepasrep"
y = sentence.count(token)
print(y)

print([(x,y) for x,y in enumerate(["Python", "pressure"])])

(x,y) for x,y in enumerate(a_list,1)