#read-write from te file  
s= "vansh is a good boy "
# with open("text.txt" ,"w") as f:
#     f.write(s)

        #or
     
fp = open("text.txt" ,"w")
fp.write(s)
fp.close()

# with open("text.txt" ,"r") as f:
#     s =fp.read()
#     print(s)
    
    
f= open("text.txt" ,"r")
s= f.read()
print(s)