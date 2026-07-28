# securelogin
A secure authentication web application built with **Flask**, **SQLite**, **SQLAlchemy**, and **bcrypt** that demonstrates secure user registration, password hashing, login authentication, and session management following cybersecurity best practices.

> This project was built as a learning-focused cybersecurity project to understand how secure authentication systems work internally.

---

## 📖 Project Overview

This application implements a secure user authentication system with the following core security principles:

- Passwords are never stored in plain text.
- Passwords are hashed using **bcrypt** before storage.
- User credentials are validated securely.
- SQLAlchemy ORM is used to reduce SQL Injection risks.
- User sessions are managed securely using Flask sessions.
- Protected routes require authentication.
- Users can securely log out.

---

## ✨ Features

### ✅ User Registration

- Create new user accounts
- Username uniqueness validation
- Email uniqueness validation
- Password hashing using bcrypt
- Store user securely in SQLite database

---

### ✅ Secure Login

- Authenticate registered users
- Verify passwords using bcrypt
- Invalid username/password handling
- Secure authentication flow

---

### ✅ Session Management

- Persistent login sessions
- Protected dashboard
- Automatic login state management
- Secure logout

---

### ✅ Database

- SQLite database
- SQLAlchemy ORM
- User model
- Automatic database creation

---

### ✅ Security Features

- Password Hashing (bcrypt)
- SQLAlchemy ORM (helps prevent SQL Injection)
- Input Validation
- Secure Session Management
- Authentication Required Routes

---

## 🛠 Tech Stack

### Backend

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Login

### Database

- SQLite

### Frontend

- HTML5
- CSS3
- Bootstrap 5

---

## 📂 Project Structure

```
securelogin/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── instance/
│   └── users.db
│
├── models/
│   ├── __init__.py
│   └── user.py
│
├── templates/
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
├── static/
│   └── css/
│       └── style.css
│
└── venv/
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/secure-login-system.git

cd secure-login-system
```

---

### Create a Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📸 Application Flow

### Registration

```
User
   │
   ▼
Fill Registration Form
   │
   ▼
Validate Input
   │
   ▼
Hash Password (bcrypt)
   │
   ▼
Store User in Database
```

---

### Login

```
User
   │
   ▼
Enter Credentials
   │
   ▼
Search User
   │
   ▼
Verify Password Hash
   │
   ▼
Create Session
   │
   ▼
Redirect to Dashboard
```

---

### Logout

```
User
   │
   ▼
Logout
   │
   ▼
Destroy Session
   │
   ▼
Redirect to Login
```

---

## 🔒 Security Measures Implemented

### Password Hashing

Passwords are hashed using **bcrypt** before being stored.

```
Password
      │
      ▼
bcrypt
      │
      ▼
Hashed Password
```

---

### SQL Injection Protection

Instead of writing raw SQL queries, the application uses SQLAlchemy ORM.

Example:

```python
User.query.filter_by(username=username).first()
```

This prevents SQL injection attacks caused by string concatenation.

---

### Session Management

Authenticated users receive a secure session after successful login.

Protected pages require authentication before access.

---

### Logout

User sessions are destroyed securely using Flask-Login.

---

## 📚 Learning Objectives

This project demonstrates:

- Flask Fundamentals
- Web Authentication
- Password Hashing
- Session Management
- SQLAlchemy ORM
- Secure Login Systems
- Cybersecurity Best Practices
- Secure User Authentication Workflow

---

## 🚀 Future Enhancements

- Two-Factor Authentication (2FA)
- Password Reset via Email
- Password Strength Meter
- Email Verification
- CSRF Protection
- Account Lockout after Multiple Failed Attempts
- Remember Me Functionality
- Login Attempt Logging
- Audit Logs
- User Roles (Admin/User)
- JWT Authentication
- Docker Deployment
- PostgreSQL/MySQL Support

---

## 🧪 Test Cases

### Registration

- Register new user
- Duplicate username
- Duplicate email

### Login

- Valid credentials
- Invalid username
- Invalid password

### Session

- Access dashboard after login
- Access dashboard without login
- Logout successfully

---

## 👨‍💻 Author

**Tanya Singh**

Cybersecurity | AI/ML | Digital Forensics Enthusiast

GitHub: https://github.com/singhtanyarajput

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Project Status

✅ Registration Completed

✅ Password Hashing (bcrypt)

✅ Login Authentication

✅ Session Management

✅ Protected Dashboard

✅ Secure Logout

🔄 Additional Security Enhancements Planned

---

## 💡 Key Takeaway

This project focuses on implementing a secure authentication workflow by combining password hashing, ORM-based database access, and session management to protect user accounts from common web security threats while following modern authentication best practices.