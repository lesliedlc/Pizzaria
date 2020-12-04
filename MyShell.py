import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzaria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

p = Pizza.objects.get(id=1)
print(p.name)

toppings = p.topping_set.all()

for topping in toppings:
    print(topping)