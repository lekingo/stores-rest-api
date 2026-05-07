"""
blocklist.py 

This file just contains the blockist of the JWT tokens. It will be imported by the app and the logout resource so that tokens can be added to the blocklist when the user logs out.
"""

# Using a set is far from ideal. 
# TODO: consider using a database or redis to store the blocklist. 
BLOCKLIST = set()