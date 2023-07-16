# Contributing Guidelines

Welcome! We appreciate your interest in contributing. Please take a moment to review the following guidelines to ensure a smooth and collaborative contribution process.

## Table of Contents

- [Purpose](#purpose)
- [Setup](#setup)
- [Secret Key](#SecretKey)
- [Configure your .env](#configure-env)
- [Creating Issues](#creating-issues)
- [Submitting Pull Requests](#submitting-pull-requests)
- [Code Style](#code-style)
- [Code Review and Merging](#code-review-and-merging)
- [Code of Conduct](#code-of-conduct)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Purpose

This document provides guidelines and instructions for contributing to our project. It aims to ensure that contributions are made in a consistent and efficient manner.

## Setup

To set up the project locally, please follow these steps:

1. Clone the repository: `git clone https://github.com/AleDouglas/SwitchSetup.git`
2. Install the for ansible and Django in requirements.txt .
3. You need generate your own [Secret Key](#SecretKey).
4. [Configure your .env](#configure-env)
5. You can run it in your terminal or dockerfile

### Terminal: **(Before starting run [Configure your .env](#configure-env))**
```
cd WebApi
python manage.py migrate
python manage.py runserver
```

### Dockerfile: **(Before starting run [Configure your .env](#configure-env))**
```
cd WebApi
python manage.py migrate
cd ..
docker build -t image_name
docker run -p 8000:8000 image_name
```

After this, use for login:
```
Username: admin
Password: 123
```

Once inside the system, you have the capability to manage your users and their credentials effectively.

## SecretKey

Start the Python interpreter
```
import secrets
secrets.token_hex(32)
Copy the key
```
Be mindful that you can generate a new key whenever necessary. 
However, it is crucial to remember that if you are using our project, you should not disclose the key to anyone.

## Configure .env

Create an .env file in the /core directory:
```
SECRET_KEY=YOU SECRET KEY
DEBUG=True
```
Use DEBUG=TRUE only when in development.
## Creating Issues

If you encounter any issues or have feature requests, please create an Issue using the following guidelines:

1. Before creating a new Issue, search the existing Issues to avoid duplicates.
2. Provide a clear and descriptive title.
3. Include detailed information about the problem or feature request, including steps to reproduce (if applicable).
4. Add relevant labels to categorize the Issue appropriately.

## Submitting Pull Requests

We welcome Pull Requests for bug fixes, improvements, or new features. To submit a Pull Request, please follow these steps:

1. Fork the repository and create a new branch for your changes.
2. Commit your changes with clear and concise messages.
3. Provide a detailed description of the changes made in the Pull Request.
4. Ensure that your code adheres to our [Code Style](#code-style) guidelines.

## Code Style

We don't follow a specific code style, however, it's important to stick to the standard already in place.

## Code Review and Merging

All Pull Requests will go through a code review process before merging. Reviewers will provide feedback and suggestions for improvement. Once the changes pass the review, they will be merged into the main branch.

## Code of Conduct

We have a Code of Conduct to ensure a respectful and inclusive environment for all contributors. Please review our [Code of Conduct](https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct) and adhere to it throughout your interactions within the project.

## Acknowledgments

We would like to express our gratitude to all contributors who have dedicated their time and effort to this project.

## Contact

If you have any questions, suggestions, or need further assistance, feel free to contact us at [xand.douglass@gmail.com].

We appreciate your contributions and look forward to working together to make this project even better!
