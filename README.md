# NIMAP Machine Test

## Django Python RESTful API Implementation

This project demonstrates a RESTful API implementation using Django and MySQL.

### Database
- MySQL

### IDE
- PyCharm

### Operating System
- Linux (Ubuntu)

## Prerequisites
- Python 3.x
- Django
- MySQL

## Getting Started

To run this project, please follow the steps below to set up the database and start the Django server.

### Step 1: Database Setup

1. **Log into MySQL**

    ```bash
    mysql -u root -p
    ```

2. **Create and Use a New Database**

    ```sql
    CREATE DATABASE my_database;
    USE my_database;
    ```

3. **Create Required Tables**

    Run the following SQL commands to create the necessary tables:

    ```sql
    -- Create the auth_user table
    CREATE TABLE auth_user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        password VARCHAR(128) NOT NULL,
        last_login DATETIME NULL,
        is_superuser BOOLEAN NOT NULL,
        username VARCHAR(150) NOT NULL UNIQUE,
        first_name VARCHAR(150) NOT NULL,
        last_name VARCHAR(150) NOT NULL,
        email VARCHAR(254) NOT NULL,
        is_staff BOOLEAN NOT NULL,
        is_active BOOLEAN NOT NULL,
        date_joined DATETIME NOT NULL
    );

    -- Create the myapp_client table
    CREATE TABLE myapp_client (
        id INT AUTO_INCREMENT PRIMARY KEY,
        client_name VARCHAR(255) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        created_by_id INT NULL,
        CONSTRAINT fk_client_user FOREIGN KEY (created_by_id) REFERENCES auth_user (id) ON DELETE SET NULL
    );

    -- Create the myapp_project table
    CREATE TABLE myapp_project (
        id INT AUTO_INCREMENT PRIMARY KEY,
        project_name VARCHAR(255) NOT NULL,
        client_id INT NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        created_by_id INT NULL,
        CONSTRAINT fk_project_client FOREIGN KEY (client_id) REFERENCES myapp_client (id) ON DELETE CASCADE,
        CONSTRAINT fk_project_user FOREIGN KEY (created_by_id) REFERENCES auth_user (id) ON DELETE SET NULL
    );

    -- Create the myapp_project_users table
    CREATE TABLE myapp_project_users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        project_id INT NOT NULL,
        user_id INT NOT NULL,
        CONSTRAINT fk_project_users_project FOREIGN KEY (project_id) REFERENCES myapp_project (id) ON DELETE CASCADE,
        CONSTRAINT fk_project_users_user FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE
    );
    ```

### Step 2: Django Project Setup

1. **Navigate to the Project Directory**

    Make sure you are in the project directory where `manage.py` is located:

    ```bash
    cd project_management
    ```

2. **Apply Migrations**

    Run the following commands to create the necessary tables in your MySQL database:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

3. **Run the Development Server**

    Start the Django development server using the command below:

    ```bash
    python3 manage.py runserver
    ```

### Step 3: Testing the APIs

You can test the APIs using any REST client such as Postman or Curl.

- **Register a Client:**
  Use `POST /api/clients/` to create a new client.

- **Fetch Clients Info:**
  Use `GET /api/clients/` to retrieve the list of clients.

- **Edit/Delete Client Info:**
  Use `PUT/PATCH /api/clients/:id` to edit client details or `DELETE /api/clients/:id` to delete a client.

- **Add New Projects for a Client:**
  Use `POST /api/clients/:id/projects/` to add a new project for a client and assign users to it.

- **Retrieve Assigned Projects for Logged-in Users:**
  Use `GET /api/projects/` to fetch all projects assigned to the currently logged-in user.


