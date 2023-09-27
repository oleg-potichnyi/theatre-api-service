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
## Docker Compose: Ensure that Docker and Docker Compose are installed on your system.
## Build the Docker Containers:
# Setup via Docker
docker-compose build
## Start the Docker Containers:
docker-compose up
## Stopping the Server:
docker-compose down
```

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