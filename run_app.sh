#!/bin/bash
export FLASK_ENV=development
export FLASK_APP=main.py
flask run -h localhost -p 3003
