<h1 align="center">Hi, guys! 👋</h1>

<p align="center">
    <b>What is SwitchSetup?</b><br><br>
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
- [Configure your .env](#configure-env)
- [DataBase](#database)
- [Run SwitchSetup](#run-switchsetup)
- [FAQ](#faq)
- [Version](#version)
- [Videos](#videos)


## Setup


#### Git Clone

To set up the project locally, please follow these steps:

1. Clone the repository: `git clone https://github.com/AleDouglas/SwitchSetup.git` .
2. Install the packages from the requirements.txt file in your Virtual Environment or use the Dockerfile .
3. You need generate your own [Secret Key](#SecretKey) .
4. [Configure your .env](#configure-.env) .
5. You can run it in [your terminal or dockerfile](#run-switchsetup) .


## SecretKey

Start the **Python interpreter**
```
import secrets
secrets.token_hex(32)
Copy the key in .env
```

#### Configure .env


Create an .env file in the /core directory:
```
SECRET_KEY=SECRET KEY
DEBUG=True
```
**Use DEBUG=TRUE only when in development.**


Be mindful that you can generate a new key whenever necessary. 
However, it is crucial to remember that if you are using our project, you should not disclose the key to anyone.

## Run SwitchSetup

Use for login:
```
Username: admin
Password: 123
```

#### Terminal Local:

```
cd WebApi
python manage.py migrate
python manage.py runserver
```

#### Dockerfile:

```
cd WebApi
python manage.py migrate
cd ..
docker build -t image_name .
docker run -p 8000:8000 imagename
```


## Database

We use SQLite at first, but it is possible to manage other databases.

Use [Django's](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DATABASES) own reference.

If you lose the database file or decide to switch to a different one, you will need to follow these steps:

1. Migration ( **Inside the WebApi file** )


```
python manage.py migrate
```
After this, you just need to either use Docker or run it on your local machine.

Use for login:
```
Username: admin
Password: 123
```


I recommend using MySQL or PostgreSQL to avoid the use of a physical database within the documents. Simply follow the [Django]((https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DATABASES) ) reference for the necessary modifications.


## FAQ


##### Problems for login authentication in Ansible-Docker
We have identified an issue regarding Ansible authentication. This might be caused by the required keys. Simply copy the keys from the ~/.ssh/ file to the 'sshkeys' folder within the project. We will work on resolving this problem in the upcoming updates.


##### Issue when trying to run the server, indicating something related to allauth
We've identified some issues on certain machines. You just need to add the:
```
'allauth.account.middleware.AccountMiddleware', 
 ```
to the MIDDLEWARE list in the settings.py file.

## Version


| Version   |            |  Date |
|----------|:-------------:|------:|
| 1.6.1 | Fixing and Update system for customized playbooks and hosts | 13/09/2023
| 1.6 | Added a system for customized playbooks and hosts ( TEST ) | 13/09/2023
| 1.5.3 | Resolved Datetime Import and finish tests | 18/08/2023
| 1.5.2 | Resolved logging issue in certain system tasks | 18/08/2023
| 1.5.1 | Added ansible execution information control system | 18/08/2023 |
| 1.5 | Possible solution for connecting via docker-ansible and adding level of information when running ansible | 17/08/2023 |
| 1.4 |  Fixed ansible conection | 17/07/2023 |
| 1.3 |  SSH Save Credentials | 16/07/2023 |
| 1.2 |  User Options | 14/07/2023 |
| 1.1 |  Fixed login form | 14/07/2023 |
| 1.0 |    Up version 1.0   |   14/07/2023 |


## Videos


[First impression ( 14/07/2023 )](https://www.youtube.com/watch?v=5jByei5CKC8)
