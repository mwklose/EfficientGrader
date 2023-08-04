import os
import pandas as pd
from bs4 import BeautifulSoup

from efficient_grader.saspy_connection import SASPyConnection


class EfficientGrader:

    def __init__(self, sas_key: str):

        if not os.path.isfile(sas_key):
            raise Exception(f"Invalid SAS key: {sas_key}")

        self.sas_key = sas_key
        self.sas_connection = SASPyConnection(self.sas_key)

    def grade_exact_match(self, sas_student: str) -> float:
        # The HTML from the KEY must exactly equal the HTML from the student output.
        # Only use in rare circumstances.
        key_html = self.sas_connection.run_key()
        usr_html = self.sas_connection.run_code(sas_student)

        return 1 * (key_html['LST'] in usr_html['LST'])

    def grade_table_contents(self, sas_student: str) -> float:

        key_html = self.sas_connection.run_key()
        usr_html = self.sas_connection.run_code(sas_student)

        with open("runners/keyhtml.html", "w+") as khtml:
            khtml.write(key_html['LST'])

        if not os.path.exists(os.path.dirname(f"runners/{sas_student}")):
            os.makedirs(os.path.dirname(f"runners/{sas_student}"))

        with open(f"runners/{sas_student}.html", "w+") as uhtml:
            uhtml.write(usr_html['LST'])

        key_soup = BeautifulSoup(key_html['LST'], "html.parser")
        usr_soup = BeautifulSoup(usr_html['LST'], "html.parser")

        usr_soup_df = [pd.read_html(str(t))
                       for t in usr_soup.find_all("table")]
        key_soup_df = [pd.read_html(str(t))
                       for t in key_soup.find_all("table")]

        grade_dict = {}
        for i, t in enumerate(key_soup_df):
            key_table = t[0]
            grade_dict[i] = any([key_table.equals(ugd[0])
                                for ugd in usr_soup_df])

        return sum(grade_dict.values()) / len(grade_dict.keys())

    def grade_student(self, sas_student: str) -> float:

        print("Grading Student started.")
