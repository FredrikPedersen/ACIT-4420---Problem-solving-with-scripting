import typing

from coursegrade import CourseGrade

class ACIT4420_2020(CourseGrade):

    def __init__(self):
        super().__init__()

        self._graded_assignments: typing.List = [None] * 7
        self._graded_assignments_weight: typing.List[int] = [5, 7, 10, 6, 7, 8, 7]

        self._final_exam_result: int = 0
        self._final_exam_weight: int = 50
