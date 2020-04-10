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

api = API(prov)

# Store the roster inside of a variable
roster = api.get_roster()

exporter = Exporter(roster)

# Export the roster to a CSV format
exporter.export_csv()

