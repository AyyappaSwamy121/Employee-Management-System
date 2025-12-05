# Leave Management System 2

A comprehensive Django-based leave management system for organizations to manage employee leave requests, track attendance, and handle administrative tasks.

## 🚀 Features

### Employee Features
- **User Registration & Login** with OTP verification
- **Profile Management** with profile picture upload
- **Leave Application** with multiple leave types
- **Leave Status Tracking** (Pending, Approved, Denied)
- **Time Clock System** for attendance tracking
- **Task Management** for daily work reporting
- **Leave History** viewing

### Admin Features
- **Employee Management** (Add, Update, Delete employees)
- **Department Management** 
- **Leave Type Management**
- **Leave Approval/Rejection** with email notifications
- **Reporting Dashboard** with leave statistics
- **Time Entry Management**
- **Comprehensive Admin Panel**

## 🛠️ Technology Stack

- **Backend**: Django 5.0.1
- **Database**: SQLite3 (Development) / PostgreSQL (Production)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Email**: SMTP (Gmail)
- **Authentication**: Django Auth + Custom OTP system
- **Static Files**: WhiteNoise middleware

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/leave-management-system.git
cd leave-management-system
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Setup
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your configuration
# SECRET_KEY=your-secret-key-here
# DEBUG=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 🔧 Configuration

### Email Configuration (Gmail)
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password
3. Update your `.env` file with:
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-16-character-app-password
   ```

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 🚀 Deployment

### Heroku Deployment
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set environment variables: `heroku config:set SECRET_KEY=your-key`
4. Deploy: `git push heroku main`

### Production Settings
- Set `DEBUG=False`
- Use PostgreSQL database
- Configure proper `ALLOWED_HOSTS`
- Use environment variables for all sensitive data

## 📁 Project Structure

```
leave_management2/
├── leave_management2/          # Django settings
├── leave2/                     # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── templates/             # HTML templates
│   └── static/                # Static files
├── media/                     # User uploads
├── staticfiles/               # Collected static files
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
└── manage.py                 # Django management
```

## 🔐 Security

- Environment variables for sensitive data
- CSRF protection enabled
- Secure session management
- Password validation
- XSS protection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the [documentation](docs/)
- Review existing issues

## 🔄 Version History

- **v2.0** - Current version with Django 5.0.1
- **v1.0** - Initial release

---

**⚠️ Important**: Never commit sensitive data like SECRET_KEY, passwords, or API keys to version control. Always use environment variables!