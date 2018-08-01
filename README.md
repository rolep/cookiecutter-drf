# cookiecutter-drf

[![Build Status](https://travis-ci.com/fndrz/cookiecutter-drf.svg?token=qdpTcWC2mqQPPSZNoKk1&branch=master)](https://travis-ci.com/fndrz/cookiecutter-drf)


## Requirements
- Docker
- Python 3.7
- Pipenv


## Features

### Architecture:
* Containerized (Docker)
* Dependency and python version management (Pipenv)
* Python 3.7
* Django 2.0

### Utilities:
* Better settings (django-environ, django-configurations)
* Better logging (logutils)
* Common model fields and mixins (django-model-utils)

### API:
* Django Rest Framework
* QuerySet filtering (django-filter)
* Automatic Swagger/OpenAPI documentation (django-rest-swagger)

### Authentication:
* Custom user model
* Authentication endpoints (djoser)
* Social authentication and OAuth2 (social-auth-app-django, django-oauth-toolkit, django-rest-framework-social-oauth2)

### Testing:
* pytest with pytest-django
* Easy API testing (django-rest-assured)
* Factories (factory-boy)
* django-debug-toolbar available locally
* Code quality (Flake8)
* CI integration (Travis CI)

### Continuous Deployment:
* Heroku


## Upcoming Features:
* Email verification
* Better permissions


## Usage
See [USAGE.md](USAGE.md).
