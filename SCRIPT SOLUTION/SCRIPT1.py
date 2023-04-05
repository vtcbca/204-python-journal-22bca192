#write a script to enter any string and check palidrome or not.
x=input("Enter any string:")
y=x[::-1]
if(x==y):
    print("This string is palidrome")
else:
    print("This strintg is not palidrome")
    
