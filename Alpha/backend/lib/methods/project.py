from backend.lib.database.project import Project
from backend.lib.database.inventory import Inventory
from backend.lib.database.playbook import Playbook
from backend.lib.database.template import Template
from backend.lib.database.task import Task
from backend.lib.database.user import CustomUser
from backend.lib.database.dashboard import Activity


class GetProject():
    def all():
        return Project.objects.all()

    def only(id):
        return Project.objects.get(id=int(id))

    def get_inventory(id):
        return Inventory.objects.get(id=int(id))
    
    def get_task(id):
        return Task.objects.get(id=int(id))
    
    def get_playbook(id):
        return Playbook.objects.get(id=int(id))

    def get_activity(id):
        return Activity.objects.get(id=int(id))

    def get_template(id):
        return Template.objects.get(id=int(id))
    
    def get_user(id):
        return CustomUser.objects.get(id=int(id))

    def filter(user):
        return Project.objects.filter(owner=user)

    def filter_member(user):
        return Project.objects.filter(members=user)

    def owner(id, owner):
        return Project.objects.get(id=int(id),owner=owner)

    def member(id, user):
        return Project.objects.get(id=int(id),members=user)

    def create(title, password, owner):
        return Project.objects.create(title=title, password=password, owner=owner)

    def add_member(id, user):
        return Project.objects.get(id=int(id)).members.add(user)

    def create_activity(project_id = None, user = None, description = ''):
        activity = Activity.objects.create(description = description, user = user)
        if project_id == None:
            return activity
        return Project.objects.get(id=int(project_id)).activity.add(activity)

    def create_inventory(title, description, inventory_file):
        return Inventory.objects.create(title=title, description=description, inventory_file=inventory_file)

    def only_inventory(project_id, owner, inventory_id):
        try:
            return Project.objects.get(id=int(project_id),owner=owner).inventories.get(id=inventory_id)
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def create_playbook(title, description, playbook_file):
        return Playbook.objects.create(title=title, description=description, playbook_file=playbook_file)

    def only_playbook(project_id, owner, playbook_id):
        try:
            return Project.objects.get(id=int(project_id),owner=owner).playbooks.get(id=playbook_id)
        except Exception as e:
            print(f"Error: {e}")
            return False

    def create_template(author, project, title, version, playbook, inventory):
        template = Template.objects.create(author=author, title=title, version=version, playbook=playbook, inventory=inventory)
        project = project.templates.add(template)
        return template

    def only_template(project_id, owner, template_id):
        try:
            return Project.objects.get(id=int(project_id),owner=owner).templates.get(id=template_id)
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def all_task():
        return Task.objects.all()

    def get_task(id):
        return Task.objects.get(id=int(id))
    
    def create_task(title, author, status, output, template_id):
        task = Task.objects.create(title=title, author=author, status=status, output=output)
        template = Template.objects.get(id=int(template_id)).tasks.add(task)
        return task

    def addMember(project_id, user_id):
        try:
            user = CustomUser.objects.get(id=int(user_id))
            project = Project.objects.get(id=int(project_id)).members.add(user)
            return user
        except Exception as e:
            print(f"Error: {e}")
            return False

