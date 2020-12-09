import enum


class SolutionType(enum.Enum):

    BUILD_SOLUTION = "Build Solution"
    RECURSIVE = "Recursive"
    A_STAR = "A*"

    @staticmethod
    def as_list():
        return list(map(lambda st: st.value, SolutionType))
