secret_number = 777

 print(
         """
         +================================+
         | Welcome to my game, muggle!    |
         | Enter an integer number        |
         | and guess what number I've     |
         | picked for you.                |
         | So, what is the secret number? |
         +================================+
         """)

 number = int(input("Guess my number or type 0 to give up: "))

# 0 terminates execution.
while number != 0:
    if number == secret_number:
        number = secret_number
        print ("Well done, muggle! You are free now.")
    else:
        print ("Ha ha! You're stuck in my loop!")

number = int(input("Guess my number or type 0 to give up: "))
