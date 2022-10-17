rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
image = [rock , paper , scissors]
human = int(input("welcome to game type 0 for rock , 1 for paper and 2 for scissors"))
print(image[human])

computer = random.randint(0,2)
print(f"computer choice")
print(image[computer])

if human >= 0 or computer < 0:
  print("invalid no. ")

elif human == 0 and computer == 2 :
  print("you win")

elif human == 2 and computer == 0 :
  print("you lose")

elif human < computer : 
  print("you lose")

elif human == computer:
  print("draw")

elif human > computer : 
  print("you win")

else : 
  print("invalid no. ")
  