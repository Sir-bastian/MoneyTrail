# Moneytrail Application

Moneytrail is a Flask-based web application that provides functionality for user registration, login, logout, and managing expenses. This README provides instructions on how to set up, run, and use the application.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the application, you'll need Python 3 and MySQL installed. You can set up your environment by following these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    ```

2. Change to the application directory:
    ```bash
    cd <application-directory>
    ```

3. Set up a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux and macOS
    # On Windows: source venv/Scripts/activate
    ```

4. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Update the `app.py` file with your MySQL database connection details:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database>'
    ```

    - Replace `<username>`, `<password>`, `<host>`, `<port>`, and `<database>` with your MySQL credentials and database information.
    - If your password contains special characters (e.g., `@`), make sure to URL encode the password (e.g., `%40` for `@`).

2. Set the `SECRET_KEY` in `app.py`:
    ```python
    app.config['SECRET_KEY'] = 'your_secret_key'
    ```

    - Replace `'your_secret_key'` with a secure, random secret key for Flask session management.

3. Create the necessary database tables:
    ```bash
    python3 main.py
    ```

## Usage

To run the application:

1. Start the Flask development server:
    ```bash
    python3 main.py
    ```

2. Open your web browser and navigate to `http://localhost:5000` to access the application.

## API Endpoints

The application provides various API endpoints for user and expense management:

- `/register` (POST): Register a new user.
- `/login` (POST): Log in an existing user.
- `/logout` (GET): Log out the current user.
- `/expenses` (GET, POST): Retrieve all expenses for the logged-in user or add a new expense.
- `/expenses/<int:expense_id>` (PUT, DELETE): Update or delete an existing expense.

## Contributing

Contributions to the application are welcome! To contribute, please fork the repository, create a branch, and submit a pull request.

## License

The application is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
