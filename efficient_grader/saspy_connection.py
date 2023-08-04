import saspy
import os


class SASPyConnection:

    def __init__(self, key: str):

        if not os.path.isfile(key):
            raise Exception(
                f"File with user details not valid. Is: {key}")

        self.key = key
        self.session = saspy.SASsession()

    def run_code(self, usr_file: str):
        if not os.path.isfile(usr_file):
            raise Exception(
                f"File with user details not valid. Is: {usr_file}")

        with open(usr_file) as u:
            usr_html = self.session.submit(u.read())

        return usr_html

    def run_key(self):
        return self.run_code(self.key)
