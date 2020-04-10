#!/usr/bin/env python3
import sys
from os import path

if not path.isfile('config.py'):
    print('You need to create a configuration file first. '\
        + 'View the README for more information.')
    sys.exit(1)

import config
from api import API
from auth import AuthProvider
from export import Exporter

# Instantiate a Authentication Provider
prov = AuthProvider(config.SCHOOL_URL)

# Authenticate the user
prov.authenticate()

# Initialize the API
api = API(prov)
api.initialize()

# Store the roster inside of a variable
roster = api.get_roster()

# Export the roster to a CSV format
exporter = Exporter(roster)
exporter.export_csv()

