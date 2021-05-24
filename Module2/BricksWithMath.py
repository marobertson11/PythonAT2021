blocks = int(input("Enter the number of blocks: "))

height = round((2 * blocks) ** 0.5)

if(blocks < height * (height + 1) / 2):  
    height -= 1   

print("The height of the pyramid:", height)
