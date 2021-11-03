from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Bludo, Ingredient 



def home(request):
    try:
        bludo_id = int(request.GET.get("bludo_id"))
    except (ValueError, TypeError):
        bludo_id = None
        default_select1 = 'Выберите блюдо'
    try:
        ingredient_id = int(request.GET.get("ingredient_id"))
    except (ValueError, TypeError):
        ingredient_id = None
        default_select2 = 'Выберите ингредиент'
        
    result_select = []
    def GroupBy(dict):
        for t1 in dict:
            result_select.append({'bludo': t1, 'ingredients': t1.ingredients.all()})    

    if bludo_id and not(ingredient_id):     # Если выбрали блюдо 
        default_select1 = str(Bludo.objects.filter(id=bludo_id)[0])
        default_select2 = 'Выберите ингредиент'
        temp = Bludo.objects.all().filter(nazvanie=default_select1)
        GroupBy(temp)

    if not(bludo_id) and ingredient_id:   # Если выбрали ингредиент
        default_select1 = 'Выберите блюдо'
        default_select2 = str(Ingredient.objects.filter(id=ingredient_id)[0])
        temp = Bludo.objects.all().filter(ingredients__nazvanie=default_select2).order_by('nazvanie')
        GroupBy(temp)
 
    if not(bludo_id) and not(ingredient_id): # если ничего не выбранно отправляем список всех блюд
        tempbludo = Bludo.objects.all()
        for t1 in tempbludo:
            result_select.append({'bludo': t1, 'ingredients': t1.ingredients.all()})

    List_bludo = Bludo.objects.all()      #заполняем первый селект списком рецептов
    List_ingredient = Ingredient.objects.all()   #заполняем второй селект списком ингредиентов

    return render(
        request,
        'home.html', 
        {   'default_select1'   : default_select1 , 
            'default_select2'   : default_select2,
            'select_bludo'      : List_bludo,       # отправляем на страницу список блюд
            'select_ingredient' : List_ingredient,  # отправляем на страницу список ингредиентов
            'result_select'     : result_select,       # отправляем на страницу результат запроса
        }
    )

