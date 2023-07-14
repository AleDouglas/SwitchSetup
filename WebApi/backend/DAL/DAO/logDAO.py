from backend.DAL.models.log import AnsibleLog
from django.db.models import Q


def createLog(user, date, hour, switch, playbook, host, output):
    log = AnsibleLog(
        user=user,
        date=date,
        hour=hour,
        switch=switch,
        playbook=playbook,
        host=host,
        output=output,
    )
    log.save()
    return True

def filterLog(user, date, id):
    if (id=='' and user=='' and date==''):
        log = AnsibleLog.objects.all()
        return log

    filters = Q()
    if id != '':
        filters &= Q(id=int(id))
    if user != '':
        filters &= Q(user=user)
    if date != '':
        filters &= Q(date=date)

    log = AnsibleLog.objects.filter(filters)
    return log