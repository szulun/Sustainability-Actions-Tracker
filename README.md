# 🌍 Sustainability Actions Tracker

A professional full-stack web application designed to track and manage eco-friendly activities. Built with Django REST Framework (Backend) and React (Frontend).

## 🚀 Key Features

- **Full CRUD Functionality**: Create, Read, Update, and Delete sustainability actions seamlessly
- **Real-time Calculations**: Automatically computes the Total Impact Score based on all logged actions
- **Advanced Error Handling**: Distinguishes between network/server issues and data validation errors with user-friendly alerts
- **Responsive UI**: Modern, clean dashboard interface that works across different screen sizes
- **API Integrity**: Backend endpoints fully tested and verified via Postman

## 🛠 Tech Stack

| Layer        | Technology                                    |
|--------------|-----------------------------------------------|
| Frontend     | React.js, Axios, CSS3                         |
| Backend      | Python, Django, Django REST Framework (DRF)   |
| API Testing  | Postman                                       |
| Database     | SQLite (Default Django DB)                    |

## 📦 Project Structure
```
.
├── backend/            # Django API logic and settings
└── frontend/           # React components and UI assets
```

## ⚙️ Quick Start

### 1. Backend Setup (Django)
```bash
cd backend
pip install django djangorestframework django-cors-headers
python manage.py migrate
python manage.py runserver
```

API will be running at: `http://127.0.0.1:8000/api/actions/`

### 2. Frontend Setup (React)
```bash
cd frontend
npm install
npm install axios
npm start
```

UI will be available at: `http://localhost:3000`

## 🧪 Development Proof

### API Testing (Postman)
Verified successful `GET` and `POST` requests with status 200 OK.

*(Optional: Insert your Postman screenshot link here)*

### UI & Error Handling
Includes proper feedback for users when the server is offline or data is invalid.
