from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:8080/customer_login.php')
    page.screenshot(path='jules-scratch/verification/screenshot-before-login.png')
    page.fill('input[name="login_code"]', '123')
    page.click('button[type="submit"]')
    page.wait_for_url('http://localhost:8080/customer_dashboard.php')
    page.screenshot(path='jules-scratch/verification/customer_dashboard.png')
    page.goto('http://localhost:8080/statement_of_account.php')
    page.screenshot(path='jules-scratch/verification/statement_of_account.png')
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
