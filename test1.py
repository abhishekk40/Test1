a=6
y=0
for i in range(1,6): # Always keep the first loop for the Count of Number of lines
    for j in range(1,y+1): # This loop is for Printing Space
        print(" ",end=" ")
    y=y+1 #This is for increasing the number of spaces everytime
    for k in range(1,a): #This loop is for Printing "1"
        print("1",end=" ")
    a=a-1 #This is for decreasing the value of "a" everytime

    print("\n")
        
        
