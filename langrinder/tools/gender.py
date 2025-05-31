from enum import StrEnum


class Gender(StrEnum):
    MALE   = "male"
    FEMALE = "female"
    OTHER  = "other"


class GenderGenerator:
    def __init__(self, gender: Gender):
        self.g = gender

    def gender(
            self,
            male: str,
            female: str,
            other: str = "",
    ):
        return (
            male if self.g== Gender.MALE
            else female if self.g == Gender.FEMALE
            else other
        )
