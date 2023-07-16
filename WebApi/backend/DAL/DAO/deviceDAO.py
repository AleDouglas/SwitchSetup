from backend.DAL.models.device import DeviceCredential
from django.db.models import Q


def getAllDeviceCredential():
    return DeviceCredential.objects.all()

def getDeviceCredential(id):
    return DeviceCredential.objects.get(id=int(id))

def createCredential(title, username, password):
    credential = DeviceCredential(
        title=title,
        username=username,
        password=password,
    )
    credential.save()
    return True
