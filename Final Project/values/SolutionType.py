import enum


class SolutionType(enum.Enum):

    RECURSIVE_WALK = "Recursive Walk"
    A_STAR = "A*"

    @staticmethod
    def as_list():
        return list(map(lambda st: st.value, SolutionType))
