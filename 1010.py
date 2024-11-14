x = input().split(" ") #to take input with space as a string
y= input().split(" ") #to take input with space as a string
a,b,c = x #spit them as a,b,c
d,e,f= y    #spit them as d,e,f


# convert b,e into int type
# convert c,f into float type


calc=(int(b) * float(c)) + (int(e) * float(f))
#print value 


print("VALOR A PAGAR: R$ %0.2f" %calc)

