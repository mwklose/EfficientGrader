import saspy
import os


class SASPyConnection:

    def __init__(self, usr_file: str):

        if not os.path.isfile(usr_file):
            raise Exception(
                f"File with user details not valid. Is: {usr_file}")

        self.session = saspy.SASsession()
