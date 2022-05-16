d1={"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"]}
d2={}
for k,v in d1.items():
        for value in v:
                if value not in d2:
                        d2[value]=[]
                d2[value].append(k)
print(d2)
