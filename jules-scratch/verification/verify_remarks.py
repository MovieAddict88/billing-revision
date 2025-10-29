from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/login.php")
    page.screenshot(path="jules-scratch/verification/login_page.png")
    page.get_by_placeholder("User Name").fill("admin")
    page.get_by_placeholder("Password").fill("admin")
    page.get_by_role("button", name="Login").click()
    page.goto("http://localhost:8080/customers.php")
    page.screenshot(path="jules-scratch/verification/admin_dashboard.png")
    page.goto("http://localhost:8080/index.php")
    page.screenshot(path="jules-scratch/verification/employer_dashboard.png")
    page.goto("http://localhost:8080/customer_login.php")
    page.get_by_placeholder("Login Code").fill("c06dbb145a03483e87603c0b1a7d653c")
    page.get_by_role("button", name="Login").click()
    page.screenshot(path="jules-scratch/verification/customer_dashboard.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
