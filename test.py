
secret = 27
guess = int(input("enter a number here: "))
i = 0
num = i

#very cold = too low
# cold = low
# warm = high
# hot = very high
subtract = secret - guess
    
if secret == guess:
    print("hot🥵") 

elif secret >= 30:
    print("warm🫠")

elif secret >= 20:
    print("win🌟")

elif secret >=10:
    print("cold❄️")

elif secret >=5:
    print("very cold🥶")

else:
    print("you have failed. Try again.you lose")

