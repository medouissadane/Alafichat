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

print("Welcome to the Rock, Paper, Scissors game: \n")
help = input("Prees Enter continue or type (Help) for the rules ").lower()
if help == "help":
    print(
        """\n
        **************** RULES ****************
        1) You choose and the computer chooses
        2) Rock smashes Scissors --> Rock wins
        3) Scissors cut Paper --> Scissors wins
        4) Paper covers Rock --> Paper wins

    """
    )

game_list = ["Rock", "Paper", "Scissors"]
your_choice = input("Enter your_choice (Rock, Paper, Scissors):").capitalize()

# your_choice*********************
if your_choice not in game_list:
    print("Invalid choice. Please run y=the program  again and choose Rock, Paper, or Scissors")
else:
    
    print("\n You chose:")
    if your_choice=="Rock":
        print(rock_ascii)

    elif your_choice=="Paper":
        print(paper_ascii)

    elif your_choice=="Scissors":
        print(scissors_ascii)

    else:
        print("Invaled choice")


    # computer_choice*****************
    computer_choice = random.choice(game_list)
    print("\n Computer chose:")

    if computer_choice=="Rock":    
        print(rock_ascii)

    elif computer_choice=="Paper":
        print(paper_ascii)

    elif computer_choice=="Scissors":
        print(scissors_ascii)

    #    win or lose*******************
    if your_choice=="Rock" and computer_choice=="Scissors" or your_choice=="Paper" and computer_choice=="Rock" or your_choice=="Scissors" and computer_choice=="Paper":
        print(f"You win! {your_choice} beats {computer_choice}")
    elif your_choice==computer_choice:
        print("It's a tie!")
    else:
        print(f"You lose! {computer_choice} beats {your_choice}")