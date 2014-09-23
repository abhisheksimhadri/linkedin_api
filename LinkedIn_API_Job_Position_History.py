import json
from linkedin import linkedin 


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = '----'
USER_SECRET = '----'

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
