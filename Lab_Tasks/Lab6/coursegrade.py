import typing


class CourseGrade:

    def __init__(self):
        self._normal_assignments: typing.List[bool] = None

        self._graded_assignments: typing.List[int] = None
        self._graded_assignments_weight: typing.List[int] = None

        self._final_exam_result: int = None
        self._final_exam_weight: int = None

# ----------------- Public Methods ----------------- #

    def get_grade(self) -> str:
        grade_score = self.__calculate_total_grade_score()

        if grade_score < 40:
            return "F"
        elif 40 <= grade_score < 50:
            return "E"
        elif 50 <= grade_score < 60:
            return "D"
        elif 60 <= grade_score < 80:
            return "C"
        elif 80 <= grade_score < 90:
            return "B"
        elif grade_score >= 90:
            return "A"

# ----------------- Private Methods ----------------- #

    def __calculate_total_grade_score(self) -> int:
        """
        Calculates the total nummerical grade score based on a few requirements:
         - The final exam score must be more than 40 to get a passing grade.
         - If there were non-graded obligatory assignments, all of them must have been handed in.
         - If there were graded obligatory assignments, all of them must have been handed in and their combined score
           must equal a passing grade for the total grade to be valid. See __calculate_score_from_graded_assignments.
         - Score from the final exam is added to the score result multiplied with how many percent it is weighted
           towards the final score.

        :return: If any failure states are reached, returns 0, else the combined score from the graded assignments and
                 and the final exam.

        """
        grade_score: int = 0

        if self._final_exam_result < 40:
            return 0

        if self._normal_assignments is not None:
            if not self.__control_normal_assignments_approved():
                return 0

        if self._graded_assignments is not None:
            score_from_graded_assignments: int = self.__calculate_score_from_graded_assignments()
            if score_from_graded_assignments == 0:
                return 0
            else:
                grade_score += score_from_graded_assignments

        grade_score += self._final_exam_result * (self._final_exam_weight/100)

        return grade_score

    def __control_normal_assignments_approved(self) -> bool:
        """
        If there were non-graded obligatory assignments, all of them must have been approved to get a passing grade.

        :return: false if an assignment was not approved, otherwise returns true.
        """
        for approved in self._normal_assignments:
            if not approved:
                return False

        return True

    def __calculate_score_from_graded_assignments(self) -> int:
        """
        Calculates the total score from the graded assignments based on the following requirements:
         - All assignments where handed in, it is considered a failing grade.
         - The sum percentage of the graded assignments must be higher than 40.

        :return: The sum of all the graded assignments multiplied by their percentage weight towards the total grade,
                 0 if any of the aforementioned requirements are broken.
        """
        assignment_score_sum: int = 0
        grade_score: int = 0

        for i in range(len(self._graded_assignments)):
            if self._graded_assignments[i] is not None:
                assignment_score_sum += self._graded_assignments[i]
                grade_score += self._graded_assignments[i] * (self._graded_assignments_weight[i]/100)
            else:
                return 0

        if (assignment_score_sum/len(self._graded_assignments)) < 40:
            return 0

        return grade_score

# ----------------- Getters and Setters ----------------- #

    def get_normal_assignments(self) -> typing.List[bool]:
        if self._normal_assignments is None:
            raise Exception("This class has no normal assignments")

        return self._normal_assignments

    def get_graded_assignments(self) -> typing.List[int]:
        if self._graded_assignments is None:
            raise Exception("This class has no graded assignments")

        return self._graded_assignments

    def get_final_exam_result(self) -> int:
        if self._final_exam_result is None:
            raise Exception("This class has no final exam")

        return self._final_exam_result

    def set_normal_assignments(self, normal_assignments: typing.List[bool]):
        if self._normal_assignments is None:
            raise Exception("This class has no normal assignments")

        self._normal_assignments = normal_assignments

    def set_normal_assignment(self, assignment_number: int, approved: bool):
        if self._normal_assignments is None:
            raise Exception("This class has no normal assignments")

        self._normal_assignments[assignment_number] = approved

    def set_graded_assignments(self, graded_assignments: typing.List[int]):
        if self._graded_assignments is None:
            raise Exception("This class has no graded assignments")

        if len(graded_assignments) != len(self._graded_assignments):
            raise Exception("Passed invalid number of assignment scores")

        self._graded_assignments = graded_assignments

    def set_graded_assignment(self, assignment_number: int, score: int):
        if self._graded_assignments is None:
            raise Exception("This class has no graded assignments")

        self._graded_assignments[assignment_number] = score

    def set_final_exam_result(self, final_exam_result: int):
        if self._final_exam_result is None:
            raise Exception("This class has no final exam")

        self._final_exam_result = final_exam_result
