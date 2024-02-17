# ConOp, Consumption Optimizer

ConOp is a simple to use web app that'll help you optmize your electrical consumption.

## Installing

In order to install and host your own instance of ConOp, clone this file and run the following commands:

# Web frontend

Detailed descriptions are available at the web's [README](./web/README.md).

# Backend

This Flask application provides a RESTful API for user management, file uploading, and data analysis. It supports user registration and login, secure file uploads to a server with session-based authentication, and performs predefined data analysis tasks.

## Features

- **User Authentication:** Register new users and manage user login sessions.
- **File Upload:** Securely upload files to the server with session-based authentication.
- **Data Analysis:** Perform data analysis on uploaded files and return results.

### Installing

First, clone the repository to your local machine:

bash
git clone https://yourrepositoryurl.git

Navigate to the project directory:

cd flask-file-upload-and-analysis

Create a virtual environment and activate it:

python -m venv venv
## On Windows
venv\Scripts\activate
## On Unix or MacOS
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

Set the environment variables for the Flask application:

export FLASK_APP=run.py
export FLASK_ENV=development

Start the Flask application:

flask run

## Contributing

Read more about [contributing guidelines](./CONTRIBUTING.md) and [code of conduct](./CODE_OF_CONDUCT.md) at the previous links.
