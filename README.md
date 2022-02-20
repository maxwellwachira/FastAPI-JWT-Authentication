<h1 align="center"><b>Securing FastAPI with JWT Token-based Authentication
</b></h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/maxwellwachira/FastAPI-JWT-Authentication.git)

# Description
Implemention of Token-based authentication using FastAPI and JSON Web Tokens

# Table of contents
* [Prerequisites](#Prerequisites)
* [Directory Structure](#Directory-Structure)
* [Running Locally](#Setting-up-Local-Environment)
* [Acknowledgement](#Acknowledgement)
* [License](#License)


# Prerequisites
- [Python3](https://www.python.org/)


# Directory-Structure
    FastAPI-JWT-Authentication
    ├── app			             # contains app files
    |   ├── api.py
    |   ├── auth
    |   |   ├── auth_bearer.py
    |   |   └── auth_handler.py	
    |	└── models.py    
	├── .env    
	├── main.py                  # Application entry point
    ├── requirements.txt		 # project dependencies
    ├── secret_generator.py		 # Python script to help in generation of SECRET KEY
	└── README.md

# Setting-up-Local-Environment
### clone the repository and navigate to the project directory
```bash
git clone https://github.com/maxwellwachira/FastAPI-JWT-Authentication.git
cd FastAPI-JWT-Authentication/
```
### Create a python virtual environment and activate it
```bash
python3 -m venv venv
source venv/bin/activate
```
### Install Project dependencies
```bash
pip install -r requirements.txt
```
The secret in the environment file (.env.example) should be something stronger and should not be disclosed. I recommend using [secret_generator.py](https://github.com/maxwellwachira/FastAPI-JWT-Authentication/blob/main/secret_generator.py) to generate the secret key

# Acknowledgement
Special thanks to [Abdulazeez Abdulazeez Adeshina](https://testdriven.io/authors/adeshina/) for the awesome [tutorial](https://testdriven.io/blog/fastapi-jwt-auth/)
and also to [Sebastián Ramírez aka @tiangolo](https://github.com/tiangolo) the creator of FastAPI 


## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)
