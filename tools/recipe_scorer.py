import random

RECIPES = [
    {"name": "Veg Omelette", "ingredients": ["eggs", "onion", "tomato"]},
    {"name": "Fried Rice", "ingredients": ["rice", "onion", "egg"]},
    {"name": "Grilled Cheese", "ingredients": ["bread", "cheese"]},
    {"name": "Fruit Salad", "ingredients": ["apple", "banana", "yogurt"]},
    {"name": "Pasta Delight", "ingredients": ["pasta", "cheese", "tomato"]},
    {"name": "Chicken Stir Fry", "ingredients": ["chicken", "onion", "beans"]},
    {"name": "Tomato Soup", "ingredients": ["tomato", "salt", "onion"]},
    {"name": "Banana Shake", "ingredients": ["banana", "milk", "yogurt"]},
]

def get_scored_recipes(inventory_items):
    recipes = RECIPES.copy()
    random.shuffle(recipes)  # randomize base order

    scored = []
    for recipe in recipes:
        score = sum(1 for ing in recipe["ingredients"] if ing in inventory_items)
        score += random.randint(0, 1)  # add small randomness
        scored.append((score, recipe))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [r for score, r in scored]
