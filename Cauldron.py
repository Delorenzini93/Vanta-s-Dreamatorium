from inventory import add_item, remove_item, has_item
import Status

discovered_recipes = set()

basic_combinations = {
    frozenset(["Tomato", "Salt"]): "Tomato Paste",
    frozenset(["Flour", "Water", "Salt"]): "Dough",
    frozenset(["Milk", "Butter"]): "Cream",
    frozenset(["Bone", "Water"]): "Broth",
    frozenset(["Ash", "Water"]): "Lye",
    frozenset(["Honey", "Lemon"]): "Syrup",
    frozenset(["Berry", "Sugar"]): "Jam",
    frozenset(["Ginger", "Honey"]): "Tonic Base",
    frozenset(["Mint", "Water"]): "Mint Extract",
    frozenset(["Wax", "Lavender"]): "Scented Wax",
    frozenset(["Coal", "Sulfur"]): "Black Powder",
    frozenset(["Clay", "Water"]): "Wet Clay",
    frozenset(["Sand", "Coal"]): "Crude Glass",
    frozenset(["Iron Shavings", "Vinegar"]): "Rust Paste",
    frozenset(["Mushroom", "Butter"]): "Mushroom Paste",
    frozenset(["Garlic", "Oil"]): "Garlic Oil",
    frozenset(["Raw Meat", "Salt"]): "Cured Meat",
    frozenset(["Fish", "Salt"]): "Salted Fish",
}
#############################################
recipe_combinations = {
    frozenset(["Dough", "Tomato Paste", "Mushroom Paste"]): {
        "recipe_name": "Savory Pie Recipe",
        "with_recipe": "Savory Pie",
        "without_recipe": "Dough",
    },
    frozenset(["Broth", "Carrot", "Celery"]): {
        "recipe_name": "Stew Recipe",
        "with_recipe": "Hearty Stew",
        "without_recipe": "Thin Broth",
    },
    frozenset(["Tonic Base", "Mint Extract", "Ash"]): {
        "recipe_name": "Smoke Elixir Recipe",
        "with_recipe": "Smoke Elixir",
        "without_recipe": "Murky Liquid",
    },
    frozenset(["Tonic Base", "Rust Paste", "Sulfur"]): {
        "recipe_name": "Corrosive Vial Recipe",
        "with_recipe": "Corrosive Vial",
        "without_recipe": "Foul Liquid",
    },
    frozenset(["Wet Clay", "Ash", "Salt"]): {
        "recipe_name": "Hardened Seal Recipe",
        "with_recipe": "Hardened Seal",
        "without_recipe": "Cracked Clay",
    },

}

def discover_recipe(recipe_name):
    discovered_recipes.add(recipe_name)
    print(f"Recipe discovered: {recipe_name}!")

def cauldron():
    print("\nA large cauldron sits in the center of the room, still warm.")

    ingredients = []

    print("Add up to 3 ingredients. Type 'done' when ready.")

    for i in range(3):
        item = input(f"Ingredient {i+1} (or 'done'): ").strip()

        if item.lower() == "done":
            break

        if not has_item(item):
            print(f"You don't have {item}.")
            return

        ingredients.append(item)

    if len(ingredients) < 2:
        print("You need at least 2 ingredients.")
        return

    combo = frozenset(ingredients)

    if combo in recipe_combinations:
        result_data = recipe_combinations[combo]
        recipe_name = result_data["recipe_name"]

        for ingredient in ingredients:
            remove_item(ingredient)

        if recipe_name in discovered_recipes:
            result = result_data["with_recipe"]
            print(f"\nThe cauldron glows intensely...")
            print(f"You obtained: {result}!")
        else:
            result = result_data["without_recipe"]
            print(f"\nSomething comes out of the cauldron, but it feels incomplete...")
            print(f"You obtained: {result}.")

        add_item(result)
        return

    if combo in basic_combinations:
        result = basic_combinations[combo]

        for ingredient in ingredients:
            remove_item(ingredient)

        print(f"\nThe cauldron bubbles...")
        print(f"You obtained: {result}!")
        add_item(result)
        return

    for ingredient in ingredients:
        remove_item(ingredient)

    print("\nThe cauldron bubbles and produces nothing useful...")
    print("The ingredients are lost.")