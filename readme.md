<h1 align="center">Hi, guys! 👋</h1>

<p align="center">
    <b>What is SwitchSetupApi?</b><br><br>
    <i>
        This software is designed to configure network devices using <span color="blue">Ansible</span><br>
        For now it works in a very simple way, but I plan to improve security and new features.<br>
        For more information, diagrams and project architecture, see our documentation.<br>
    </i><br>
    Be free to collaborate!<br>
</p>

<h3 align="center">How use</h3>

You can use Docker

```
sudo docker pull xandouglas/switchsetup:v1.1
sudo docker run -p 8000:8000 --name switchsetup -d xandouglas/switchsetup:v1.1
```

After creating the image, use for login:
```
Username: admin
Password: 123
```


<h3 align="center">Version</h3>

| Version   |            |  Date |
|----------|:-------------:|------:|
| 1.1 |  Fixed login form | 14/07/2023 |
| 1.0 |    Up version 1.0   |   14/07/2023 |
