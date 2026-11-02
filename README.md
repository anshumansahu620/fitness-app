# Gym Management System

A full-stack Gym Management application built with **Django REST Framework** on the backend and **Next.js (React 19 & Tailwind CSS)** on the frontend. The system provides complete tracking for gym members, automated membership duration management, daily attendance, nutritional diet logs, workout routines, and interactive Swagger API documentation.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup (Django)](#1-backend-setup-django)
  - [Frontend Setup (Next.js)](#2-frontend-setup-nextjs)
- [API Documentation](#api-documentation)
- [Docker Deployment](#docker-deployment)
- [License](#license)

---

## Features

### Member & Account Management (`account`)
- Member registration with profile pictures, contact information, age, and sex.
- Membership tiers with auto-calculated expiration dates (`1 Month`, `3 Months`, `6 Months`, `1 Year`).
- JWT-based authentication (access & refresh tokens) powered by `djangorestframework-simplejwt`.

### Attendance Tracking (`attendance`)
- Daily check-in/check-out logs for members (`Present` / `Absent`).
- Automated entry timestamping and date-indexed history.

### Diet & Nutrition Tracker (`diet`)
- Log daily meals (`Breakfast`, `Lunch`, `Dinner`, `Snacks`).
- Real-time macro and calorie calculation (total calories, protein, carbs, fats).
- Flexible structured JSON storage for complex ingredient/meal data.

### Exercise & Workout Logging (`exercise`)
- Pre-configured catalog of popular gym exercises (Bench Press, Squats, Deadlifts, Pull-ups, etc.).
- Track sets, repetitions, target muscle groups, and performance progress.

### Interactive API Documentation
- Built-in Swagger UI and Redoc via `drf-yasg` for testing endpoints directly in the browser.

---

## Tech Stack

### Backend
- **Framework**: [Django 5.2](https://www.djangoproject.com/)
- **API**: [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
- **Authentication**: JWT via [django-rest-framework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/)
- **API Documentation**: [drf-yasg](https://drf-yasg.readthedocs.io/) (Swagger & OpenAPI 2.0)
- **Database**: SQLite (default for development) / MySQL compatible (`mysqlclient`)
- **CORS Handling**: `django-cors-headers`

### Frontend
- **Framework**: [Next.js 16](https://nextjs.org/) (App Router)
- **Library**: [React 19](https://react.dev/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **Language**: [TypeScript](https://www.typescriptlang.org/)

---

## Project Architecture

```text
django-project/
├── .gitignore               # Root git ignore rules
├── README.md                # Project documentation
├── requirements.txt         # Root Python dependencies
│
├── gymbackend/              # Django Backend Application
│   ├── manage.py            # Django CLI utility
│   ├── Dockerfile           # Docker configuration for backend
│   ├── requirements.txt     # Python dependencies
│   ├── db.sqlite3           # Development SQLite database
│   ├── gymbackend/          # Project configuration (settings, urls, wsgi)
│   ├── account/             # Member profiles & JWT authentication
│   ├── attendance/          # Attendance tracking app
│   ├── diet/                # Nutrition and meal logging app
│   ├── exercise/            # Workouts and exercise logs app
│   ├── notification/        # Notification service
│   ├── templates/           # Custom HTML templates
│   └── media/               # Uploaded member profile images
│
└── frontend/                # Next.js Frontend Application
    ├── package.json         # Node.js dependencies and scripts
    ├── tsconfig.json        # TypeScript configuration
    ├── next.config.ts       # Next.js configuration
    ├── public/              # Static public assets
    └── src/
        └── app/             # Next.js App Router (pages & components)
            ├── components/  # Reusable UI components (NavBar, Hero, etc.)
            ├── globals.css  # Global Tailwind styles
            ├── layout.tsx   # Root layout wrapper
            └── page.tsx     # Landing page
```

---

## Getting Started

### Prerequisites

- **Python**: `3.10+`
- **Node.js**: `18.18+` or `20+`
- **npm** or **yarn** / **pnpm**
- **Git**

---

### 1. Backend Setup (Django)

1. **Navigate to the backend directory**:
   ```bash
   cd gymbackend
   ```

2. **Create and activate a virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv env
     .\env\Scripts\Activate.ps1
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Admin)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```
   The backend will be available at: `http://localhost:8000`

---

### 2. Frontend Setup (Next.js)

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install Node dependencies**:
   ```bash
   npm install
   ```

3. **Start the Next.js development server**:
   ```bash
   npm run dev
   ```
   The frontend will be available at: `http://localhost:3000`

---

## API Documentation

Once the backend server is running, you can explore and test all API endpoints interactively:

- **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- **Django Admin**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Key API Routes:
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/account/` | `POST / GET` | User authentication, member profile, and JWT token refresh |
| `/api/attendance/` | `POST / GET` | Mark attendance and retrieve attendance records |
| `/api/diet/` | `POST / GET` | Log meal nutrition and view dietary progress |
| `/api/exercise/` | `POST / GET` | Record exercise sets, reps, and workout logs |

---

## Docker Deployment

To build and run the backend inside Docker:

```bash
cd gymbackend
docker build -t gymbackend .
docker run -p 8000:8000 gymbackend
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
