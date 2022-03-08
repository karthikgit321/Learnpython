def firstlast(str):
    if len(str)>=2:
        first=str[0:2]
        last=str[-2:]
        print(first+last)
    else:
        print("empty string")
firstlast("resource")
firstlast("w3")
firstlast("W")