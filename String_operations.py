name="Guhan Ganesan"
print(name[0])
print(name[1:])
print(name[1::])
print(name[::1])
print(name[::-1])
print(name[-1])
print(name[:-1])
print(name[-4:-1])
print(name[1:6])


Result:-
       
G
uhan Ganesan
uhan Ganesan
Guhan Ganesan
nasenaG nahuG
n
Guhan Ganesa
esa
uhan 
#---------------------------------
star="*"
fname="Guhan"
lname="Ganesan"
print(fname+lname)
print(fname+" "+ lname)
print(fname+"\n"+lname)
print("His name is:",fname,lname)
print(star*5) # repeatations
print("Guhan",
       "Ganesan")

if "han" in "Guhan":
    print("True")

if 'h' in "Guhan":
    print("True")

if 'h' not in "Guhan":
    print("True")
else:
    print("False")


for char in "Guhan":
    if(char=='G'):
        print("Hi")
    if(char=='u'):
        print("How")
        
        
        
Result:
GuhanGanesan
Guhan Ganesan
Guhan
Ganesan
His name is: Guhan Ganesan
*****
Guhan Ganesan
True
True
False
Hi
How
