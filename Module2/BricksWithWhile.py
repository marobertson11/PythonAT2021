blocks = int(input("Enter the number of blocks: "))

# Using 0 here allows us to account for the "1" block scenerio.
 height = 0

# # Starting with a single required block prevents the "0" error. 
 blocks_needed = 1

breakpoint()
 while blocks_needed <= blocks:
   height += 1
   blocks -= blocks_needed
   blocks_needed += 1

print("The height of the pyramid:", height)
