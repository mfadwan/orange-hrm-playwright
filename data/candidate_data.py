from dataclasses import dataclass, field
from datetime import datetime

from faker import Faker

faker = Faker()


@dataclass
class Candidate:
    firstName: str = field(default_factory=lambda: faker.first_name())
    middleName: str = None
    lastName: str = field(default_factory=lambda: faker.last_name())
    email: str = field(default_factory=lambda: faker.email())
    contactNumber: str = None
    keywords: str = None
    comment: str = None
    dateOfApplication: str = field(default_factory=lambda: datetime.today().strftime("%Y-%m-%d"))
    consentToKeepData: bool = False
    vacancyId: int = 16  # Assuming this vacancy ID exists in the system

    id: int = None

    def to_dict(self):
        return {
            "firstName": self.firstName,
            "middleName": self.middleName,
            "lastName": self.lastName,
            "email": self.email,
            "contactNumber": self.contactNumber,
            "keywords": self.keywords,
            "comment": self.comment,
            "dateOfApplication": self.dateOfApplication,
            "consentToKeepData": self.consentToKeepData,
            "vacancyId": self.vacancyId,
        }
