from dataclasses import dataclass

# from faker import Faker

# faker = Faker()


@dataclass
class Vacancy:
    name: str = "Test Vacancy"  # field(default_factory=lambda: f"QA {faker.word()}")
    description: str = "Test vacancy created via API"

    jobTitleId: int = 22
    employeeId: int = 1
    numOfPositions: int = 1
    status: bool = True
    isPublished: bool = True

    id: int = None

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "jobTitleId": self.jobTitleId,
            "employeeId": self.employeeId,
            "numOfPositions": self.numOfPositions,
            "status": self.status,
            "isPublished": self.isPublished,
        }
