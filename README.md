# **GAME STAT**
REST API сервис для счета статистики. Проект написан на python 3.9.

Стек: FastApi, PostgreSQL, docker-compose, SQLAlchemy, poetry

### **API методы**:
- Метод сохранения статистики
(POST запрос на http://localhost:8000/)

- Метод показа статистики
(GET запрос на http://localhost:8000/)

- Метод сброса статистики
(DEL запрос на http://localhost:8000/)


### **Метод сохранения статистики**.

**Принимает на вход**:
```
date - дата события
views - количество показов (опционально)
clicks - количество кликов (опционально)
cost - стоимость кликов в рублях с точностью до копеек (опционально)
```
Реализована валидация всех полей.

**Пример запроса**:
```
{
  "body": [
    {
      "date": "2023-01-18",
      "views": 39,
      "clicks": 159,
      "cost": 1887.59
    },
    {
      "date": "2023-01-17",
      "views": 73,
      "clicks": 214,
      "cost": 3298.11
    }
  ]
}
```
**Пример вывода**:
```
{
  "message": "Statistics created successfully",
  "result": [
    {
      "date": "2023-01-18",
      "views": 39,
      "clicks": 159,
      "cost": 1887.59
    },
    {
      "date": "2023-01-17",
      "views": 73,
      "clicks": 214,
      "cost": 3298.11
    }
  ]
}
```

### **Метод показа статистики**
**Принимает на вход**:
```
date_from - дата начала периода (включительно)
date_to - дата окончания периода (включительно)
order_by - поле, по которому требуется отсортировать ответ (по умолчанию поле date)
```
Реализована валидация всех полей.

**Результат**:
```
date - дата события
views - количество показов (опционально) 
clicks - количество кликов (опционально) 
cost - стоимость кликов (опционально) 
cpc = средняя стоимость клика (cost/clicks) (опционально) 
cpm = средняя стоимость 1000 показов (cost/views * 1000) (опционально) 
```
**Пример запроса**:
```
{
  "date_from": "2022-01-20",
  "date_to": "2022-04-20",
  "order_by": "views"
}
```
**Пример вывода**:
```
[
  {
    "date": "2022-02-26",
    "views": 3686,
    "clicks": 189,
    "cost": 61887.59,
    "cpc": 327.45,
    "cpm": 16789.91
  },
  {
    "date": "2022-03-30",
    "views": 3686,
    "clicks": 189,
    "cost": 61887.59,
    "cpc": 327.45,
    "cpm": 16789.91
  }
]
```

### **Метод сброса статистики**
Удаляет всю сохраненную статистику.

**Пример вывода**:
```
{
  "message": "Statistics deleted successfully"
}
```
Встроенная документация FastAPI: http://localhost:8000/docs#/


## **Запуск проекта**.
Склонировать проект:
```
git pull https://github.com/thegastroler/game_stat
```
В корневой папке проекта:
```
docker-compose up -d --build
```
Проект готов к работе.

Для просмотра БД переходим в админ-панель pgAdmin 
http://localhost:5050/
```
login: admin@admin.com
password: admin
```

Далее подключаемся к БД:
```
Object -> Register -> Server...
name: game_stat
```
Во вкладке **Connection**:
```
Host name: db
Port: 5432
Maintenance database: postgres
Username: postgres
Password: postgres
```
Просмотр таблицы по пути:
```
game_stat -> Databases -> postgres -> Schemas -> public -> Tables
```

