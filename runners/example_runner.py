from efficient_grader.efficient_grader import EfficientGrader

eg = EfficientGrader("files/saspy_example.sas")

eg.grade_exact_match("files/saspy_example_student1.sas")

print(eg.grade_table_contents("files/saspy_example_student1.sas"))
print(eg.grade_table_contents("files/saspy_example_student2.sas"))
