import os
from ansible_runner import run

# Obtém o diretório atual do script Python
script_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho absoluto para o playbook
playbook_path = os.path.join(script_directory, 'playbook.yml')
inventory_path = os.path.join(script_directory, 'host-cisco.yml')
artifacts_directory = './salvar_aqui/'
# Executa o playbook
r = run(playbook=playbook_path, inventory=inventory_path, artifact_dir=artifacts_directory)


print("Status => {} ({})".format(r.status, r.rc))


output = {}
output_all = {}
for event in r.events:
    stdout_lines = event.get('stdout', [])
    if stdout_lines:
        print(stdout_lines)