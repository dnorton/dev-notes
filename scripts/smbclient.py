class SMBClient(object):

    username, password, domain = None, None, None

    cifs_share = None
    smbclient_auth = []
    smbclient_cmd = []

    pipe = None  # the Popen object

    def __init__(self, user=None, pwd=None, domain=None, sharePath=None):
        self.username = user
        self.password = pwd
        self.domain = domain
        self.cifs_share = sharePath


    def __enter__(self):
        print "entering smbclient class"
        if self.username is None or self.password is None:
            self._auth()

        self.smbclient_cmd.extend(['smbclient', '-A', "/dev/stdin", '--option=clientntlmv2auth=no'])

        self.smbclient_auth.extend([
            "username = %s" % self.username,
            "password = %s" % self.password,
            "domain = %s" % self.domain
        ])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.pipe is not None:
            try:
                self.pipe.terminate()
            except:
                pass
            self.pipe = None
        self.smbclient_cmd = []
        print "exiting smbclient"

    def _auth(self):
        print "Enter your ssh credentials"
        if self.username is None:
            self.username = raw_input("Enter user name: ")
        if self.password is None:
            self.password = getpass.getpass("Enter your password: ")
        if self.domain is None:
            self.domain = raw_input("Enter user domain: ")

    def run(self, cmd=None):
        print "running %s on %s" % (cmd, self.cifs_share)
        if cmd is not None:
            self.smbclient_cmd.extend([self.cifs_share, '-c', cmd])
            print self.smbclient_cmd
            self.pipe = Popen(self.smbclient_cmd, stdin=PIPE)
            self.pipe.stdin.write(os.linesep.join(self.smbclient_auth))
            stdout, stderr = self.pipe.communicate()
            return stdout, stderr
