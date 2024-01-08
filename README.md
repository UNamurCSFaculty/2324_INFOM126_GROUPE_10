# PipeMessage Django App

PipeMessage is a Django app designed for adding, displaying, and managing messages. It provides a user-friendly interface for users to leave messages and conveniently view and manage them.

## Prerequisites

Ensure that you have the following prerequisites before getting started with the project:

- [Python (>=3.x)](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- [django](https://www.djangoproject.com/)

## Getting Started

1. **Clone the repository:**

    ```
    git clone https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_10.git
    ```

2. **Create a virtual environment and install dependencies:**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
## Running Tests

```
python manage.py test
```
## Docker
To run the app using Docker (you have to install Docker on your computer before):


```
docker build CIpipeline
 ```
Visit http://localhost:8000 in your browser.

3. **Run the app:**

    ```
    cd CIpipeline
    python manage.py runserver
    ```


## Usage
Access the site at http://localhost:8000.
- Add messages using the provided form.
- View, edit, or delete messages from the message history.

## Contributing
Please see the [CONTRIBUTING.md] file for details on how to contribute to this project.

## Code of Conduct
Please read the [CODE_OF_CONDUCT.md](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_10/blob/main/CODE_OF_CONDUCT.md) for details on our code of conduct.

## Contact
Communication: You can contact us at rosnyanderson@student.unamur.be.
## Reporting Issues
If you encounter any issues or have suggestions for improvements, please open an issue in the [issue tracker](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_10/issues).

License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_10/blob/main/LICENSE) file for details.
