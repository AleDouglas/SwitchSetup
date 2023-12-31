import subprocess

class AnsibleSwitchConnector:

    def __init__(self):
        self.huaweiHost = 'backend/integrations/communs/huawei/hosts.yml'
        self.ciscoHost = 'backend/integrations/communs/cisco/hosts.yml'
        self.huaweiPlaybook = 'backend/integrations/communs/huawei/playbook.yml'
        self.ciscoPlaybook = 'backend/integrations/communs/cisco/playbook.yml'
        self.ansibleHost = 'backend/integrations/communs/ansible/hosts.yml'
        self.ansiblePlaybook = 'backend/integrations/communs/ansible/playbook.yml'
        self.ansibleCFG = 'ansible_cfg=backend/integrations/communs/ansible/ansible.cfg'

    def write_ansible_host(self, string, switch, password, username):
        user_str = f"        ansible_user: {username}\n"
        password_str = f"        ansible_ssh_pass: {password}\n"
        become_str = f"        ansible_become_password: {password}"
        try:
            command_list = string.split('\n')
            command_str = ''
            for item in command_list:
                command_str += '        '+item+'\n'
            if switch == 'Huawei':
                with open(self.huaweiHost , 'r') as arquivo:
                    linhas = arquivo.readlines()
            if switch == 'Cisco':
                with open(self.ciscoHost, 'r') as arquivo:
                    linhas = arquivo.readlines()
            linhas[9] = user_str
            linhas[10] = password_str
            linhas[11] = become_str
            linhas[5] = command_str
            
            with open(self.ansibleHost, 'w') as arquivo:
                arquivo.writelines(linhas)
            return True
        except:
            return False

    def write_ansible_playbook(self, string, switch):
        command_list = string.split('\n')
        if len(command_list) == 1:
            command_str = f'        commands: "{command_list[0]} "\n'

        else:
            command_str = '        commands: |\n'
            for item in command_list:
                command_str += '          '+item+'\n'

        try:
            if switch == 'Huawei':
                with open(self.huaweiPlaybook, 'r') as arquivo:
                    linhas = arquivo.readlines()
            if switch == 'Cisco':
                with open(self.ciscoPlaybook, 'r') as arquivo:
                    linhas = arquivo.readlines()
            linhas[15] = command_str
            with open(self.ansiblePlaybook, 'w') as arquivo:
                arquivo.writelines(linhas)
            return True
        except:
            return False

    def run_ansible(self, ansible_level):
        try:
            if int(ansible_level) == 0:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', self.ansibleHost, '-e', self.ansibleCFG]
            elif int(ansible_level) == 1:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', self.ansibleHost, '-e', self.ansibleCFG, '-v']
            elif int(ansible_level) == 2:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', self.ansibleHost, '-e', self.ansibleCFG, '-vvv']
            else:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', self.ansibleHost, '-e', self.ansibleCFG, '-vvvvv']
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            self.clear_data()
            return output
        except subprocess.CalledProcessError as e:
            self.clear_data()
            return e.output


    def run_ansible_custom(self, path_playbook, path_host, ansible_level):
        path_playbook = path_playbook[1:]
        path_host = path_host[1:]
        try:
            if int(ansible_level) == 0:
                command = ['ansible-playbook', path_playbook, '-i', path_host, '-e', self.ansibleCFG]
            elif int(ansible_level) == 1:
                command = ['ansible-playbook', path_playbook, '-i', path_host, '-e', self.ansibleCFG, '-v']
            elif int(ansible_level) == 2:
                command = ['ansible-playbook', path_playbook, '-i', path_host, '-e', self.ansibleCFG, '-vvv']
            else:
                command = ['ansible-playbook', path_playbook, '-i', path_host, '-e', self.ansibleCFG, '-vvvvv']
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        except subprocess.CalledProcessError as e:
            return e.output

    # Serve para executar um Host padrão e um Playbook customizável
    def run_ansible_device(self, path_host, playbook_command, ansible_level, switch):
        self.write_ansible_playbook(playbook_command, switch)
        path_host = path_host[1:]
        try:
            if int(ansible_level) == 0:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', path_host, '-e', self.ansibleCFG]
            elif int(ansible_level) == 1:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', path_host, '-e', self.ansibleCFG, '-v']
            elif int(ansible_level) == 2:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', path_host, '-e', self.ansibleCFG, '-vvv']
            else:
                command = ['ansible-playbook', self.ansiblePlaybook, '-i', path_host, '-e', self.ansibleCFG, '-vvvvv']
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            self.clear_data()
            return output
        except subprocess.CalledProcessError as e:
            self.clear_data()
            return e.output


    def clear_data(self):
        playbook_file = open(self.ansiblePlaybook, 'w')
        playbook_file.close()
        host_file = open(self.ansibleHost, 'w')
        host_file.close()
        return True