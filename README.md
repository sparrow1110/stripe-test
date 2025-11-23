# Stripe + Django тестовое


## Все доступные URL

| URL                | Описание                                    |
|--------------------|---------------------------------------------|
| `/item/<id>/`      | Страница отдельного товара                  |
| `/order/<id>/`     | Страница отдельного заказа                  |
| `/admin`           | Админ-панель Django                         |
| `/buy/<id>/`       | Создание Stripe Checkout Session для товара |
| `/buy-order/<id>/` | Создание Stripe Checkout Session для заказа |
| `/success/`        | Страница после успешной оплаты              |
| `/cancel/`         | Страница при отмене оплаты                  |


## Запуск локально

```bash
git clone https://github.com/sparrow1110/stripe-test.git
cd stripe-test

cp .env.example .env                 # при необходимости отредактировать
docker-compose up --build
```

После запуска проект доступен по адресу:  
http://localhost:8000

Админка: http://localhost:8000/admin (admin / root - логин / пароль по умолчанию)
