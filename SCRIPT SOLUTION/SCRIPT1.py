#write a script enter the string check palidrome  or note.

x=input("enter any string :")
y=x[::-1]
if(x==x[::-1]):
    print("this string is palidrome")
else:
    print("this string is not palidrome")
    
    

