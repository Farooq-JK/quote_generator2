# Quote Generator

A Django-based web application that allows users to generate, manage, and download inspirational quotes.

## Features

- Generate and view inspirational quotes
- Download quotes as images
- User authentication system
- Quote management system
- Responsive design

## Technologies Used

- Python 3.x
- Django 5.1.5
- Bootstrap 4
- SQLite database
- django-crispy-forms
- Pillow for image processing
- whitenoise for static files

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd quote_generator
```

2. Create a virtual environment and activate it:
```bash
python -m venv myenv
# On Windows
myenv\Scripts\activate
# On Unix or MacOS
source myenv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

## Running the Application

To run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

- `quote_generator/` - Main project directory containing settings
- `quotes/` - Main application directory
- `db.sqlite3` - SQLite database
- `requirements.txt` - Project dependencies
- `manage.py` - Django's command-line utility for administrative tasks

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 