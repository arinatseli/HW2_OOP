# test_recipes.py
import pytest
from cooking.ingredient import Ingredient
from cooking.recipe import Recipe
from cooking.shopping_list import ShoppingList

class TestIngredient:
    """Тесты для класса Ingredient"""

    def test_ingredient_1(self):
        ingredient = Ingredient("Мука", 500.0, "г")
        assert ingredient.name == "Мука"
        assert ingredient.quantity == 500.0
        assert ingredient.unit == "г"

    def test_ingredient_2(self):
        ingredient = Ingredient("Мука", 500, "г")
        assert ingredient.quantity == 500.0
        assert isinstance(ingredient.quantity, float)

    def test_ingredient_3(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", -5.0, "г")

    def test_ingredient_4(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", 0, "г")

    def test_ingredient_str_1(self):
        ingredient = Ingredient("Мука", 500.0, "г")
        assert str(ingredient) == "Мука: 500.0 г"

    def test_ingredient_str_2(self):
        ingredient = Ingredient("Мука", 500, "г")
        assert str(ingredient) == "Мука: 500.0 г"

    def test_ingredient_eq_1(self):
        ingredient1 = Ingredient("Мука", 500.0, "г")
        ingredient2 = Ingredient("Мука", 1000.0, "г")
        assert ingredient1 == ingredient2

    def test_ingredient_eq_2(self):
        ingredient1 = Ingredient("Мука", 500.0, "г")
        ingredient2 = Ingredient("Сахар", 500.0, "г")
        assert ingredient1 != ingredient2

    def test_ingredient_eq_3(self):
        ingredient1 = Ingredient("Мука", 500.0, "г")
        ingredient2 = Ingredient("Мука", 500.0, "кг")
        assert ingredient1 != ingredient2


class TestRecipe:
    """Тесты для класса Recipe"""

    def test_recipe_1(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        ingredients = [flour, water]
        recipe = Recipe("Хлеб", ingredients)
        assert recipe.title == "Хлеб"
        assert recipe.ingredients == ingredients

    def test_recipe_2(self):
        recipe = Recipe("Пустое блюдо")
        assert recipe.title == "Пустое блюдо"
        assert recipe.ingredients == []

    def test_recipe_3(self):
        recipe = Recipe("Пустое блюдо", None)
        assert recipe.title == "Пустое блюдо"
        assert recipe.ingredients == []

    def test_add_ingredient_1(self):
        recipe = Recipe("Хлеб")
        water = Ingredient("Вода", 300, "мл")
        recipe.add_ingredient(water)
        assert recipe.ingredients[0] == water

    def test_add_ingredient_2(self):
        recipe = Recipe("Хлеб")
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 250, "г")
        recipe.add_ingredient(flour1)
        recipe.add_ingredient(flour2)
        assert recipe.ingredients[0].name == "Мука"
        assert recipe.ingredients[0].quantity == 750.0
        assert recipe.ingredients[0].unit == "г"

    def test_add_ingredient_3(self):
        recipe = Recipe("Тесто")
        water1 = Ingredient("Вода", 200, "мл")
        water2 = Ingredient("Вода", 100, "л")
        recipe.add_ingredient(water1)
        recipe.add_ingredient(water2)
        assert len(recipe.ingredients) == 2

    def test_scale_1(self):
        flour = Ingredient("Мука", 500, "г")
        recipe = Recipe("Хлеб", [flour])
        scaled_recipe = recipe.scale(2)
        assert recipe.ingredients[0].quantity == 500
        assert scaled_recipe.ingredients[0].quantity == 1000

    def test_scale_2(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        recipe = Recipe("Хлеб", [flour, water])
        scaled_recipe = recipe.scale(2.5)
        assert scaled_recipe.ingredients[0].quantity == 1250.0
        assert scaled_recipe.ingredients[1].quantity == 750

    def test_scale_3(self):
        flour = Ingredient("Мука", 500, "г")
        recipe = Recipe("Хлеб", [flour])
        with pytest.raises(ValueError):
            recipe.scale(-1)

    def test_scale_4(self):
        flour = Ingredient("Мука", 500, "г")
        recipe = Recipe("Хлеб", [flour])
        with pytest.raises(ValueError):
            recipe.scale(0)

    def test_len_1(self):
        recipe = Recipe("Пустое блюдо")
        assert len(recipe) == 0

    def test_len_2(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        recipe = Recipe("Хлеб", [flour, water])
        assert len(recipe) == 2

    def test_len_3(self):
        recipe = Recipe("Хлеб")
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 250, "г")
        recipe.add_ingredient(flour1)
        assert len(recipe) == 1
        recipe.add_ingredient(flour2)
        assert len(recipe) == 1


class TestShoppingList:
    """Тесты для класса ShoppingList"""

    def test_add_recipe_1(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        bread = Recipe("Хлеб", [flour, water])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(bread, 1)
        assert len(shopping_list._items) == 2

    def test_add_recipe_2(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        bread = Recipe("Хлеб", [flour, water])
        shopping_list = ShoppingList()
        with pytest.raises(ValueError):
            shopping_list.add_recipe(bread, -1)

    def test_add_recipe_3(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        bread = Recipe("Хлеб", [flour, water])
        shopping_list = ShoppingList()
        with pytest.raises(ValueError):
            shopping_list.add_recipe(bread, 0)

    def test_remove_recipe_1(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        milk = Ingredient("Молоко", 200, "мл")
        bread = Recipe("Хлеб", [flour, water])
        pancakes = Recipe("Блины", [flour, milk])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(bread, 1)
        shopping_list.add_recipe(pancakes, 1)
        assert len(shopping_list._items) == 4
        shopping_list.remove_recipe("Хлеб")
        assert len(shopping_list._items) == 2
        ingredients = {item[0].name for item in shopping_list._items}
        assert "Мука" in ingredients
        assert "Молоко" in ingredients
        assert "Вода" not in ingredients
        for ingredient, title in shopping_list._items:
            assert title == "Блины"
            assert ingredient.name in ["Мука", "Молоко"]

    def test_remove_recipe_2(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        bread = Recipe("Хлеб", [flour, water])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(bread, 1)
        shopping_list.remove_recipe("Блины")
        assert len(shopping_list._items) == 2

    def test_get_list_1(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        bread1 = Recipe("Хлеб 1", [flour, water])
        bread2 = Recipe("Хлеб 2", [flour, water])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(bread1, 1)
        shopping_list.add_recipe(bread2, 1)
        result = shopping_list.get_list()
        flour_result = None
        for ingr in result:
            if ingr.name == "Мука":
                flour_result = ingr
                break
        assert flour_result is not None
        assert flour_result.quantity == 1000.0

    def test_get_list_2(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        salt = Ingredient("Соль", 10, "г")
        bread = Recipe("Хлеб", [flour, water, salt])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(bread, 1)
        result = shopping_list.get_list()
        names = [ingr.name for ingr in result]
        assert names == sorted(names)
        assert names == ["Вода", "Мука", "Соль"]

    def test_add_1(self):
        """Проверка: объединение двух списков покупок"""
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        salt = Ingredient("Соль", 10, "г")
        bread = Recipe("Хлеб", [flour, water])
        dough = Recipe("Тесто", [flour, water, salt])
        list1 = ShoppingList()
        list2 = ShoppingList()
        list1.add_recipe(bread, 1)
        list2.add_recipe(dough, 1)
        sum = list1 + list2
        assert len(sum._items) == 5

    def test_add_2(self):
        flour = Ingredient("Мука", 500, "г")
        water = Ingredient("Вода", 300, "мл")
        bread = Recipe("Хлеб", [flour, water])
        list1 = ShoppingList()
        list2 = ShoppingList()
        list1.add_recipe(bread, 1)
        list2.add_recipe(bread, 1)
        orig_len1 = len(list1._items)
        orig_len2 = len(list2._items)
        sum = list1 + list2
        assert len(list1._items) == orig_len1
        assert len(list2._items) == orig_len2
        assert len(sum._items) == orig_len1 + orig_len2
