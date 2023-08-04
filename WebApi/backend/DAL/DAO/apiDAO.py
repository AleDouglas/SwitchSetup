from backend.DAL.models.api import *
import secrets

def getAllApi():
    return ApiKey.objects.all()


def getApi(id):
    return ApiKey.objects.get(id=int(id))

def createKey(title):
    credential = ApiKey(
        title=title,
        key=secrets.token_hex(32)
    )
    credential.save()
    return True
