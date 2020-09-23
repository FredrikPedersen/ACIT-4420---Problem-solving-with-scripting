import typing

from coursegrade import CourseGrade


class ACIT4420_2019(CourseGrade):

    def __init__(self):
        super().__init__()

        self._normal_assignments: typing.List = [None] * 7

        self._final_exam_result: int = 0
        self._final_exam_weight: int = 100
