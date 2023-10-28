from backend.DAL.models.log import AnsibleLog
from django.db.models import Q


def getLog():
    return AnsibleLog.objects.all()

def createLog(user, service, description, data, hour, playbook, host, output):
    log = AnsibleLog(
        user=user,
        service = service,
        description = description,
        data=data,
        hour=hour,
        playbook=playbook,
        host=host,
        output=output,
    )
    log.save()
    return True