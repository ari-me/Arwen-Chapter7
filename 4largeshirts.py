#Chapter 7 - Exercise 4
#Using the same code in exercise 3, make the default of size "L" and the default of text "I love Python"
def make_shirt(size = "L", text = "I love Python"):
    print(f"The shirt you want is size {size} with the text '{text}'.")
make_shirt() #Print the default
make_shirt("M") #Print the default message with a different size
make_shirt(text = "Happiness", size = "XS") #Print with different size and message