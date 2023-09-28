# Theatre Project

This project for managing theatre with actors and genres

## Installation

Python3 must be already installed

```shell
# Local setup
# Clone the repository:
git clone https://github.com/oleg-potichnyi/theatre-api-service.git
# Change directory to the project folder:
cd theatre-api-service
# Set up a virtual environment:
python3 -m venv venv
# Activate the virtual environment on Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
# Install dependencies:
pip install -r requirements.txt
# Environment variables:
## To use the .env and .env.sample files, simply duplicate the .env.sample file and rename it as .env.
## Fill in the variables in the .env file with your actual configuration values, 
## keeping sensitive information private, while the .env.sample file acts as a reference
## for other developers to understand the required environment variables.
# Run this command to apply migrations and update the database schema:
python manage.py migrate
# Start the development server:
python manage.py runserver
```
```shell
# Start the Application via Docker
# Clone the repository:
git clone https://github.com/oleg-potichnyi/theatre-api-service.git
# Change directory to the project folder:
cd theatre-api-service
# Setup via Docker
# Build the Docker Containers:
docker-compose build
# Start the Docker Containers:
docker-compose up
# Stopping the Docker Containers:
# To stop the Docker containers, use the following command:
docker-compose down
```

## How to Obtain a JWT Token

In order to access protected endpoints in this Theatre API, you need to obtain a JSON Web Token (JWT) by authenticating as a user. Follow these steps to get your JWT token:
1.Register an Account
2.Use your registered email and password to log in and obtain your JWT token.
3.After sending the login request, you will receive a JSON response that includes your JWT token.
4.Include the obtained `access_token` in the `Authorization` header of your requests to protected API endpoints.
5.If your access token expires, you can use the `refresh_token` to obtain a new one without having to log in again. 

## Features

* Management of the theater hall, genres and actors
* Play Management
* Performance Scheduling
* Reservation System
* Admin Panel and User Authentication
* API endpoints for interacting with theatre data programmatically
* Pagination and Filtering
* Docker Support
* Documented API endpoints for frontend developers

## User credentials

```shell
Email: admin@admin.com
password: user12345
```