FROM python:3.9-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Install Ansible, Ansible Core, ncclient, jxmlease, xmltodict e ansible-pylibssh
RUN pip install ansible ansible-core ncclient jxmlease xmltodict ansible-pylibssh
# Install Docker and dependencies
RUN pip install django django-allauth django-compat django-environ Pillow psycopg2-binary djangorestframework
# Copy files
COPY /Alpha /Alpha
COPY /sshkeys /root/.ssh
# Set working directory
WORKDIR /Alpha

# Set entrypoint
ENTRYPOINT ["python3","manage.py","runserver", "0.0.0.0:8000"]

