# HW2_OOP - система для управления рецептами

## Краткое описание
Это консольное приложение, которое позволяет создавать блюда, добавлять их в "рецепты", масштабировать порции и генерировать список покупок.

## Использование

## Как запустить код

```bash
python -c "from cooking.ingredient import Ingredient; print(Ingredient('Мука', 500, 'г'))"
```

Или создайте файл `main.py`:

```python
from cooking.ingredient import Ingredient

ingredient = Ingredient("Мука", 500, "г")
print(ingredient)
```

И запустите:

```bash
python main.py
```
## Установка
```bash
git clone https://github.com/arinatseli/HW2_OOP.git
cd HW2_OOP
pip install -r requirements.txt
```
## Запуск тестов
```bash
pytest
```
## Автор
Целищева Арина Борисовна, группа ББИ2508