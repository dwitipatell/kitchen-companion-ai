from agents import IngredientAgent, RecipeAgent

def main():
    print("🍳 Welcome to Kitchen Companion AI")

    # user input
    user_ingredients = input("Enter ingredients you have: ")

    # create agents
    ingredient_agent = IngredientAgent()
    recipe_agent = RecipeAgent()

    # step 1: ingredient cleanup
    cleaned_ingredients = ingredient_agent.process(user_ingredients)

    # step 2: generate recipe from processed ingredients
    recipe = recipe_agent.generate_recipe(cleaned_ingredients)

    print("\n✨ Suggested Recipe Based on Your Ingredients:")
    print(recipe)


if __name__ == "__main__":
    main()
