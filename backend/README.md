# ⚙️ Sustainability Tracker - Backend API

Django REST API serving as the backbone for the Sustainability Tracker application.

## 🚀 Getting Started

### Prerequisites
- **Python** 3.8 or higher
- **pip** (Python package manager)

### Installation & Setup

1. Navigate to the `backend` directory
2. Install required dependencies:
```bash
pip install django djangorestframework django-cors-headers
```

### Database Migration
Apply migrations to set up your database schema:
```bash
python manage.py migrate
```

### Run the Server
Start the Django development server:
```bash
python manage.py runserver
```

The API will be available at: http://127.0.0.1:8000/api/actions/

## 🛠 Tech Stack
- **Django**: High-level Python web framework
- **Django REST Framework (DRF)**: For building the Web API
- **django-cors-headers**: Enables React frontend communication with API

## 📂 Data Model

The API manages sustainability actions with the following fields:
- `id`: Unique identifier (Primary Key)
- `action`: Name of the sustainability activity (String)
- `date`: When the action took place (Date)
- `points`: Impact score (Integer)

## 🧪 Testing with Postman

Test the endpoints by sending requests to: `http://127.0.0.1:8000/api/actions/`