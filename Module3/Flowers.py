#Please submit some suggested code
'''
Imagine that your computer program loves these plants. 
Whenever it receives an input in the form of the word Spathiphyllum, 
it involuntarily shouts to the console the following string: 
    "Spathiphyllum is the best plant ever!"

From Lab 3.1.1.10 
'''
flower = input("What is the best plant? ")

while flower != "peonies":
    print("Nice try, but", flower, "isn't it. Try again!")
    flower = input("What is the best plant? ")

print("Yes,", flower, "is the best plant ever!")
