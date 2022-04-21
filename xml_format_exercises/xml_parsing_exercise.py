"""
Текст задания:

Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
"""


"""Решение"""
from xml.etree import ElementTree
# from sys import stdin

cubes = {"red":0, "green":0, "blue":0}

def calcDepthForAllCHildrens(elem, depth=1):
    global cubes

    cubes[elem.attrib["color"]] += depth

    depth += 1

    for child in elem:
        calcDepthForAllCHildrens(child, depth)

xml_tree = ElementTree.parse("test.xml") # in real exercise use stdin instead of "test.xml"
root = xml_tree.getroot()

calcDepthForAllCHildrens(root, 1)

print(cubes["red"], cubes["green"], cubes["blue"])
