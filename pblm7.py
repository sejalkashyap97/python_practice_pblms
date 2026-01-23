# Suppose you are playing a game in turn with the computer. Total n number of
# sticks are to be picked up in this game. Whoever picks the last one loses the game. Neither
# the computer nor you can pickup more than 3 sticks at a time. Nobody can skip a turn, i.e.
# at least one stick is to be picked up in a turn. Write a program to ensure that the computer
# wins optimally (whenever there is a chance) irrespective of the turn.
def computer_turn(sticks):
    # """
    # Optimal strategy:
    # Leave the opponent with (4k + 1) sticks.
    # """
    if sticks % 4 == 1:
        return 1  # forced move (losing position)
    return (sticks - 1) % 4 or 1 
#comp loses if sticks%4==1 at start of his turn

def game(total_sticks, user_starts):
    sticks = total_sticks

    while sticks > 0:
        print(f"\nSticks remaining: {sticks}")

        if user_starts:
            # User's turn
            choice = int(input("Pick sticks (1-3): "))
            while choice < 1 or choice > 3 or choice > sticks:
                choice = int(input("Invalid move. Pick again (1-3): "))

            sticks -= choice

            if sticks == 0:
                print("You picked the last stick.")
                print("❌ You lose. Computer wins!")
                break

        else:
            # Computer's turn
            choice = computer_turn(sticks)
            if choice > sticks:
                choice = 1

            print(f"Computer picks {choice} stick(s).")
            sticks -= choice

            if sticks == 0:
                print("Computer picked the last stick.")
                print("🎉 You win!")
                break

        user_starts = not user_starts


# --------- Main Program ---------

n = int(input("Enter total number of sticks: "))
start = input("Do you want to start first? (y/n): ").lower()

game(n, start == 'y')
