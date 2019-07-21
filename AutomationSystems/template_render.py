import json
import sys
from jinja2 import Environment, FileSystemLoader
from agavepy import Agave

'''
This script renders the system.json from the system templates and registers the system using agavepy

Run the script as following to register the storage system
python template_render.py <auth_token> template/storage.json storage_system_template.json <apiUsername> <apiPassword> <projectName> <reservation>

or 

Run the script as following to register the execution system
python template_render.py <auth_token> template/compute.json compute_system_template.json <apiUsername> <apiPassword> <allocation> <projectName> <reservation>


'''

# valid access token for the tenant above 
tok = sys.argv[1]
# system.json rendered file location
system_json_dest = sys.argv[2] 
# system.json template file location
system_template_source = sys.argv[3] 
#api user name
apiUserName = sys.argv[4]
#apiPassword 
apiPassword = sys.argv[5]
# allocation:  -A ProjectName -r ReservationName
projectName = sys.argv[6]
reservationName = sys.argv[7]
#directory for templates
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template(system_template_source)
output = template.render(UPDATEUSERNAME=apiUserName,UPDATEPASSWORD=apiPassword,UPDATEPROJECT=projectName,UPDATERESRVATION=reservationName)
# write rendered output to a file
sysfile = open(system_json_dest, 'w') 
sysfile.write(output)
sysfile.close()

with open(system_json_dest, 'r') as f:
    data = f.read()
    s = json.loads(data)

# register system with agave
ag = Agave(api_server='https://api.tacc.utexas.edu', token=tok)
ag.systems.add(body=s)


