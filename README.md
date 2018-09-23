# Pet Survey app

This is a small Django app for collecting pet and pet owner information.



## Setup

Create a Python 2.7.x virtualenv and clone the repository. Then run the following commands:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata breeds.json
```

This will install Django 1.11.15 in your virtualenv, create a local SQLite database for the Django models and custom models in the `pet_survey` app, and load data into the `Breed` model.

## Running the app

The app can be started up with `python manage.py runserver`, and navigating to `localhost:8000` in your web browser will bring up the survey.  After successfully submitting the form, you can create a superuser account (`python manage.py createsuperuser`) and login to the Django admin to view saved entries (http://localhost:8000/admin/pet_survey/pet/).

I had planned to create a page for viewing saved entries that didn't require authentication, but ended up running out of time.