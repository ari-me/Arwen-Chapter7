#Chapter 7 - Exercise 5
#a function that accepts the name of a city and country (the country having a default)
def describe_city(city, country = "U A E"):
    print(f"{city.title()} is in {country.title()}")
#Call function for three different cities, at least one not the default country
describe_city("Dubai")
describe_city("Tokyo", "Japan")
describe_city("Manila", "Philippines")