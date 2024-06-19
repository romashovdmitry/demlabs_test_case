# demlabs_test_case
Django Test Case for Demlabs.

## Quick Start

1. Clone the repository

```
git init
git clone https://github.com/romashovdmitry/demlabs_test_case/
```

2. There is a file example.env. Open this file, pass your comfortable values to variables and change name to .env.

Plz, don't forget about Telegram ENVs.

4. Run docker-compose 

```
docker compose up
```

# How to create new product?

## Stack

- [ ] Docker, docker compose for containerization
- [ ] Framework: Django
- [ ] API: Django Rest Framework (DRF)
- [ ] Database: PostgreSQL
- [ ] Swagger for describing implemented methods in OpenAPI format
- [ ] Redis: for processing user's basket
- [ ] aiogramm: for processing updates from bot

# Swagger UI

Link to [Swagger UI](http://81.31.244.30:8001/api/docs/)

# TODO:

- Websockets for order status tracking
- more tests
- endpoint for payment webhooks/pushs/any other methods.
- more details in Product model
