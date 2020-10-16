#def areYouPlayingBanjo(name):
#    name_0 = name.find("r",0,2)
#    name_1 = name.find("R",0,2)
#    if name_0 == 0 or name_1 == 0:
#        name = (name + " plays banjo")
#    else:
#        name = (name + " does not play banjo")
#    return name

#def double_integer(i):
#    i = i*2
#double_integer(2)

def fix(paragraph):
    lst = []
    lst_2 = []
    p = paragraph.split(".")
    separator = '.'
    
    for i in p:
        g = i.split(" ")
        lst_2.append(g)
        for x in lst_2:
            for x_1 in x:
                if x.index(x_1) == 1 or x.index(x_1) == 0 or  x.index(x_1) == 2:
                    r = x_1.title()
                    z_1 = r + " "
                    lst.append(z_1)
                else:
                    z_2 = x_1 + " "
                    lst.append(z_2)
                
    tup = lst_2[0] + lst_2[1]
    z = separator.join(tup)
    
    print(z)
    
fix("hello. my name is inigo montoya. you killed my father. prepare to die.")