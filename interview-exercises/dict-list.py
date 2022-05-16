Dict= {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
       "hotmail.com": ["bruce.wayne"]}
for key,value in Dict.items():
    values = value
    for count,ele in enumerate(values):

        if key=="gmail.com":
            a = ("@"+key)
            print(ele,a)
        elif key=="yahoo.com":
            a = ("@"+key)
            print(ele,a)
        else:
            a = ("@"+key)
            print(ele,a)







