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


############## Version Alpha functions ################

# Playbook methods
class GetPlaybook():
    def all():
        return PlaybookCustom.objects.all()
    def only(id):
        return PlaybookCustom.objects.get(id=int(id))

# Host methods
class GetHost():
    def all():
        return HostCustom.objects.all()
    def only(id):
        return HostCustom.objects.get(id=int(id))
    def device(ip):
        return HostCustom.objects.get(device=str(ip))

# Ansible methods
class GetAnsibleSetting():
    def all():
        return AnsibleSetting.objects.all()
    def only(id):
        return AnsibleSetting.objects.get(id=int(id))

