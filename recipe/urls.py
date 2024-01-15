from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>', views.recipe, name='recipe'),
]
