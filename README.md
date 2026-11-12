# Auth Login & Protect API

A secure authentication REST API built using **FastAPI** and **Supabase**. This project provides user registration, login, token refresh, and protected routes using Bearer token authentication.

##  Features

- **User Signup:** Register new users using email and password.
- **User Login:** Authenticate users using Supabase authentication.
- **JWT Authentication:** Generate access and refresh tokens.
- **Protected Profile:** Allow authenticated users to access their profile.
- **Protected Dashboard:** Secure dashboard endpoint accessible only to authenticated users.
- **Token Refresh:** Generate a new access token using a refresh token.
- **Public Information:** Provide publicly accessible API information.
- **Health Check:** Check API server status.

##  Technologies Used

- Python
- FastAPI
- Supabase
- Pydantic
- Uvicorn
- JWT / Bearer Token Authentication

##  Project Structure

```text
auth-login-protect/
│
├── main.py
├── supabase_client.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/auth-login-protect.git
```

### 2. Navigate to the project folder

```bash
cd auth-login-protect
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

For macOS/Linux:

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project directory and add your Supabase project URL and API key using the variable names expected by `supabase_client.py`.

**Note:** Never share or upload your `.env` file to GitHub.

### 7. Run the application

```bash
uvicorn main:app --reload --port 8000
```

The API will run at:

`http://127.0.0.1:8000`

##  API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home |
| GET | `/health` | Health Check |
| POST | `/auth/signup` | User Registration |
| POST | `/auth/login` | User Login |
| GET | `/public/info` | Public Information |
| GET | `/protected/profile` | Protected Profile |
| GET | `/protected/dashboard` | Protected Dashboard |
| POST | `/auth/refresh` | Refresh Access Token |

##  API Documentation

FastAPI provides interactive Swagger documentation.

After starting the server, open:

`http://127.0.0.1:8000/docs`

You can test all API endpoints directly through Swagger UI.

##  Authentication

The application uses Supabase Authentication to manage user registration and login.

Protected endpoints require a valid access token in the Authorization header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

The refresh endpoint accepts a refresh token to obtain a new access token.

##  Project Objective

The objective of this project is to understand and implement secure user authentication and authorization using FastAPI and Supabase. It demonstrates API development, token-based authentication, protected routes, and integration with an external authentication service.

## 👨 Author

**Devdatta Desai**

GitHub: https://github.com/Deva5000

---

**Project:** Auth Login & Protect API  
**Version:** 1.0.0