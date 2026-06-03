from ingredient import Ingredient
from recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("portions должно быть положительным")
        scaledRecipe = recipe.scale(portions)
        for ingredient in scaledRecipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self):
        ingredientsDict = {}
        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in ingredientsDict:
                ingredientsDict[key] += ingredient.quantity
            else:
                ingredientsDict[key] = ingredient.quantity
        result = []
        for (name, unit), quantity in ingredientsDict.items():
            result.append(Ingredient(name, quantity, unit))
        result.sort(key=lambda ingr: ingr.name)
        return result

    def __add__(self, other: 'ShoppingList'):
        if not isinstance(other, ShoppingList):
            raise TypeError("Нельзя добавить other, у него неверный тип")
        newList = ShoppingList()
        newList._items = self._items + other._items
        return newList