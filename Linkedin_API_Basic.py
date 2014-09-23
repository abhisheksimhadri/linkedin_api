from linkedin import linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

# Instantiate the developer authentication class

CONSUMER_KEY = '75knk5spgqnma9'
CONSUMER_SECRET = 'xSdsQzy9WMtF8hvm'
USER_TOKEN = '5fbff52f-0f2a-43cd-acb4-434ca744b479'
USER_SECRET = '0d26cee6-94a0-44c4-be1f-8d6609c72afa'

RETURN_URL = '' # Not required for developer authentication

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                          USER_TOKEN, USER_SECRET, 
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

value = application.get_profile()

print value

