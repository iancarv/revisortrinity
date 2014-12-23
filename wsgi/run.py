#!/usr/bin/python
from app import app, envs
if __name__ == "__main__":
    app.run(debug=True)  # We will set debug false in production
