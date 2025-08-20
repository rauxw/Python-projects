people = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}

new_dict = {key:value for (key,value) in people.items() if value >= 30}

print(new_dict)