# Django Blog Platform

A multi-user blog platform built with Django, featuring authentication, role-based permissions, and a fully customized Django Admin interface for content management.

This project demonstrates production-style backend development using Django’s ORM, authentication system, and admin tooling.

---

## 🚀 Features

- User authentication (signup, login, logout)
- Create, read, update, and delete blog posts
- Comment system
- Role-based permissions (users can only manage their own content)
- Fully customized Django Admin dashboard
- PostgreSQL database integration
- Clean MVC/MVT architecture
- Secure data handling and authorization
- Production-ready project structure

---

## 🛠 Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL
- **Authentication:** Django Auth
- **Admin Interface:** Django Admin (customized)
- **Frontend:** Django Templates + HTML/CSS
- **Version Control:** Git & GitHub

---

## 📸 Screenshots

> *(Add screenshots here if you want — admin panel, homepage, post detail page)*

---

## ⚙️ Installation & Setup

### 1. Create and activate a virtual environment

``` bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

``` bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file and add:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/blogdb
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create admin user
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```
### Visit
```cpp
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
```

## 🔐 Permissions & Security
- Only authenticated users can create posts
- Users can only edit or delete their own posts
- Admin users have full access via Django Admin
- Ownership enforced at both view and admin levels