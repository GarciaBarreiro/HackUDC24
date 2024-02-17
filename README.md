# ConOp, Consumption Optimizer

ConOp is a simple to use web app that'll help you optmize your electrical consumption.

# Web frontend

Detailed install steps are available at the web's [README](./web/README.md).

# Backend

This Flask application provides a RESTful API for user management, file uploading, and data analysis. It supports user registration and login, secure file uploads to a server with session-based authentication, and performs predefined data analysis tasks.

## Features

- **User Authentication:** Register new users and manage user login sessions.
- **File Upload:** Securely upload files to the server with session-based authentication.
- **Data Analysis:** Perform data analysis on uploaded files and return results.

### Installing

First, clone the repository to your local machine:

```bash
git clone https://yourrepositoryurl.git
```

Navigate to the project directory:

```bash
cd flask-file-upload-and-analysis
```

Create a virtual environment and activate it:

```bash
python -m venv venv
```

## On Windows

```
venv\Scripts\activate
```

## On Unix or MacOS

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set the environment variables for the Flask application:

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
```

Start the Flask application:

```bash
flask run
```

# Data processing

For the data processing of the electrical consumption data we have done several things:

We have calculated reference values to compare the user's data with. We have calculated the average values for diferent seasons of the year, for different time frames and some more, so that we can compare the user's consumption with this.

We also can provide the graphs of the consumption data to the users on the app, like the consumption over time with the data they have already uploaded.

## Contributing

Read more about [contributing guidelines](./CONTRIBUTING.md) and [code of conduct](./CODE_OF_CONDUCT.md) at the previous links.
