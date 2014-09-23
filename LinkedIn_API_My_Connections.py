import json
from prettytable import PrettyTable


connections_data = open("linkedin_connections.json","r")
connections = json.load(connections_data)

pt = PrettyTable(field_names=['Name', 'Location'])
pt.align = 'l'

[ pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name'])) 
  for c in connections['values']
      if c.has_key('location')]

print pt


