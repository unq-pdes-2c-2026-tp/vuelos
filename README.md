# vuelos

## Authors
- Elizabeth Gasañol
- Federico Martinez
- Pablo Pissi

## Installation

```bash
docker build --no-cache .
```

## Create migrations
```bash
python manage.py makemigrations
```

## Running the api
```bash
docker compose up -d
```
## Creating mock flights
```bash
docker compose exec vuelos python manage.py crear_vuelos
```
