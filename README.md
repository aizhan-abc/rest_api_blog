# 📝 Blog API (FastAPI)

Простой REST API для управления блогом — создание, чтение, обновление и удаление постов.  
Реализовано с помощью **FastAPI** и **SQLAlchemy**, с базой данных **SQLite**.

---

## 🚀 Возможности

- ✨ Создание нового поста  
- 📖 Просмотр всех постов  
- 🔍 Получение конкретного поста по ID  
- ✏️ Обновление поста  
- 🗑️ Удаление поста  
- ❤️ Возможность ставить "лайки" постам  

---

## 🛠️ Технологии

- [FastAPI](https://fastapi.tiangolo.com/) — фреймворк для создания API  
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM для работы с базой данных  
- [Pydantic](https://pydantic-docs.helpmanual.io/) — валидация данных  
- [SQLite](https://www.sqlite.org/) — встроенная база данных  

---

## 📂 Структура проекта

rest_api/
│
├── app/
│ ├── crud.py # Логика работы с БД (CRUD)
│ ├── database.py # Подключение к базе данных
│ ├── main.py # Точка входа (FastAPI приложение)
│ ├── models.py # SQLAlchemy-модели
│ ├── schemas.py # Pydantic-схемы (валидация)
│
├── blog.db # SQLite база данных
├── requirements.txt # Зависимости проекта
├── README.md # Описание проекта
└── docker-compose.yml # Настройки Docker (опционально)

---

## ⚙️ Установка и запуск

1. **Клонируй репозиторий**
   ```bash
   git clone https://github.com/aizhan-abc/blog_api.git
   cd blog_api
Создай и активируй виртуальное окружение
python -m venv venv
source venv/bin/activate   # для macOS/Linux
venv\Scripts\activate      # для Windows
Установи зависимости
pip install -r requirements.txt
Запусти сервер
uvicorn app.main:app --reload
Открой в браузере
http://127.0.0.1:8000
📘 Swagger UI
После запуска приложения открой:
👉 http://127.0.0.1:8000/docs

Здесь доступен удобный интерфейс для тестирования всех эндпоинтов API.

💡 Пример использования API
Создать пост
POST /posts/
{
  "title": "Мой первый пост",
  "content": "Это тестовое содержимое.",
  "author": "Айжан"
}
Поставить лайк
POST /posts/1/like
📄 Лицензия
Этот проект распространяется под лицензией MIT.
Свободно используй, улучшай и экспериментируй ❤️
