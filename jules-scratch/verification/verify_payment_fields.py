
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/customer_login.php")
    print(page.content())
    page.fill('input[name="login_code"]', "CUST-00001")
    page.click('button[type="submit"]')
    page.goto("http://localhost:8080/manual_payment.php?customer=1")
    page.screenshot(path="jules-scratch/verification/verification.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
