#! /usr/local/bin/python

"""Generic interface to handle database connection parameters."""

import re

class DBCredentials:
    """Class to manage database connection credentials."""

    def __init__(self):

        self.creds = {
            'host': '',
            'port': '',
            'username': '',
            'password': '',
            'database': '',
        }

    def load_file(self, filename):
        """Load credentials from a file; no input validation."""

        with open(filename, 'r') as creds_file:
            text = creds_file.read()
        creds_file.close()

        pairs = re.findall(r'(\w+)=([^\s]+)', text)

        for pair in pairs:
            self.creds[pair[0]] = pair[1]

        #print self.creds

    def get_params(self):
        """Returns all connection parameters."""

        return self.creds

    def get_host(self):
        """Returns host."""

        return self.creds['host']

    def set_host(self, host):
        """Sets host."""

        self.creds['host'] = host

    def get_port(self):
        """Returns port."""

        if self.creds['port']:
            return self.creds['port']
        else:
            return '3306'

    def set_port(self, port):
        """Sets port."""

        self.creds['port'] = port

    def get_username(self):
        """Returns username."""

        return self.creds['username']

    def set_username(self, username):
        """Sets username."""

        self.creds['sid'] = username

    def get_password(self):
        """Returns password."""

        return self.creds['password']

    def set_password(self, password):
        """Sets password."""

        self.creds['password'] = password

    def get_database(self):
        """Returns database name."""

        if self.creds['database'] == '' and self.creds['host'] != '':
            self.creds['database'] = self.creds['host']

        return self.creds['database']

    def set_database(self, database):
        """Sets database name."""

        self.creds['database'] = database
