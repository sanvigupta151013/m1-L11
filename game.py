# ================================
# NUMBER GUESSING GAME
# ================================

# ---------- SETTINGS (given to you) ----------
secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print(" 🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

while count < max_attempts and guess != secret:
    guess = int(input("Enter your number here: "))
    count += 1     

    if guess == secret:
        print("you won the game!🌟")
        print("congratulation! you are a good guesser!🥳")

    else:
        
        
    #diff>=20 = ice cold
    # diff >= 10 = cold
    # diff >= 5 = warm
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        if diff >= 20:
            print("ice cold🥶")  

        elif diff >= 10:
            print("cold❄️")

        elif diff >= 5:
            print("warm🫠")

        else:
            print("you are wrong")

        remaining = max_attempts - count

        if remaining > 0:
            print("💓")
            for i in range(remaining):
                print("💓", end=" ")
            print()
    
if guess != secret:
    print(f"☠️Game over.")
    print(f"The secret number was: {secret}")   
    print("Better luck next time!")