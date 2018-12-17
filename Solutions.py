def countex(str):
    str.casefold()      #remove effect of uppercase n lowercase
    l = []
    n = len (str)   #count lenght of string
    for i in range (n):
        l.append (str[i])      #take string character into list
    d = {x: l.count (x) for x in l}       #remove the duplicate count n store key n value
    d={k:round((v*100/n),2) for(k,v) in d.items()}   #perform opearation on value to convert into percentage
    print(d)
    

countex ('my name is anil patidar')
