
A Django REST Framework-based backend API for a sneakers store. This project includes functionality to manage products, handle user authentication, and manage shopping carts.

---

## Features

- **Product Management:**
  - View all products.
  - View detailed product information.
- **Cart Management:**
  - Add items to the cart.
  - View cart details.
  - Remove items from the cart.
- **Authentication:**
  - Token-based authentication using JWT.

---

## Technologies Used

- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For building RESTful APIs.
- **Django Simple JWT**: For token-based authentication.
- **SQLite/MySQL/PostgreSQL**: Database options.
- **drf-yasg**: For API documentation.

---

## Installation Instructions

1. Clone the repository:
    ```bash
        git clone https://github.com/yourusername/sneakers-store.git
        cd sneakers-store

2.Create and activate a virtual environment:
    ```bash
        python3 -m venv .venv
        source .venv/bin/activate

3.Install dependencies:
    ```bash
        pip install -r requirements.txt

4.Run database migrations:
    ```bash
        python manage.py makemigrations
        python manage.py migrate

5.Start the development server:
    ```bash
        python manage.py runserver

6.Access the application at http://127.0.0.1:8000/.
