from recipe import Recipe
from ingredient import Ingredient


class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        self.diet_type = diet_type
        super().__init__(title, ingredients)

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("ratio должен быть положительным числом")
        scaledRecipe = super().scale(ratio)
        return DietaryRecipe(scaledRecipe.title, self.diet_type, scaledRecipe.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"