"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
"""

import json

data = json.loads(input())

child_count = {i["name"]:0 for i in data}
data = {i["name"]:i["parents"] for i in data}

used_list = []

def find_parents(cur_class, classes):
    global used_list

    if classes[cur_class] == []:
        if cur_class not in used_list:
            child_count[cur_class] += 1
            used_list.append(cur_class)
    else:
        if cur_class not in used_list:
            child_count[cur_class] += 1
            used_list.append(cur_class)
        for class_name in classes[cur_class]:
            find_parents(class_name, classes)


for class_name in data.keys():
    find_parents(class_name, data)
    used_list = []

child_count = [f"{k} : {v}" for k, v in child_count.items()]
child_count.sort()

for i in child_count:
    print(i)
