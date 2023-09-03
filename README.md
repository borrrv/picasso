<!-- README.md -->
+ [![cov](https://<you>.github.io/borrrv/badges/coverage.svg)](https://github.com/borrrv/picasso/actions)
# Тестовое задание для Picasso
## Запуск проекта
- Введите команду
```
sudo docker-compose up -d --build
```
- Проект готов к работе
## Эндпоинты (относительно http://localhost/)
- (POST) Загрузка файлов

```/api/upload/```

![screenshot](https://github.com/borrrv/picasso/blob/main/images/upload.png?raw=true)
- (GET) Получить список файлов

```/api/files/```

```response```:
```
[
    {
        "id": 2,
        "file": "http://localhost/media/uploads/703037506_PG0kXDX.jpeg",
        "uploaded_at": "2023-09-03T15:20:19.804953+03:00",
        "processed": true
    },
    {
        "id": 1,
        "file": "http://localhost/media/uploads/703037506.jpeg",
        "uploaded_at": "2023-09-03T15:07:04.313369+03:00",
        "processed": true
    }
]
```
- Coverage
![screenshot](https://github.com/borrrv/picasso/blob/main/images/coverage.png?raw=true)