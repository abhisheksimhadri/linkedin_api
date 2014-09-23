from geopy import geocoders
import json


GEO_APP_KEY = 'An8mawuxNvC8EzpI3iDaTD1RzvgZVuuaAtMbnLDXPihDVFsRkZo5Jzn77K6u_Ha4' # XXX: Get this from https://www.bingmapsportal.com
g = geocoders.Bing(GEO_APP_KEY)

transforms = [('Greater ', ''), (' Area', '')]

connections = json.loads(open('linkedin_connections.json').read())

results = {}
for c in connections['values']:
    if not c.has_key('location'): continue
        
    transformed_location = c['location']['name']
    for transform in transforms:
        transformed_location = transformed_location.replace(*transform)
    geo = g.geocode(transformed_location, exactly_one=False)
    if geo == []: continue
    results.update({ c['location']['name'] : geo })
    
print json.dumps(results, indent=1)


