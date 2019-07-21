This script renders the system.json from the system Jinja2 template and registers it using agavepy

Run the script as following to register the storage system
```
python template_render.py <auth_token> template/storage.json storage_system_template.json <apiUsername> <apiPassword> <projectName> <reservation>
```
or 

Run the script as following to register the execution system
```
python template_render.py <auth_token> template/compute.json compute_system_template.json <apiUsername> <apiPassword>  <projectName> <reservation>
```

Arg 1 Oauth token for the apiUser
Arg 2 Destination path for rendered json , for storage system it is template/storage.json and for execution system it is compute_system_template.json
Arg 3 Source path for template, for storage system it is storage_system_template.json and for execution system it is compute_system_template.json
Arg 4 is the apiUserName "train***"
Arg 5  project name required in the custom directive only for execution system
Arg 6. reservation name required in the custom directive only for execution system


