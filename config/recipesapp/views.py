from django.shortcuts import render


def recipe_view(request):
    recipe_name = request.GET.get("recipe")  
    
    recipe = None

    recipes = {
        "goulash": "Рецепт гуляша: мясо, лук, paprika, томаты.",
        "dumplings": "Рецепт вареников: тесто, картошка, лук, сметана.",
    }

    if recipe_name in recipes:
        recipe = recipes[recipe_name]
    else:
        recipe = "Рецепт не найден. Попробуйте другой."

    return render(
        request, "recipe.html", {"recipe_name": recipe_name, "recipe": recipe}
    )
