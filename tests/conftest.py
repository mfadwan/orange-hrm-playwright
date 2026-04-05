import pytest


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


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    safe_goto(page, "https://opensource-demo.orangehrmlive.com/")

    yield page
    page.close()
