#Chapter 7 - Exercise 3
#A function that accepts size of shirt and text printed on the shirt
def make_shirt(size, text):
    print(f"The shirt you want is size {size} with the text '{text}'.")
make_shirt("M", "I Love Me <3") #Calling the function using positional arguments
make_shirt(text = "Happiness", size = "L") #Calling the function using keyword arguments