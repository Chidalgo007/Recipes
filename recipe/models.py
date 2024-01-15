from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    img = models.URLField()
    difficulty = models.CharField(max_length=20)
    prep = models.IntegerField()
    cooking = models.IntegerField()
    total = models.IntegerField()
    ingredients = models.CharField(max_length=9999)
    instruction = models.CharField(max_length=9999)

    def get_ingredients_list(self):
        return self.ingredients.split(',')

    def get_instruction_list(self):
        return self.instruction.split('Step')