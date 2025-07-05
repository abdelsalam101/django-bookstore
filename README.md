## 📚 Django Bookstore

A responsive Django-based web application to manage a bookstore. Users can add, edit, delete, and view books, each with detailed attributes. Built with Django and Bootstrap for a clean and responsive user interface.

---

## 🚀 Features

- ✅ User authentication (Sign Up / Login / Logout)
- 🔐 Authorization for views:
  - Certain pages require login
  - Specific actions require permissions
- 📖 Full CRUD for books:
  - Add new books
  - Edit book details
  - Delete books
  - View book list with:
    - Title
    - Author
    - Publication Date
    - Price
    - Categories
- 🖥️ Responsive design using **Bootstrap 5**

---

## 🛠️ Technologies Used

- Python 3.x
- Django 5.x
- SQLite (default development database)
- Bootstrap 5
- HTML / CSS

---

## 📂 Project Structure

Lab1/
├── book_store/ # Django project folder (settings, urls, wsgi, etc.)
│ ├── books/ # App for managing books (views, models, forms, templates)
│ ├── templates/ # Shared templates like base.html
│ └── static/ # Static assets (CSS, JS, etc.)
├── manage.py # Django management script
└── lab_env/ # Virtual environment (excluded from version control)


## 🧪 Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/abdelsalam101/django-bookstore.git
   cd django-bookstore/Lab1
2. **Create & activate a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**:
   ```
   pip install -r requirements.txt

4. **Apply migrations**:
   ```
   python manage.py migrate

5. **5. Create a superuser (for admin access)**:
   ```  
   python manage.py createsuperuser

6. **Run the development server**:
   ```  
   python manage.py runserver

7. **Access the site**:
   ```
   Open http://localhost:8000 in your browser.

🔐 Authentication & Authorization
Users must log in to add or edit books.

Certain views are restricted based on user permissions (e.g. only users with books.add_book permission can create books).

Admin panel available at /admin.

📸 Screenshots
![1](https://github.com/user-attachments/assets/114784a0-ddc8-433d-a7ec-8c4227ecf0e9)
![2](https://github.com/user-attachments/assets/ba1a7c46-3967-477d-9eec-aaf75dfa4f55)
![3](https://github.com/user-attachments/assets/a4a8bb7f-0e2c-4f65-a64a-a8549be1517c)
![4](https://github.com/user-attachments/assets/96d0dcc5-4144-452d-8e82-928a659ee6f4)

📄 License
This project is licensed under the MIT License. See LICENSE for details.

Built with ❤️ using Django and Bootstrap.
