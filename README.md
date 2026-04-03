# EECE430 Assignment 5 - Dockerized Player List

This repository contains the Assignment 4 Django project for managing a volleyball player list, prepared for Assignment 5 as a Dockerized GitHub submission.

## Project Features

- Add, view, update, and delete volleyball players
- Server-rendered Django frontend and backend
- SQLite database with seeded sample player data
- Django admin access for demonstration

## Included Player Fields

- ID
- Name
- Date Joined
- Position
- Salary / Payment
- Contact Person

## Admin Credentials

- Username: `karim`
- Password: `karim`

## Run Locally

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Django server:

```bash
python manage.py runserver
```

4. Open the app at [http://localhost:8000/](http://localhost:8000/).

## Run With Docker

1. Build the Docker image:

```bash
docker build -t player-list-app .
```

2. Run the container:

```bash
docker run -p 8000:8000 player-list-app
```

3. Open the app at [http://localhost:8000/](http://localhost:8000/).

## Notes

- The committed `db.sqlite3` already contains sample player records for demo purposes.
- The root route `/` redirects to `/players/`.
