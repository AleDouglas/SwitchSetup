import subprocess, re , json, os
from ansible_runner import run
from ansi2html import Ansi2HTMLConverter


class Ansible:

    def run_ansible(path_playbook, path_inventory):
        converter = Ansi2HTMLConverter(inline=True)
        script_directory = os.path.dirname(os.path.abspath(__file__))
        path_playbook = path_playbook.split('/')
        path_inventory = path_inventory.split('/')
        path_playbook = f'{path_playbook[3]}/{path_playbook[4]}'
        path_inventory = f'{path_inventory[3]}/{path_inventory[4]}'
        playbook = os.path.join(script_directory, path_playbook)
        inventory = os.path.join(script_directory, path_inventory)
        output_task = {}
        stdout = []
        stdout_html = []
        r = run(playbook=playbook, inventory=inventory)
        for event in r.events:
            if event.get('event') == 'runner_on_ok':
                task_name = event.get('event_data', {}).get('task', '')
                task_result = event.get('event_data', {}).get('res', {})
                output_task[task_name] = task_result.get('stdout')
            stdout.append(event.get('stdout', []))

        for x in stdout:
            stdout_html.append(converter.convert(x, full=False ))

        ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
        stdout = [ansi_escape.sub('', line) for line in stdout]
        return output_task, stdout, stdout_html, r.rc
