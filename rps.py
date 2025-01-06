import random

def play():
    #This function starts the program, asks for your choice and sees if you won by checking what the values in the winner function are
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if winner(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def winner(player, opponent):
    if (player != 'r') and (player != 's') and (player != 'p'):
        return print("Invalid input, you're supposed to type letters 'r' or 'p' or 's'. ")
    #This lets the user know they are supposed to type those certain letters and not anything else

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True

        
        
print(play())

        


        