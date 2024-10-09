# Django Article Platform

This is a Django-based web platform that allows users to create, edit, and manage articles. Users can also view detailed articles, leave comments, and interact with a clean and responsive design. The project uses Django as the backend framework and Tailwind CSS for styling.

## Features

- User authentication (login, logout, sign up)
- Add, edit, and delete articles
- Article detail pages with comments
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

## Features Overview
- Home Page: Displays a list of articles with pagination.
- Article Detail Page: Shows article content and allows users to leave comments.
- Add/Edit/Delete Article: Authenticated users can manage their own articles.
- User Profile Page: Shows the logged-in user's articles.
- Admin Panel: Available at http://127.0.0.1:8000/admin/ for managing the site.

## Folder Structure
  ```bash
|-- mysite/
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|-- templates/
|   |-- base.html
|   |-- article_list.html
|   |-- article_detail.html
|   |-- add_article.html
|   |-- edit_article.html
|-- static/
|   |-- css/
|       |-- styles.css
|-- manage.py
|-- requirements.txt
|-- README.md
