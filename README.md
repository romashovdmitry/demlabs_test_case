# demlabs_test_case
Django Test Case for Demlabs.

Screencast illustrating main project's functionality: [click_me](https://youtu.be/xx50t_QjUTg)

## Quick Start

1. Clone the repository

```
git init
git clone https://github.com/romashovdmitry/demlabs_test_case/
```

2. There is a file example.env. Open this file, pass your comfortable values to variables and change name to .env.

Plz, don't forget about Telegram ENVs.

If Django would be created too long just comment two lines with Admin LTE

```
INSTALLED_APPS = [
    # beatiful admin panel
    "adminlte3",
    "adminlte3_theme",
```

4. Run docker compose 

```
docker compose up --build
```

# How to create new product?

New products could be created by [Admin panel:](http://127.0.0.1:8001/admin/)

## Stack

- [ ] Docker, docker compose for containerization
- [ ] Framework: Django
- [ ] API: Django Rest Framework (DRF)
- [ ] Database: PostgreSQL
- [ ] Swagger for describing implemented methods in OpenAPI format
- [ ] Redis: for processing user's basket
- [ ] aiogramm: for processing updates from bot
- [ ] pytest: couple simple tests (need more)

# Swagger UI

Link to [Swagger UI](http://127.0.0.1:8001/api/docs/)

# TODO:

- Websockets for order status tracking
- more tests
- endpoint for payment webhooks/pushs/any other methods.
- more details in Product model
- maybe, it's better to divide basket from order views
