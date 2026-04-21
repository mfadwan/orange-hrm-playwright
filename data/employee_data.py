from dataclasses import dataclass, field

from faker import Faker

faker = Faker()


@dataclass
class Employee:
    first: str = field(default_factory=faker.first_name)
    middle: str = field(default_factory=faker.first_name)
    last: str = field(default_factory=faker.last_name)
    pic_path: str = None
    emp_number: int = None
