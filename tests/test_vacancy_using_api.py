from playwright.sync_api import expect


def test_vacancy_created_via_api(page, add_vacancy):
    vacancy = add_vacancy

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

    search = page.get_by_placeholder("Search")
    search.fill(vacancy.name)
    search.press("Enter")

    row = page.get_by_role("row", name=vacancy.name)

    expect(row.first).to_be_visible(timeout=15000)


"""def test_vacancy_created_via_api(page, add_vacancy):

    vacancy = add_vacancy

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

    expect(page.get_by_text(vacancy.name)).to_be_visible()"""
