from fastfood_restaurant.models import *

user1 = User(email='nikname21@gmail.com', password='defender42')
client1 = Client(name=' Азат Соколов', card_number='4147 5657 9878 9009')
user2 = User(email='altywa1998@gmail.com', password='nono34')
worker2 = Worker(name='Алтынай Алиева', position='Оператор кассы')
food1 = Food(name='Шаурма', start_price=50)
food2 = Food(name='Гамбургер', start_price=25)
ingr1 = Ingredient(name='сыр', extra_price=10)
ingr2 = Ingredient(name='курица', extra_price=70)
ingr3 = Ingredient(name='говядина', extra_price=80)
ingr4 = Ingredient(name='салат', extra_price=15)
ingr5 = Ingredient(name='фри', extra_price=15)

n1 = Order.objects.add(food1, ingr3, ingr1, ingr4, ingr5)
n2 = Order.objects.add(food2, ingr2, ingr4)

order1 = Order.objects.get(id=1)
total_cost = order1.total_cost()

order2 = Order.objects.get(id=2)
total_cost = order1.total_cost()

