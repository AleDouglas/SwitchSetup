import subprocess

class AnsibleSwitchConnector:

    def __init__(self):
        self.huaweiHost = 'backend/integrations/communs/huawei/hosts.yml'
        self.ciscoHost = 'backend/integrations/communs/cisco/hosts.yml'
        self.huaweiPlaybook = 'backend/integrations/communs/huawei/playbook.yml'
        self.ciscoPlaybook = 'backend/integrations/communs/cisco/playbook.yml'
        self.ansibleHost = 'backend/integrations/communs/ansible/hosts.yml'
        self.ansiblePlaybook = 'backend/integrations/communs/ansible/playbook.yml'
        self.ansibleCFG = 'backend/integrations/communs/ansible/ansible.cfg'

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
            command_str = f'        commands: {command_list[0]}\n'

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

    def run_ansible(self):
        try:
            command = ['ansible-playbook', self.ansiblePlaybook, '-i', self.ansibleHost]
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