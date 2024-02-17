# SPDX-FileCopyrightText: 2024 Tomás García Barreiro, Ángel Suárez Torres, Muhammad Imran
#
# SPDX-License-Identifier: MIT-0

from flaskr import start_app

app = start_app()

if __name__ == "__main__":
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
