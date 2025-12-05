\CONTRIBUTING.md
# Contributing to Leave Management System

Thank you for considering contributing to this project!

## Development Process

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

## Setup Development Environment

```bash
git clone https://github.com/yourusername/leave-management-system.git
cd leave-management-system
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions and classes

## Testing

Run tests before submitting:
```bash
python manage.py test
```

## Reporting Issues

When reporting issues, include:
- Django version
- Python version
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)