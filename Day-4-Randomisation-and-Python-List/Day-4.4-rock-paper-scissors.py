import random

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

rock_paper_scissors = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
ai_choice = random.randint(0, 2)

if your_choice == ai_choice:
    print(f"{rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n{rock_paper_scissors[ai_choice]}")
    print("IT's A TIE!!!")
elif your_choice == 0 and ai_choice == 1:
    print(f"{rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n{rock_paper_scissors[ai_choice]}\nYou lose!!!")
elif your_choice == 0 and ai_choice == 2:
    print(f"{rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n{rock_paper_scissors[ai_choice]}\nYou win!!!")
elif your_choice == 1 and ai_choice == 0:
    print(f"{rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n{rock_paper_scissors[ai_choice]}\nYou win!!!")
elif your_choice == 1 and ai_choice == 2:
    print(f"{rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n{rock_paper_scissors[ai_choice]}\nYou lose!!!")
elif your_choice == 2 and ai_choice == 0:
    print(f"{rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n{rock_paper_scissors[ai_choice]}\nYou lose!!!")
elif your_choice == 2 and ai_choice == 1:
    print(f"{rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n{rock_paper_scissors[ai_choice]}\nYou win!!!")

