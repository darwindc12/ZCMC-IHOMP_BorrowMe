# **ZCMC-IHOMP BorrowMe V1.1.0**

Welcome to **BorrowMe**, the go-to tool for ZCMC employees to check out, track, and manage peripheral devices. This project includes both a **Django web application** and a **FastAPI API backend**.

---

##  **New in Version 1.1.0**
-  **Integrated FastAPI** for faster, modern API interactions.
-  **CRUD endpoints** to manage borrowing records (GET, POST, PUT, DELETE).
-  **Performance improvements** for better speed and flexibility.

---

##  **Features**
- **Browse Devices**: View which devices are available for borrowing.
- **Request Devices**: Employees can request to borrow devices via the web.
- **Admin Management**: Admins can update device statuses via the admin panel.
- **API Access**: FastAPI backend to support CRUD operations for borrow records.
##  **Getting Started**
These instructions will get you up and running with **Docker**. You'll be able to run both the **Django web app** and **FastAPI API** in a single container.

---

##  **Prerequisites**
Make sure you have the following tools installed:

-  **Python 3.11** (optional, only if running locally)  
-  **Docker** (this is required for containerized development)  

---

##  **Setup Instructions**

### 1 **Clone the Repository**
```bash
git clone https://github.com/yourusername/borrowme.git
cd borrowme


### 2 **Build the Docker Image**

```bash
docker build -t borrowme:latest .

### 3 **Run the Container**

```bash
docker run -p 8000:8000 -p 8001:8001 borrowme:latest

### 4 **Access the App**

- **Django Web App**: [http://localhost:8000](http://localhost:8000)  
- **FastAPI API Docs**: [http://localhost:8001/docs](http://localhost:8001/docs)

##  **Usage Instructions**

###  **Django Web App**

- **URL**: [http://localhost:8000](http://localhost:8000)  
- **Admin URL**: [http://localhost:8000/admin](http://localhost:8000/admin)  

**Default login credentials**:  
- **Username**: `admin`  
- **Password**: `admin123`

### **FastAPI API**

- **Docs (Swagger UI)**: [http://localhost:8001/docs](http://localhost:8001/docs)  
- **ReDoc API Docs**: [http://localhost:8001/redoc](http://localhost:8001/redoc)

## **API Endpoints**

| **Endpoint**         | **Method**  | **Description**                     |
|---------------------|-------------|-------------------------------------|
| `/api/borrows/`      | **GET**     | Get a list of all borrows.           |
| `/api/borrows/{id}`  | **GET**     | Get details for a specific borrow.   |
| `/api/borrows/`      | **POST**    | Create a new borrow record.          |
| `/api/borrows/{id}`  | **PUT**     | Update a specific borrow record.     |
| `/api/borrows/{id}`  | **DELETE**  | Delete a specific borrow record.     |

## **Troubleshooting**

If you encounter issues, here are some common fixes.

### **Problem**: `ModuleNotFoundError: No module named 'ihomp_borrowme_project'`
**Solution**:  
- Ensure your **src/** folder is properly structured.  
- Double-check the `DJANGO_SETTINGS_MODULE` environment variable. It should point to **ihomp_borrowme_project.settings**.  

---

### **Problem**: **Database errors or migrations not applied**
**Solution**:  
Rebuild the container and force migrations by running the following commands:  
```bash
docker-compose down --volumes
docker-compose up --build

### **Problem**: **"Address already in use" for port 8000 or 8001**
**Solution**:  
- Make sure nothing else is running on **port 8000** or **port 8001**.  
- If other services are using these ports, you can stop them or change the port mappings in Docker.  

**How to change port mapping in Docker**:  
Edit the **docker run** command to map to different ports on your host machine.  
```bash
docker run -p 8080:8000 -p 8081:8001 borrowme:latest


## **How to Contribute**

### 1 **Fork the repo and create a new branch**
```bash
git checkout -b feature/your-feature-name


### 2 **Make your changes, commit, and push**
```bash
git push origin feature/your-feature-name

### 3 **Open a pull request for review**

1. **Go to the GitHub repository**.  
2. Click on **Pull Requests** in the top navigation bar.  
3. Click the **New Pull Request** button.  
4. Select your branch from the branch list.  
5. Add a description of your changes and submit it for review.  


## **Changelog**

### **Version 1.1.0**
- **Added FastAPI integration** for modern and faster API interactions.  
- **CRUD endpoints** for borrowing records (GET, POST, PUT, DELETE) to manage borrowing records efficiently.  
- **Performance improvements** for better speed and flexibility.  
