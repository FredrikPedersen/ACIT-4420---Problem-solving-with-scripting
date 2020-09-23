from acit44202019 import ACIT4420_2019
from acit44202020 import ACIT4420_2020

class1 = ACIT4420_2020()
class1.set_graded_assignments([70, 70, 70, 70, 70, 70, 70])
class1.set_graded_assignment(2, 100)
class1.set_final_exam_result(76)
print(class1.get_grade())

class2 = ACIT4420_2019()
class2.set_normal_assignments([True, True, True, True, True, True, True])
class2.set_final_exam_result(76)
print(class2.get_grade())

class3 = ACIT4420_2020()
class3.set_graded_assignments([20, 20, 20, 20, 20, 20, 20])
class3.set_graded_assignment(2, 100)
class3.set_final_exam_result(84)
print(class3.get_grade())

class4 = ACIT4420_2019()
class4.set_normal_assignments([True, True, True, True, True, True, True])
class4.set_final_exam_result(84)
print(class4.get_grade())