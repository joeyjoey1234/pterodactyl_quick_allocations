import requests
import time
endpoint = input('enter in your endpoint url example https://ptero-panel.com : ')
if endpoint[-1] == '/':
    pass
else:
    endpoint = endpoint + '/'


apikey = input("enter api key:   ")
apikey = str(apikey)

print("enter the ips you wish to allocate separated by spaces")

ips = input('')
ips = str(ips)
ips = ips.split(' ')

print("enter the ports you wish to allocate separated by spaces Example 4000-4500 5555 4444")

ports = input(' ')
ports = str(ports)
ports = ports.split(' ')

url = '{}api/application/nodes/2/allocations'.format(endpoint)


headers = {
    "Authorization": "Bearer {}".format(apikey),
    "Accept": "application/json",
    "Content-Type": "application/json"
}

count = 0
for ip in ips:
    for port in ports:
        count = count + 1
        python_sucks = ' "ip": "{}", "ports": [ "{}"] '.format(ip, port)
        payload = '{%s}' % (python_sucks)
        print('Doing {}'.format(python_sucks))
        response = requests.request('POST', url, data=payload, headers=headers)
        if response.text == '':
            pass
        else:
            print(response.text)
            print('it broke here {}'.format(python_sucks))
            quit()
        if count == 230:
            print('sleeping for 70 seconds to prevent hitting api limit')
            time.sleep(70)
            count = 0
        else:
            pass
