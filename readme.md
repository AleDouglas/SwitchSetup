<h1 align="center">Hi, guys! 👋</h1>

<p align="center">
    <b>What is SwitchSetupApi?</b><br><br>
    <i>
        This software is designed to configure network devices using <span color="blue">Ansible</span><br>
        For now it works in a very simple way, but I plan to improve security and new features.<br>
        For more information, diagrams and project architecture, see our documentation.<br>
    </i><br>
    Be free to <a href="https://github.com/AleDouglas/SwitchSetup/blob/master/CONTRIBUTING.md">collaborate</a>!
</p>

## Table of Contents

- [Setup](#setup)
- [Secret Key](#secretkey)
- [Version](#version)
- [Configure your .env](#configure-.env)


## Setup

You can use Docker Image

```
sudo docker pull xandouglas/switchsetup:v1.1
sudo docker run -p 8000:8000 --name switchsetup -d xandouglas/switchsetup:v1.1
```

After creating the image, use for login:
```
Username: admin
Password: 123
```

To set up the project locally, please follow these steps:

1. Clone the repository: `git clone https://github.com/AleDouglas/SwitchSetup.git`
2. Install the for ansible and Django in requirements.txt .
3. You need generate your own [Secret Key](#SecretKey).
4. [Configure your .env](#configure-.env)
5. You can run it in your terminal or dockerfile

Terminal: **(before run [Configure your .env](#configure-.env))**
```
cd WebApi
python manage.py runserver
```

Dockerfile: **(before run [Configure your .env](#configure-.env))**
```
docker build -t image_name
docker run -p 8000:8000 image_name
```


## SecretKey

Start the Python interpreter
```
import secrets
secrets.token_hex(32)
```

## Configure .env

Create an .env file in the /core directory:
```
SECRET_KEY=YOU SECRET KEY
DEBUG=True
```
Use DEBUG=TRUE only when in development.


## Version


| Version   |            |  Date |
|----------|:-------------:|------:|
| 1.2 |  User Options | 14/07/2023 |
| 1.1 |  Fixed login form | 14/07/2023 |
| 1.0 |    Up version 1.0   |   14/07/2023 |


## Videos


[First impression ( 14/07/2023 )](https://www.youtube.com/watch?v=5jByei5CKC8)
