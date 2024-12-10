📦 ZCMC-IHOMP BorrowMe V1.1.0
Welcome to BorrowMe, the go-to tool for ZCMC employees to check out, track, and manage peripheral devices. This project includes both a Django web application and a FastAPI API backend.

New in Version 1.1.0
🚀 Integrated FastAPI for faster, modern API interactions.
🛠️ CRUD endpoints to manage borrowing records (GET, POST, PUT, DELETE).
⚡ Performance improvements for better speed and flexibility.

🚀 Features
Browse Devices: View which devices are available for borrowing.
Request Devices: Employees can request to borrow devices via the web.
Admin Management: Admins can update device statuses via the admin panel.
API Access: FastAPI backend to support CRUD operations for borrow records.
🗂️ Project Structure
bash
Copy code
project-root/
├── Dockerfile               # Docker instructions for building the app
├── requirements.txt         # Python dependencies for Django & FastAPI
├── README.md                # This file (setup instructions)
│
├── src/                     # All the source files live here
│   ├── manage.py            # Django entry point
│   ├── qr.py                # QR code generator script
│   ├── main.py              # Simple script for testing
│   │
│   ├── ihomp_borrowme_project/  # Django project directory
│   │    ├── settings.py     # Django project settings
│   │    └── other files     # Other Django files (urls.py, models.py, etc.)
│   │
│   └── fastapi_app/         # FastAPI project directory
│       └── main.py          # FastAPI entry point
🔥 Getting Started
These instructions will get you up and running with Docker. You'll be able to run both the Django web app and FastAPI API in a single container.

📋 Prerequisites
Make sure you have the following tools installed:

🐍 Python 3.11 (optional, only if running locally)
🐳 Docker (this is required for containerized development)
⚙️ Setup Instructions
1️⃣ Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/borrowme.git
cd borrowme
2️⃣ Build the Docker Image

bash
Copy code
docker build -t borrowme:latest .
📝 This command will copy all files in src/, install dependencies, set up the database, and collect static files.

3️⃣ Run the Container

bash
Copy code
docker run -p 8000:8000 -p 8001:8001 borrowme:latest
4️⃣ Access the App

Django Web App: http://localhost:8000
FastAPI API Docs: http://localhost:8001/docs
📚 Usage Instructions
📘 Django Web App
URL: http://localhost:8000
Admin URL: http://localhost:8000/admin
Default login credentials:
Username: admin
Password: admin123
📘 FastAPI API
Docs (Swagger UI): http://localhost:8001/docs
ReDoc API Docs: http://localhost:8001/redoc
📦 Environment Variables
Variable	Description	Default
DJANGO_SETTINGS_MODULE	Django settings file to load.	ihomp_borrowme_project.settings
DATABASE_URL	Database connection URL.	sqlite:///db.sqlite3
If you'd like to set up your own PostgreSQL database, you can edit DATABASE_URL in the .env file.

⚙️ API Endpoints
Endpoint	Method	Description
/api/borrows/	GET	Get a list of all borrows.
/api/borrows/{id}	GET	Get details for a specific borrow.
/api/borrows/	POST	Create a new borrow record.
/api/borrows/{id}	PUT	Update a specific borrow record.
/api/borrows/{id}	DELETE	Delete a specific borrow record.
Pro Tip: Test all the API endpoints directly in Swagger UI at http://localhost:8001/docs.

🐛 Troubleshooting
If you encounter issues, here are some common fixes.

Problem: ModuleNotFoundError: No module named 'ihomp_borrowme_project'
Solution: Ensure your src/ folder is properly structured. You may also need to check the DJANGO_SETTINGS_MODULE environment variable.

Problem: Database errors or migrations not applied
Solution: Rebuild the container and force migrations.

bash
Copy code
docker-compose down --volumes
docker-compose up --build
Problem: "Address already in use" for port 8000 or 8001
Solution: Make sure nothing else is running on those ports, or change the port mapping in Docker.

📦 How to Contribute
Fork the repo and create a new branch:
bash
Copy code
git checkout -b feature/your-feature-name
Make your changes, commit, and push:
bash
Copy code
git push origin feature/your-feature-name
Open a pull request for review.
📝 Changelog
Version 1.1.0

🚀 Added FastAPI integration.
🛠️ CRUD endpoints for borrowing records.
⚡ Performance improvements.
