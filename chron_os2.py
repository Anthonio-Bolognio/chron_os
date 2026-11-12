from cmd import Cmd
class Prompt(Cmd):
    prompt = 'ChronOS v2.0.0a1> '
    intro = 'ChronOS v2.0.0a1 (This is a version of ChronOS for that is completely refactored and will have everything eventually. For the live v1 version, go to https://github.com/anthonio-bolognio/chron_os)'
    def __init__(self, accounts: dict = {"admin": ''}):
        self._accounts = accounts|({"admin": ''} if not "admin" in accounts else {})
        self.logged_in = False
        self.admin = False
    def do_login(self, username):
        if not self.logged_in:
            if username in self._accounts:
                passw = input(f"password for {username}: ")
                if passw == self._accounts[username]:
                    self.logged_in = True
                    self.admin = username=='admin'
                else:
                    print("Wrong Username/Password")
            else:
                print("Invalid Username - use 'signup' instead")
        else:
            print("Already logged in - use 'logout'")
    def do_signup(self, username):
        if not self.logged_in:
            if not username in self._accounts:
                passw = input(f"Password for new account {username}:")
                self._accounts[username] = passw
                self._logged_in = True
            else:
                print(f"User {username} already exists. Change your username or use 'login'")
        else:
            print("You are already logged in - use 'logout' first")
    def do_logout(self, quit:bool):
        if self.logged_in:
            self.logged_in = False
            self.admin = False
        else:
            print("Log in/Sign up first ('login' or 'signup')")