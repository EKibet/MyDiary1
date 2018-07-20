"""RESTful server implemented using the
Flask-RESTful extension."""

import os
from app.app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True)
