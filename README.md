# Django Auth System

Проект представляет собой систему аутентификации пользователей с расширенными профилями, созданную на Django. Включает регистрацию, вход/выход, управление профилем и защищенные страницы.
![2025-06-18_19-56-11](https://github.com/user-attachments/assets/99e63230-375a-4363-a15b-a9da4311930d)
![2025-06-18_19-56-59](https://github.com/user-attachments/assets/543a1296-f29c-4757-a034-1096808abf4b)

## Основные возможности

- 🔐 Регистрация новых пользователей
- 🔑 Аутентификация пользователей
- 👤 Профиль пользователя с расширенными полями:
  - Имя пользователя
  - Имя и фамилия
  - Email
  - Телефон
  - Адрес
- 🛡️ Защита страниц:
  - Главная страница - доступна всем
  - Профиль - только для авторизованных пользователей
- 📱 Полностью адаптивный дизайн с использованием Bootstrap 5
- ✅ Валидация данных (особенно для номера телефона)

## Технологии

- Python 3.10+
- Django 4.2+
- Bootstrap 5
- SQLite (для разработки)

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/auth_test_hw.git
cd auth_test_hw
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Соберите статические файлы:
```bash
python manage.py collectstatic
```

6. Создайте суперпользователя (опционально):
```bash
python manage.py createsuperuser
```

7. Запустите сервер разработки:
```bash
python manage.py runserver
```

8. Откройте в браузере: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Структура проекта

```
auth_test_hw/
├── auth_test_hw/          # Основная конфигурация проекта
│   ├── settings.py        # Настройки проекта
│   ├── urls.py            # Главные URL-маршруты
│   └── ...
├── main/                  # Приложение "main"
│   ├── migrations/        # Миграции базы данных
│   ├── static/            # Статические файлы
│   │   └── main/
│   │       └── css/
│   │           └── style.css
│   ├── templates/         # Шаблоны
│   │   └── main/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── login.html
│   │       ├── profile.html
│   │       └── register.html
│   ├── admin.py           # Админ-панель
│   ├── apps.py            # Конфигурация приложения
│   ├── forms.py           # Формы
│   ├── models.py          # Модели данных
│   ├── tests.py           # Тесты
│   ├── urls.py            # URL-маршруты приложения
│   └── views.py           # Представления
├── .gitignore             # Игнорируемые файлы
├── db.sqlite3             # База данных (разработка)
├── manage.py              # Управляющий скрипт
├── README.md              # Этот файл
└── requirements.txt       # Зависимости
```

## Используемые страницы

- **Главная страница**: `/`
- **Регистрация**: `/register/`
- **Вход**: `/login/`
- **Профиль**: `/profile/` (только для авторизованных)
- **Выход**: `/logout/`

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для получения дополнительной информации.
