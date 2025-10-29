from playwright.sync_api import sync_playwright
from PIL import Image

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/login.php")
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'admin')
    page.click('button[type="submit"]')
    page.goto("http://localhost:8080/index.php")
    page.wait_for_selector('a[href="logout.php"]')
    page.goto("http://localhost:8080/customers.php")
    page.screenshot(path="jules-scratch/verification/admin_dashboard.png")
    page.goto("http://localhost:8080/index.php")
    page.screenshot(path="jules-scratch/verification/employer_dashboard.png")
    browser.close()

    # Combine screenshots
    img1 = Image.open("jules-scratch/verification/admin_dashboard.png")
    img2 = Image.open("jules-scratch/verification/employer_dashboard.png")
    combined_img = Image.new('RGB', (img1.width + img2.width, img1.height))
    combined_img.paste(img1, (0, 0))
    combined_img.paste(img2, (img1.width, 0))
    combined_img.save("jules-scratch/verification/combined_dashboard.png")

with sync_playwright() as playwright:
    run(playwright)
