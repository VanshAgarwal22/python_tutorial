#loops in python
for i in range(5):
    print(i+1)

a = [1,23,56,78,67]
for i in a:
    print(i) #access all the items og list
    
#print the table of any number
print("enter the number you wanna print the table")
a = int(input())
for i in range(10):
    print(a*(i+1))
    
k =0
while(k<10):
    print(k)
    k+=1
    
#break  and continue statement

while(True):
    num = int(input("enter the nmuber : "))
    print(num)
    if(num==5):
        break
print("program finished executing...")

for i in range(10):
    if(i==3):
        continue # skip the number and move forward
    print(i)
