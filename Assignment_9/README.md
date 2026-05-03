# Django REST API - Assignment 9

This project is a **User Profile Management API** built with Django and Django REST Framework (DRF).
It allows authenticated users to create, view, update, and delete their own profile.

---

## 📌 What this project does

* Create a user profile 👤
* View profile details 📄
* Update profile information ✏️
* Delete profile ❌
* Only authenticated users can access the API 🔐
* Search, filter, and order profiles 🔍

---

## 🚀 Features

* Built using Django REST Framework
* Uses **Generic API Views** (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`)
* One-to-one relationship between user and profile
* Only the profile owner can update or delete
* Search by username, bio, or location
* Filter profiles by location or username
* Order results by ID

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <https://github.com/nishant8105/Practice-Assignment.git>
cd <Practice-Assignment/Assignment_9>
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Required packages include:

* Django
* djangorestframework
* django-filter
* Pillow


---

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

---

### 5. Run the server

```bash
python manage.py runserver
```

---

## 🌐 API Base URL

```id="m0w8tv"
http://localhost:8000/api/
```

---

## 📡 API Endpoints

### 🔹 List or Create Profiles

* **GET** `/api/users/` → List profiles
* **POST** `/api/users/` → Create profile

---

### 🔹 Retrieve / Update / Delete Profile

* **GET** `/api/users/<id>/`
* **PUT/PATCH** `/api/users/<id>/`
* **DELETE** `/api/users/<id>/`

---

## 🔍 Filtering, Searching, Ordering

### Filter by location:

```id="a9r8p2"
GET /api/users/?location=pune
```

### Filter by username:

```id="4m1szt"
GET /api/users/?username=rahul
```

### Search:

```id="o1zt7w"
GET /api/users/?search=developer
```

### Ordering:

```id="6i7o1r"
GET /api/users/?ordering=id
```

---

## 🔐 Authentication

* Uses Django session authentication
* Login at:

```id="f3j1bz"
/api-auth/login/
```

---

## 🧪 Running Tests

Run all tests:

```bash
python manage.py test
```

Run specific app tests:

```bash
python manage.py test userProfile
```

---


## 📁 Project Structure (Simplified)

```
restAPI/
│   settings.py
│   urls.py
│
userProfile/
│   models.py
│   views.py
│   serializers.py
│   permissions.py
│   filters.py
│   urls.py
│   tests.py
```