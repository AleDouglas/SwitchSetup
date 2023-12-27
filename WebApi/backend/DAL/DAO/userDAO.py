from backend.DAL.models.user import CustomUser


def checkKey(key):
    users = CustomUser.objects.all()
    for data in users:
        if data.user_key == key:
            return True
    return False