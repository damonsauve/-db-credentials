from unittest import TestCase

from db_credentials import DBCredentials

class TestDBCredentials( TestCase ):

    def setUp( self ):

        self.creds = DBCredentials.DBCredentials()

        self.creds.loadFile( '/Users/damonsauve/git/db-credentials/db_credentials/test/test.creds' )

        self.test_creds = {
            'host'      : 'test_database',
            'port'      : '1521',
            'username'  : 'test_user',
            'password'  : 'test_password',
            'database'  : 'test_database',
        }

    def test_get_host( self ):

        self.assertEqual( self.creds.get_host(), self.test_creds['host'] )

    def test_get_port( self ):

        self.assertEqual( self.creds.get_port(), self.test_creds['port'] )

    def test_get_username( self ):

        self.assertEqual( self.creds.get_username(), self.test_creds['username'] )

    def test_get_password( self ):

        self.assertEqual( self.creds.get_password(), self.test_creds['password'] )

    def test_get_database( self ):

        self.assertEqual( self.creds.get_database(), self.test_creds['database'] )

if __name__ == "__main__":
    unittest.main()
