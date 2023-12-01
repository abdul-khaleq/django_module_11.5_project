from django.shortcuts import render

# Create your views here.
meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "strdesc": "BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the pastry"
        }
    ]
def index(request):
    return render(request, 'index.html', {'meals':meals})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')