import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="PIM").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("mohammed")
    page.get_by_role("textbox", name="Middle Name").click()
    page.get_by_role("textbox", name="Middle Name").fill("fouad")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("adwan")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("textbox").nth(4).click()
    page.get_by_role("textbox").nth(4).fill("0445")
    page.get_by_role("button", name="Save").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/241")
    page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").first.click()
    page.get_by_role("option", name="Afghan").click()
    page.locator("div").filter(has_text=re.compile(r"^-- Select --$")).nth(2).click()
    page.get_by_text("Married").click()
    page.locator("form").filter(has_text="Employee Full NameEmployee").get_by_role("button").click()
    page.locator(".orangehrm-card-container > .oxd-form > .oxd-form-row > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").click()
    page.get_by_role("option", name="AB+").click()
    page.locator("form").filter(has_text="Blood TypeAB+Test_Field Save").get_by_role("button").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
