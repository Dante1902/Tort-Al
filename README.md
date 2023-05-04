# Основная информация

![Python-3.10.6](https://img.shields.io/badge/Python-v3.10.6-blue?style=for-the-badge)

---
+ cgi-bin ([cgi-bin](https://github.com/Dante1902/Tort-Al/tree/SP-Kursovaya/cgi-bin)) Здесь находяться основные скрипты для работы на сервере

Для работы веб-сервера необходимо запустить ***start_server_windows.py*** со следующими библиотеками: 

```python
from http.server import HTTPServer, CGIHTTPRequestHandler
```

Необходимые библиотеки для работы ***obrabotka.py*** (обработка входных данных):

```python
import cgi
```

Необходимо библиотеки для работы ***Upload.py*** (для загрузки файла):

```python 
import cgi
from flask import * 
```
