import random

import re

class IngredientAgent:
    def process(self, text):
        text = text.lower()
        # replace commas and slashes with space
        text = text.replace(",", " ").replace("/", " ")
        # keep words with letters, hyphens, digits
        tokens = re.findall(r"[a-z0-9\-]+", text)
        return tokens



class RecipeAgent:
    """
    This agent generates a simple recipe using rule-based logic.
    """

    def generate_recipe(self, ingredients):
        recipes = {
            "potato": "Crispy Masala Aloo",
            "tomato": "Tomato Soup",
            "paneer": "Paneer Bhurji",
            "rice": "Veg Fried Rice",
            "onion": "Caramelized Onion Curry",
            "milk": "Sweet Milk Dessert"
        }

        found = [recipes[i] for i in ingredients if i in recipes]

        if found:
            return f"You can make: {random.choice(found)}"
        return "No matching recipe found! Try adding more ingredients."
