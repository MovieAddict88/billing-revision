from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://localhost:8000/login.php")
    page.wait_for_selector('form.form-signin')
    page.fill('input[name="username"]', "admin")
    page.fill('input[name="password"]', "admin")
    page.click('button[type="submit"]')

    page.click('a[href="customers.php"]')
    page.wait_for_selector("#grid-basic")
    page.click('a[href^="disconnect_customer.php"]')
    page.wait_for_load_state("networkidle")

    page.click('a[href="disconnected_clients.php"]')
    page.wait_for_selector("#grid-basic")

    page.screenshot(path="jules-scratch/verification/disconnected_clients.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
