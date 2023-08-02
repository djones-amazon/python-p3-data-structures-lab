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
    food_names = [food.get("name") for food in spicy_foods] 
    return food_names

def get_spiciest_foods(spicy_foods):
    spice_over_five = [food for food in spicy_foods if food.get("heat_level") > 5]
    return spice_over_five

def print_spicy_foods(spicy_foods):
    heat_emoji = '🌶'
    for i in range(3):
        current_food = spicy_foods[i]
        print(f"{current_food.get('name')} ({current_food.get('cuisine')}) | Heat Level: {heat_emoji * current_food.get('heat_level')}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    selected_food = [food for food in spicy_foods if food.get('cuisine') == cuisine][0]
    return selected_food

def print_spiciest_foods(spicy_foods):
    spice_over_five = get_spiciest_foods(spicy_foods)
    heat_emoji = '🌶'
    for i in range(len(spice_over_five)):
        current_food = spice_over_five[i]
        print(f"{current_food.get('name')} ({current_food.get('cuisine')}) | Heat Level: {heat_emoji * current_food.get('heat_level')}")

def get_average_heat_level(spicy_foods):
    heat_vals = [food.get("heat_level") for food in spicy_foods]
    ave_heat = int(sum(heat_vals) / len(heat_vals))
    return ave_heat

def create_spicy_food(spicy_foods, spicy_food):
    new_list = spicy_foods.copy()
    new_list.append(spicy_food)
    return new_list
