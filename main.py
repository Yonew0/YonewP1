abc = "abcdefghijklmnopqrstuvwxyz"
def lower_total(w) :
    c = 0;
    for cha in w :
        for d in abc.lower() :
            if d == cha :
                c += 1
    return c

def upper_total(w) :
    c = 0
    for cha in w :
        for d in abc.upper() :
            if d == cha :
                c += 1
    return c

nadpiss = "Yonew Sjel kakashky"
print(f'{nadpiss} {lower_total(nadpiss)}')
print(f'{nadpiss} {upper_total(nadpiss)}')
input()
