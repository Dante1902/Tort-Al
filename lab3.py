import requests

Template = "http://biik.ru/rasp/cg109.htm" # Запрос на сайт Биик Сибгути
b = requests.get(Template) # получение запроса
b.encoding="windows-1251" # кодировка
print(b.text) # вывод на экран
