# Social Network

## Overview
Basic models:
- User
- Post (always made by a user)
Basic features:
- user signup
- user login
- post creation
- post like
- post unlike
Requirements:
- use hunter.io for verifying email existence on signup
- use clearbit.com for getting additional data for the user on signup (user's full name)
- use JWT for user authentication

## Deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings (see example secret.env):
and change file name to .env:

`SECRET_KEY`,
`DB_PASSWORD`,
`DB_NAME`,
`DB_USER`

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Run app:

`python3 manage.py runserver`
