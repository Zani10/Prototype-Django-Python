# Django Article Platform

This is a Django-based web platform that allows users to create, edit, and manage articles. Users can also view detailed articles, leave comments, and interact with a clean and responsive design. The project uses Django as the backend framework and Tailwind CSS for styling.

## Features

- User authentication (login, logout, sign up)
- Add, edit, and delete articles
- Article detail pages with comments
- View and restore article version history
- Clean and responsive design using Tailwind CSS
- User profile page displaying their articles
- Pagination for easy navigation through articles
- Admin panel for managing articles and users

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: SQLite (default with Django)
- **Tools**: Django Admin, Visual Studio Code

## Setup Instructions

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.6+
- Django (latest version)
- Node.js and npm (for installing Tailwind CSS, optional)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate

3. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt
   
4. **Install Tailwind CSS (optional):**
   ```bash
   npm install -g tailwindcss
   npx tailwindcss init
5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
6. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   
## Running the Application

1. **Start the development server:**
   ```bash
   python manage.py runserver
2. **Open your web browser and go to: http://127.0.0.1:8000/**
3. **Create own account or log in with username zani, password zani for testing**

## Features Overview
- Home Page: Displays a list of articles with pagination.
- Article Detail Page: Shows article content and allows users to leave comments.
- Add/Edit/Delete Article: Authenticated users can manage their own articles.
- Article History: Users can view previous versions of their articles and restore specific versions.
- User Profile Page: Shows the logged-in user's articles.
- Admin Panel: Available at http://127.0.0.1:8000/admin/ for managing the site.

## Folder Structure
      |-- .venv/
      |-- media/
      |-- mysite/
      |   |-- __pycache__/
      |   |-- migrations/
      |   |-- static/
      |   |-- templates/
      |       |-- registration/
      |       |-- add_article.html
      |       |-- article_detail.html
      |       |-- article_history.html
      |       |-- article_list.html
      |       |-- base.html
      |       |-- delete_article.html
      |       |-- edit_article.html
      |       |-- preview_article.html
      |       |-- profile.html
      |   |-- admin.py
      |   |-- asgi.py
      |   |-- forms.py
      |   |-- models.py
      |   |-- settings.py
      |   |-- urls.py
      |   |-- views.py
      |   |-- wsgi.py
      |-- manage.py
      |-- requirements.txt
      |-- README.md



## SOURCES
Frontend
https://docs.djangoproject.com/en/5.1/topics/forms/
https://realpython.com/django-forms/
https://tailwindcss.com/docs
https://www.youtube.com/watch?v=dFgzHOX84xQ
https://www.tailwindtoolbox.com/
Packages
https://django-simple-history.readthedocs.io/
https://django-reversion.readthedocs.io/en/stable/
https://medium.com/@abhishekchauhan_7861/adding-version-control-to-django-models-using-django-reversion-3cf6f84631d
https://docs.djangoproject.com/en/stable/
https://djangopackages.org/
Backend
https://www.w3schools.com/django/django_models.php
https://www.w3schools.com/django/django_urls.php
https://www.w3schools.com/django/django_create_virtual_environment.php
Admin
https://www.w3schools.com/django/django_admin.php
https://www.w3schools.com/django/django_admin_create_user.php
https://www.w3schools.com/django/django_add_static_files.php
YT
https://youtu.be/rHux0gMZ3Eg
https://youtu.be/qcJZN1pvG6A?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX
