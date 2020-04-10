#!/usr/bin/env python3

import config
from auth import AuthProvider

prov = AuthProvider(config.SCHOOL_URL)

prov.authenticate()

