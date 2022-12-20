# Unit 2 Assignment: Using Conditional Logic
# Zackary Sell
# IT244: Python Programming
# Purdue University Global
# Prof. Amitava Karmaker
# December 19, 2022



# This is telling the user what their choices of colors are. I added some space around the sentence for better viewing
print(f"\nYour color choices are red, blue, green, white or yellow.\n")

# This is getting input from the user using the colors provided
userColor = input("Enter a choice from the list above: ")
userColor = userColor.lower()

#These are the possible colors available
possible_colors = ["red", "blue", "green", "white", "yellow"]

validColor = True

# This is the start of the if/elif/else statements converting the input to the Spanish variants
if userColor == "red":
    spanishColor = "rojo"
elif userColor == "blue":
    spanishColor = "azul"
elif userColor == "green":
    spanishColor = "verde"
elif userColor == "white":
    spanishColor = "blanco"
elif userColor == "yellow":
    spanishColor = "amarillo"
else:
    validColor = False

# This is displaying the phrase to let the user know the color they entered as well as the Spanish form. 
# The 'else' statement is if there is anything entered not among the list and to output an error
if validColor:
    print("The color", userColor , "in Spanish is " + spanishColor)
else:
    print("\nThat is not a valid color for this program. Ese no es un color valido.\n")
