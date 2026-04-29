# Django REST API - Assignment 9

This project is a simple **Django REST API** where users can create, read, update, and delete posts.

---

## 📌 What this project does

- Create a post ✍️  
- View all posts 📄  
- Update your own post ✏️  
- Delete your own post ❌  
- Only logged-in users can create posts 🔐  
- Search, filter, and sort posts 🔍  

---

## 🚀 Features

- Built using Django REST Framework (DRF)  
- Only the post owner can edit or delete  
- Search posts by title or content  
- Filter posts by username or date  
- Sort posts by title or creation date  

---

## ⚙️ Setup Overview

- Install required packages (Django, djangorestframework, django-filter) using 'pip install -r requirements.txt' command 
- Activate virtual environment (if not already activated)
- Apply database migrations using 'python manage.py migrate' command
- Create admin user (optional) using 'python manage.py createsuperuser' command
- Run the development server using 'python manage.py runserver' command

---
open in broswer with http://localhost:8000/hello/
## 📡 API Endpoints

### 1. Hello API  
Returns a simple message.

**Endpoint:**  
`/hello/`

---

### 2. Get All Posts  

**Endpoint:**  
`/post/` (replace hello with post in the above URL)

---

### 🔍 Filter / Search / Order

You can refine results using:

- Filter by username  
- Filter by date  
- Search by title or content  
- Order by title or date  

---

### 3. Create Post  

- Requires login  
- Automatically saves the logged-in user as creator  

**Endpoint:**  
`/post/`

---

### 4. Get Single Post  

**Endpoint:**  
`/post/<id>/` (replace post/ with post/<id>/ in the above URL)

---

### 5. Update Post  

- Requires login  
- Only the creator can update  

**Endpoint:**  
`/post/<id>/`

---

### 6. Delete Post  

- Requires login  
- Only the creator can delete  

**Endpoint:**  
`/post/<id>/`

---

## 🧪 Testing

- The project includes tests for all features  
- Tests check CRUD operations and permissions  
- Run tests using 'python manage.py test' command
