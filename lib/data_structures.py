spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_list = list()
    for food in spicy_foods:
        spicy_list.append(food["name"])
    return spicy_list

def get_spiciest_foods(spicy_foods):
    spiciest_list = list()
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_list.append(food)
    return spiciest_list

def print_spicy_foods(spicy_foods):
    emoji = '🌶'
    for food in spicy_foods:
        heat_level=food["heat_level"] * emoji
        print (f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    emoji='🌶'
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level=food["heat_level"] * emoji
            print (f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    

def create_spicy_food(spicy_foods, spicy_food):
    pass
