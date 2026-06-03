from cooking.ingredient import Ingredient
class Recipe:
    def __init__(self, title: str, ingredients: list = None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for ingr in self.ingredients:
            if ingr == ingredient:
                ingr.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return (isinstance(ratio, int) or isinstance(ratio, float)) and ratio > 0

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("ratio должен быть положительным числом")
        newIngredients = []
        for ingr in self.ingredients:
            newQuantity = ingr.quantity * ratio
            newIngredient = Ingredient(ingr.name, newQuantity, ingr.unit)
            newIngredients.append(newIngredient)
        return Recipe(self.title, newIngredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        if not self.ingredients:
            return f"{self.title}: (нет ингредиентов)"
        ingredientsStr = ", ".join(str(ingr) for ingr in self.ingredients)
        return f"{self.title}: {ingredientsStr}"