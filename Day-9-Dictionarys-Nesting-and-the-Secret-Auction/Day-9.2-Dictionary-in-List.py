"""
DICTIONARY IN LIST
Instructions

You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains
2 Dictionaries.

Write a function that will work with the following line of code to add the entry for Russia to the travel_log:
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.
You've been to Moscow and Saint Petersburg.
"""

travel_log = [
    {
        "Country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


def add_new_country(countries_visited, number_of_visits, cities_visited):
    new_entry = {
        "Country": countries_visited,
        "Visits": number_of_visits,
        "cities": cities_visited,
    }
    travel_log.append(new_entry)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
