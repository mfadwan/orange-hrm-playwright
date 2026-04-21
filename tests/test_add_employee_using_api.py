from playwright.sync_api import Page, expect


def test_employee_created_via_api_is_visible_in_list(page: Page, add_employee):
    employee = add_employee

    page.goto(
        f"https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/{employee.emp_number}"
    )

    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()

    full_name = f"{employee.first} {employee.last}"
    expect(page.get_by_text(full_name)).to_be_visible()
