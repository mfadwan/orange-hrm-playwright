from playwright.sync_api import expect


def test_candidate_created_via_api(page, add_candidate):
    candidate = add_candidate

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

    # 🔍 search
    search = page.get_by_placeholder("Search")
    search.fill(candidate.firstName)
    search.press("Enter")

    # ✅ verify
    row = page.locator("div.oxd-table-row", has_text=candidate.firstName)

    expect(row.first).to_be_visible(timeout=15000)
