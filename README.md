# DBCredentials

## Usage

Example:

    from db_credentials import DBCredentials
    creds = DBCredentials.DBCredentials()
    creds.loadFile( './db_credentials/test/test.creds' )

Expected format of cred file is:

    host=test_database
    username=test_user
    password=test_password

To access creds:

    print 'get_host: ', creds.get_host()
    print 'get_port: ', creds.get_port()
    print 'get_username: ', creds.get_username()
    print 'get_password: ', creds.get_password()

## Security Settings for Cred Files

Use file ownership and permissions to provide basic security.

Example:

    $ chmod 700 ./db_credentials/test/
    $ chmod 400 ./db_credentials/test/test.creds
    $ ls -la ./db_credentials/test/
    drwx------  test
    $ ls -la ./db_credentials/test/test.creds
    -r--------  test.creds

