from pprint import pprint

memo = dict()
data = dict()
for num, line in enumerate(open('source.txt', 'r')):
    line = line.replace('\n', '').split(' ')
    try:
        if line[0] == '/:':
            memo['bus'] = line[1].split('=')[1]
            indent = 0
            dev_dict = False
        else:
            memo['previous_indent'] = indent
            memo['previous_device'] = dev_dict
            indent = line.index('|__')
            dev_dict = dict()
            dev_dict['device'] = line[indent+1].split('=')[1]
            dev_dict['class'] = line[indent+2].split('=')[1]
            dev_dict['bus'] = memo['bus']
            if dev_dict['class'].lower() == 'hub':
                dev_dict['input'] = list()
            if not memo['previous_device']:
                data[memo['bus']] = [dev_dict]
            else:
                if indent > memo['previous_indent']:
                    memo[memo['previous_indent']] = memo['previous_device']
                    memo['previous_device']['input'].append(dev_dict)
                else:
                    if indent-4 == 0:
                        data[memo['bus']].append(dev_dict)
                    else:
                        memo[indent-4]['input'].append(dev_dict)
    except Exception as e:
        print num+1
        print e

pprint(memo)
pprint(data)

