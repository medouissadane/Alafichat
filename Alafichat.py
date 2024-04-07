import random



rock_ascii=("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)
paper_ascii=("""
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  """)
scissors_ascii=("""
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)

print("Marhba bik f alafichat: \n")
help = input("Warak Enter labghiti tal3ab ila makntich 3arf m9awa3id ktab Help: ").lower()
if help == "help":
    print(
        """\n
        **************** L9awa3id ****************
        1) Nta atkhtar o pc ghaykhtar
        2) Hajra m3a M9ass --> Hajra katrba7
        3) M9ass kay9ata3 War9a --> M9ass kyrba7
        4) War9a katghati Hajra --> War9a ktrba7

    """
    )

game_list = ["hajra", "war9a", "m9ass"]

# your_choice*********************
your_choice = input("L3ab (hajra, war9a, m9ass): ")

if your_choice not in game_list:
    print("Khtar Hajra, War9a ola M9as")

else:
    print("\n Nta:")
    if your_choice=="hajra":
        print(rock_ascii)
    elif your_choice=="war9a":
        print(paper_ascii)

    elif your_choice=="m9ass":
        print(scissors_ascii)

    else:
        print("Invaled choice")


    # computer_choice*****************
    computer_choice = random.choice(game_list)
    print("\n Pc:")

    if computer_choice=="hajra":    
        print(rock_ascii)

    elif computer_choice=="war9a":
        print(paper_ascii)

    elif computer_choice=="m9ass":
        print(scissors_ascii)

    #    win or lose*******************
    if your_choice=="hajra" and computer_choice=="m9ass" or your_choice=="war9a" and computer_choice=="hajra" or your_choice=="m9ass" and computer_choice=="war9a":
        print(f"Rbahti! {your_choice} katghlab {computer_choice}")
    elif your_choice==computer_choice:
        print("Ta3adol!")
    else:
        print(f"Khsarti! {computer_choice} katghlab {your_choice}")
