# PipeMessage Django App

PipeMessage is a Django app designed for adding, displaying, and managing messages. It provides a user-friendly interface for users to leave messages and conveniently view and manage them.

## Prerequisites

Ensure that you have the following prerequisites before getting started with the project:

- Python (>=3.x)
- Docker
- django

## Getting Started

1. **Clone the repository:**

    ```
    git clone https://github.com/your-username/PipeMessage.git
    ```

2. **Create a virtual environment and install dependencies:**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run the app:**

    ```
    python manage.py runserver
    ```

## Running Tests

```
python manage.py test
```
## Usage
Access the site at http://localhost:8000.
- Add messages using the provided form.
- View, edit, or delete messages from the message history.
## Docker
To run the app using Docker:


```
docker-compose up --build
 ```
Visit http://localhost:8000 in your browser.

## Contributing
Please see the CONTRIBUTING.md file for details on how to contribute to this project.

## Code of Conduct
Please read the [CODE_OF_CONDUCT.md](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_10/blob/main/CODE_OF_CONDUCT.md) for details on our code of conduct.

## Contact
Communication: You can contact us at rosnyanderson@student.unamur.be.
## Reporting Issues
If you encounter any issues or have suggestions for improvements, please open an issue in the [issue tracker](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_10/issues).

License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_10/blob/main/LICENSE) file for details.
