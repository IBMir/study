from jinja2 import Template

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 2, 'city': 'Санкт-Петербург'},
    {'id': 3, 'city': 'Новосибирск'},
    {'id': 4, 'city': 'Екатеринбург'},
    {'id': 5, 'city': 'Казань'},
    {'id': 6, 'city': 'Нижний Новогород'},
]

link = '''<select name='cities'>
{% for c in cities -%}
{% if c.id > 3 -%}
    <option value='{{c["id"]}}'>{{c['city']}}</option>
{% else -%}
    {{ c['city'] }}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

# print(msg)

cars = [
    {'model': 'Volkswagen Tiguan', 'price': 5700000},
    {'model': 'Renault Sandero', 'price': 2000000},
    {'model': 'Mercedes-Benz E-Класс', 'price': 11000000},
    {'model': 'BMW 3 серии', 'price': 7800000},
    {'model': 'Renault Logan', 'price': 1700000},
    {'model': 'Toyota Camry', 'price': 5000000},
    {'model': 'BMW X5', 'price': 16000000},
]

tpl = 'Суммарная стоимость равна - {{ cr | sum(attribute="price") }}'
tp = Template(tpl)
cs = tp.render(cr=cars)
# print(cs)

persons = [
    {'name': 'Мария'},
    {'name': 'Федор'},
    {'name': 'Сергей'},
    {'name': 'Владимир'},
    {'name': 'Ольга'},
    {'name': 'Алексей'},
]

tmp = '''
{%- for p in persons -%}
{% filter upper %} {{ p.name }} {% endfilter %}
{% endfor -%}
'''

tm = Template(tmp)
# print(tm.render(persons=persons))