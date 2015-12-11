DBCredentials
=============

Usage
-----

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

Security Settings for Cred Files
--------------------------------

Use file ownership and permissions to provide basic security.

Example:

    $ sudo mkdir /etc/test
    $ sudo chown -R user:group /etc/test

    $ cat <<EOF > /etc/test/test.creds
    host=test_database
    username=test_user
    password=test_password
    EOF

    $ chmod 700 /etc/test
    $ chmod 400 /etc/test/*

Verify permissions:

    $ ls -la /etc/test
    drwx------  test
    $ ls -la /etc/test/test.creds
    -r--------  test.creds
