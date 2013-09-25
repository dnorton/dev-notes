class Remote:
    """
    Container class for SSH functionality. Needs to be used in a with statement.
    
    with Remote() as remote:
      remote.connect("github.com", "me", "mypassword");
    
    """

    ssh_client = None
    user, password = None, None

    def __enter__(self):
        if self._has_paramiko():
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            paramiko.util.log_to_file("C:\\tmp\\paramiko.log")
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):

        try:
            if self.ssh_client is not None:
                self.ssh_client.close()
        except:
            print "received an exception closing the ssh connection."
        finally:
            self.ssh_client = None


    def connect(self, server, username=None, password=None):

        if not self._has_paramiko():
            return

        if username is None and password is None \
            and self.user is None and self.password is None:
            self._get_auth()
        else:
            self.user = username
            self.password = password

        try:
            self.ssh_client.connect(server, username=self.user, password=self.password)
        except paramiko.AuthenticationException:
            print "you entered an incorrect username or password.  Please try again"
            self._get_auth()
            try:
                self.ssh_client.connect(server, username=self.user, password=self.password)
            except:
                print "you entered an incorrect username or password a second time. Exiting"
                sys.exit(1)

    def get_sftp(self):

        transport = self.ssh_client.get_transport()
        return transport.open_sftp_client()

    def execute(self, command, sudo=False):

        if not self._has_paramiko():
            return None, None, None

        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        if sudo:
            stdin.write(self.password + '\n')
            stdin.flush()

        return stdin, stdout, stderr

    def _get_auth(self):
        print "Enter your ssh credentials"
        self.user = raw_input("Enter user name: ")
        self.password = getpass.getpass("Enter your password: ")


    def _has_paramiko(self):
        return 'paramiko' in sys.modules.keys()
