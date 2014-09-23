import json
from linkedin import linkedin 


CONSUMER_KEY = '75knk5spgqnma9'
CONSUMER_SECRET = 'xSdsQzy9WMtF8hvm'
USER_TOKEN = '5fbff52f-0f2a-43cd-acb4-434ca744b479'
USER_SECRET = '0d26cee6-94a0-44c4-be1f-8d6609c72afa'

RETURN_URL = ''

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

app = linkedin.LinkedInApplication(auth)


my_positions = app.get_profile(selectors=['positions'])
print json.dumps(my_positions, indent=1)


connections_data = open("linkedin_connections.json", "r")
connections = json.load(connections_data)
connection_id = connections['values'][100]['id']
connection_positions = app.get_profile(member_id=connection_id, 
                                       selectors=['positions'])
print json.dumps(connection_positions, indent=1)
