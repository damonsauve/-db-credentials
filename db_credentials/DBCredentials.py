#! /usr/local/bin/python

import sys
import re

class DBCredentials:

    def __init__( self ):

        self.creds = {
            'host':'',
            'port':'',
            'username':'',
            'password':'',
            'database':'',
        }

        return;

    # Load credentials from a file: no input validation.
    #
    def load_file( self, filename ):

        f = open( filename, 'r' )
        text = f.read()
        f.close

        #print text

        tuples = re.findall( r'(\w+)=([^\s]+)', text )

        #print tuples
        #[('host', 'localhost'), ('username', 'foo'), ('password', 'bar')]

        for tuple in tuples:
            self.creds[ tuple[0] ] = tuple[1]

        #print self.creds

        return

    def get_host( self ):
        return self.creds['host']

    def set_host( self, host ):
        self.creds['host'] = host

    # listener port - return if specified, otherwise default to 3306
    #
    def get_port( self ):
        if self.creds['port']:
            return self.creds['port']
        else:
            return '3306'

    def set_port( self, port ):
        self.creds['port'] = port

    def get_username( self ):
        return self.creds['username']

    def set_username( self, username ):
        self.creds['sid'] = username

    def get_password( self ):
        return self.creds['password']

    def set_password( self, password ):
        self.creds['password'] = password

    # database
    #
    def get_database( self ):
        if self.creds['database'] == '' and self.creds['host'] != '':
            self.creds['database'] = self.creds['host']

        return self.creds['database']

    def set_database( self, database ):
        self.creds['database'] = database
