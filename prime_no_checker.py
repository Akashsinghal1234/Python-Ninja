#Write your code below this line 👇
def prime_checker(number):
    a = True
    for i in range(2 , number):
        if number % i == 0 :
            a = False
    if a == True:
        print("It's a prime number.")
    else :
        print("It's not a prime number.")





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
