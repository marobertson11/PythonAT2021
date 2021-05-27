blocks = int(input("Enter the number of blocks: "))

counter=1
height=0
while(blocks >=0):
    height+=1
    blocks-=counter
    counter+=1
    if((blocks - counter) < 0):
        break
print("The height of the pyramid:", height)
