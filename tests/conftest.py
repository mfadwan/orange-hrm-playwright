import pytest
from playwright.sync_api import Page

from data.api_routes import (
    CANDIDATES_URL,
    CREATE_CANDIDATE,
    CREATE_EMPLOYEE,
    CREATE_VACANCY,
    DELETE_EMPLOYEE,
    DELETE_VACANCY,
)
from data.candidate_data import Candidate
from data.employee_data import Employee
from data.vacancy_data import Vacancy


def safe_goto(page, url):
    import time

    for attempt in range(3):
        try:
            print(f"[TRY] Opening page (Attempt {attempt+1})")
            page.goto(url, wait_until="load", timeout=120000)
            print("[SUCCESS] Page loaded")
            return
        except Exception as e:
            print(f"[ERROR] {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

    raise Exception("❌ Failed to load page after 3 attempts")


@pytest.fixture()
def login_with_admin(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until="domcontentloaded")
    # page.goto("https://opensource-demo.orangehrmlive.com")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("heading", name="Dashboard").wait_for()

    return page


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    safe_goto(page, "https://opensource-demo.orangehrmlive.com/")

    yield page
    page.close()


@pytest.fixture()
def add_employee(page: Page, login_with_admin):
    employee = Employee()

    # 📡 API Call
    response = page.request.post(
        url=CREATE_EMPLOYEE,
        data={"firstName": employee.first, "middleName": employee.middle, "lastName": employee.last},
    )

    assert response.ok, f"Failed to create employee: {response.text()}"

    employee.emp_number = response.json()["data"]["empNumber"]

    yield employee

    # 🧹 Cleanup
    delete_response = page.request.delete(url=DELETE_EMPLOYEE, data={"ids": [employee.emp_number]})

    assert delete_response.ok, f"Failed to delete employee: {delete_response.text()}"


@pytest.fixture()
def add_vacancy(page, login_with_admin):
    vacancy = Vacancy()

    response = page.request.post(url=CREATE_VACANCY, data=vacancy.to_dict())

    assert response.ok, f"Failed to create vacancy: {response.text()}"

    vacancy.id = response.json()["data"]["id"]

    yield vacancy

    # 🧹 Cleanup
    delete_response = page.request.delete(url=DELETE_VACANCY, data={"ids": [vacancy.id]})

    assert delete_response.ok, f"Failed to delete vacancy: {delete_response.text()}"


@pytest.fixture()
def add_candidate(page, login_with_admin, add_vacancy):
    vacancy = add_vacancy  # to get the vacancy ID for the candidate
    candidate = Candidate(vacancyId=vacancy.id)

    response = page.request.post(url=CREATE_CANDIDATE, data=candidate.to_dict())

    assert response.ok, f"Failed to create candidate: {response.text()}"

    candidate.id = response.json()["data"]["id"]

    yield candidate

    # 🧹 Cleanup (FINAL FIX)
    delete_response = page.request.delete(url=CANDIDATES_URL, data={"ids": [candidate.id]})

    assert delete_response.ok, f"Failed to delete candidate: {delete_response.text()}"
