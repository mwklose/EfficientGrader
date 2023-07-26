import os
from efficient_grader.saspy_connection import SASPyConnection


class EfficientGrader:

    def __init__(self, sas_key: str):

        if not os.path.isfile(sas_key):
            raise Exception(f"Invalid SAS key: {sas_key}")

        self.sas_key = sas_key
        self.sas_connection = SASPyConnection(self.sas_key)

    def grade_student(self, sas_student: str) -> float:
        pass
