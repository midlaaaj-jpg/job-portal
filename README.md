# Hireo – Job Portal

Hireo is a Django-based job portal that connects job seekers with companies. Employees can explore job opportunities and apply for jobs, while companies can post jobs and manage applications.

## Features

### Employee

* Employee registration and login
* Create and manage employee profiles
* Browse available jobs
* View job details
* Apply for jobs
* Track application status

### Company

* Company registration and login
* Create and manage company profiles
* Post job opportunities
* View and manage posted jobs
* Close job listings
* View applicants
* Update application status

## Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite (if configured as the project database)

## Project Setup

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate into the project folder:

   ```bash
   cd job_portal
   ```

3. Create a virtual environment:

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:

   **Windows:**

   ```bash
   env\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your browser:

   ```text
   http://127.0.0.1:8000/
   ```

## Project Status

Completed – Developed as a Django learning project.

## Author

Developed by Midlaj.
