from datetime import date

USERS = [
    {
        "id": 1,
        "name": "Alice",
        "genre": "SciFi",
        "posts": [
            {"id": 101, "title": "First Post", "created": date(2023, 1, 10)},
            {"id": 102, "title": "Second Post", "created": date(2023, 2, 15)},
        ],
    },
    {
        "id": 2,
        "name": "Bob",
        "genre": "Fantasy",
        "posts": [{"id": 201, "title": "Hello World", "created": date(2023, 3, 20)}],
    },
    {"id": 3, "name": "Carol", "genre": "Mystery", "posts": []},
    {
        "id": 4,
        "name": "David",
        "genre": "Biography",
        "posts": [
            {"id": 301, "title": "My Journey", "created": date(2023, 4, 25)},
            {"id": 302, "title": "Learning Python", "created": date(2023, 5, 30)},
        ],
    },
    {
        "id": 5,
        "name": "Eve",
        "genre": "SciFi",
        "posts": [{"id": 401, "title": "New Beginnings", "created": date(2023, 6, 5)}],
    },
    {"id": 6, "name": "Frank", "genre": "Fantasy", "posts": []},
    {
        "id": 7,
        "name": "Grace",
        "genre": "Mystery",
        "posts": [
            {"id": 501, "title": "Tech Trends", "created": date(2023, 7, 10)},
            {"id": 502, "title": "AI and Future", "created": date(2023, 8, 15)},
        ],
    },
    {
        "id": 8,
        "name": "Hank",
        "genre": "Biography",
        "posts": [{"id": 601, "title": "Travel Diary", "created": date(2023, 9, 20)}],
    },
    {
        "id": 9,
        "name": "Ivy",
        "genre": "SciFi",
        "posts": [],
    },
    {"id": 10, "name": "Jack", "genre": "Fantasy", "posts": []},
]
