from backend.DAL.models.ansible import *


def getAllPlaybook():
    return PlaybookCustom.objects.all()

def getAllCommand():
    return Command.objects.all()

def getAllHost():
    return HostCustom.objects.all()

def getPlaybook(id):
    try:
        return PlaybookCustom.objects.get(id=int(id))
    except:
        return False

def getHost(id):
    return HostCustom.objects.get(id=int(id))

def getHostDevice(ip):
    return HostCustom.objects.get(device=str(ip))