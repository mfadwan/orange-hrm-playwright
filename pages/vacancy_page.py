from playwright.sync_api import Page


class VacancyPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(60000)  # Set a reasonable default timeout for all actions
        self._added_vacancies = []

    def navigate_to_vacancies(self):
        # Click Recruitment (main menu)
        self.page.get_by_role("link", name="Recruitment", exact=True).first.click()

        # Click Vacancies tab
        self.page.get_by_role("link", name="Vacancies").click()

        # Wait for page
        self.page.locator("h5:has-text('Vacancies')").wait_for(state="visible")

    def click_add(self):
        self.page.get_by_role("button", name="Add").click()

    def add_vacancy(self, vacancy_name: str, job_title: str, hiring_manager: str, active: bool = True):
        self.click_add()

        # Vacancy name
        self.page.locator("div.oxd-input-group:has(label:has-text('Vacancy Name')) input").fill(vacancy_name)

        # Job title dropdown
        self.page.locator("div.oxd-input-group:has(label:has-text('Job Title')) div.oxd-select-text").click()
        self.page.get_by_role("listbox").wait_for()
        self.page.get_by_role("option", name=job_title).click()

        # Hiring manager
        manager_input = self.page.get_by_placeholder("Type for hints...")
        manager_input.fill(hiring_manager)
        # wait for dropdown suggestions
        self.page.get_by_role("option", name=hiring_manager).wait_for()
        self.page.get_by_role("option", name=hiring_manager).click()

        # Active toggle
        active_toggle = self.page.locator("div.oxd-switch-wrapper").nth(0)

        if not active:
            active_toggle.click()

        # Save
        self.page.locator("button:has-text('Save')").click()

        # Wait for success
        self.page.locator(".oxd-toast").filter(has_text="Success").wait_for()

        self._added_vacancies.append(vacancy_name)
