DBCredentials
-------------

To use (with caution), simply do::

    >>> from db_credentials import DBCredentials
    >>> creds = DBCredentials.DBCredentials()
    >>> creds.loadFile( './db_credentials/test/test.creds' )

Expected format of cred file is:

    host=test_database
    username=test_user
    password=test_password

To access creds:

    >>> print 'get_host: ', creds.get_host()
    >>> print 'get_port: ', creds.get_port()
    >>> print 'get_username: ', creds.get_username()
    >>> print 'get_password: ', creds.get_password()
