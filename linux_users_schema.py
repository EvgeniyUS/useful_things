import subprocess
from pprint import pprint


data = {}
for i in subprocess.check_output(['cat', '/etc/shadow']).decode('utf-8').strip().split('\n'):
    user_list = i.split(':')
    user_groups = subprocess.check_output(['id', user_list[0]]).decode('utf-8').strip().split(' ')[2].split('=')[1].split(',')
    data[user_list[0]] = {}
    for group in user_groups:
        group_id, group_name = group.strip(')').split('(')
        data[user_list[0]][group_name] = group_id


pprint(data)

