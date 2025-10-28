
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/customer_login.php")
    page.fill('input[name="login_code"]', 'misu')
    page.click('button[type="submit"]')
    page.goto("http://localhost:8080/payment_transaction.php?id=1")
    page.select_option('select[name="payment_method"]', 'Coins.ph')
    page.screenshot(path="jules-scratch/verification/payment.png")
    browser.close()
