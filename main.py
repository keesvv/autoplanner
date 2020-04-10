#!/usr/bin/env python3

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

