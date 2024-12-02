# ZCMC-IHOMP BorrowMe V1.1.0

Welcome to **BorrowMe**, the go-to tool for ZCMC employees to check out peripheral devices and keep track of them. Originally built with Django, we've now added a powerful FastAPI backend to give you even more flexibility and performance.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Use It](#how-to-use-it)
- [API Goodies](#api-goodies)
- [Contributing](#contributing)
- [What’s New in Version 1.1.0](#whats-new-in-version-110)

---

## Features

Here’s what BorrowMe can do:

- Browse the available devices and see what’s ready to borrow.
- Request to borrow devices with a few clicks.
- Admins can manage device statuses right from the admin panel.
- **New in v1.1.0**:
  - Fully integrated FastAPI for faster and modern API interactions.
  - Endpoints for creating, reading, updating, and deleting borrow records.

---

## Installation

### What You Need

- Python 3.x
- PostgreSQL (our trusty database)
- Django and FastAPI libraries
- All other necessary tools are listed in `requirements.txt`.

### Steps to Get Started

1. **Clone the Repository**  
   Start by pulling down the project to your local machine:

   ```bash
   Copy code
   git clone https://github.com/yourusername/ZCMC-IHOMP-BorrowMe.git

2. **Install Dependencies**  
   Move into the project folder and install everything you need:
   
   ```bash
   Copy code
   pip install -r requirements.txt


3. **Set Up the Database**  

   - Configure your database settings:
      - Django: In settings.py
      - FastAPI: In database.py (look for DATABASE_URL).
   - Apply the migrations:

   ```bash
   Copy code
   python manage.py makemigrations
   python manage.py migrate

4. **Run the Django App**  
   Fire up the main web application:

   ```bash
   Copy code
   python manage.py runserver

5. **Run the FastAPI App**  
Spin up the API server:

    ```bash
   Copy code
   uvicorn fastapi_app.main:app --reload

5. **You're Ready to Go!**  

   - Web app: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/
   - FastAPI API: http://localhost:8001/

##How to Use It
###For Everyday Users:
   1. Open the homepage and browse through the available devices.
   2. Select a device to see more details.
   3. Request to borrow it if it’s available.

###For Admins:
   - Log in to the admin panel (http://localhost:8000/admin/) to manage devices and requests.


##API Goodies
   If you're a developer or just love working with APIs, we've got you covered. BorrowMe now comes with a FastAPI backend that supports:

   - GET: Fetch all borrow records or a specific one.
   - POST: Add a new borrow request.
   - PUT: Update existing borrow details.
   - DELETE: Remove borrow records.

###Explore the API
   - Swagger Docs: http://localhost:8001/docs
   - ReDoc Docs: http://localhost:8001/redoc
You can test all the endpoints directly from your browser or using tools like Postman.

##Contributing
Want to help improve BorrowMe? Fantastic! Here’s how to get started:

1. Fork the Repository
   Clone your own copy of the project.

2. Create a New Branch

    ```bash
   Copy code
   git checkout -b feature/your-feature-name
3. Make Your Changes
   Add new features, fix bugs, or update documentation.

4. Push Your Changes

    ```bash
   Copy code
   git push origin feature/your-feature-name
5. Open a Pull Request
   Head to the main repository and submit your changes for review.

##What’s New in Version 1.1.0
- 🚀 FastAPI Integration: A modern and blazing-fast API layer.
- 🛠 CRUD Endpoints: Manage borrow records with GET, POST, PUT, and DELETE.
-⚡ Performance Boost: API interactions are now quicker and more flexi
