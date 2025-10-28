
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/login.php")
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'admin')
    page.click('button[type="submit"]')
    page.goto("http://localhost:8080/manual_payment.php?customer=1")
    page.select_option('select[name="payment_method"]', 'Coins.ph')
    page.screenshot(path="jules-scratch/verification/manual_payment.png")
    browser.close()
