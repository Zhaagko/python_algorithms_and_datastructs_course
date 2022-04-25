"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
"""

import re, requests

regex = r"<a .*href=[\"\']?([\w\d-]+://)?(([\w\d-]+\.)?([\w\d-]+\.)+([\w\d-]+))((:\d\d\d\d)?|(/[\S]+/?)*)[\"\']?.*>"

url = input().strip()

response_text = requests.get(url).text

matches = re.finditer(regex, response_text, re.MULTILINE)

success = []

for match in matches:
    res = match.group(2)
    if len(res) > 0:
        if res not in success:
            success.append(res)

success = list(sorted(success))

for i in success:
    print(i)
