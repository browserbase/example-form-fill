import os
from playwright.sync_api import sync_playwright
from browserbase import Browserbase
from dotenv import load_dotenv

load_dotenv()

def create_session():
    """Creates a Browserbase session."""
    bb = Browserbase(api_key=os.environ["BROWSERBASE_API_KEY"])
    session = bb.sessions.create(
        project_id=os.environ["BROWSERBASE_PROJECT_ID"],
        # Add configuration options here if needed
    )
    return session

def fill_form(inputs):
    """Automates form filling using Playwright with Browserbase."""
    session = create_session()
    print(f"View session at https://browserbase.com/sessions/{session.id}")

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(session.connect_url)

        # Get the default browser context and page
        context = browser.contexts[0]
        page = context.pages[0]

        # Navigate to the form page
        page.goto("https://forms.gle/f4yNQqZKBFCbCr6j7")

        # Select superpower
        page.locator(f'[role="radio"][data-value="{inputs["superpower"]}"]').click()
        page.wait_for_timeout(1000)

        # Select features used
        for feature in inputs["features_used"]:
            page.locator(f'[role="checkbox"][aria-label="{feature}"]').click()
        page.wait_for_timeout(1000)

        # Fill in coolest build
        page.locator('input[jsname="YPqjbf"]').fill(inputs["coolest_build"])
        page.wait_for_timeout(1000)

        # Click submit button
        page.locator('div[role="button"]:has-text("Submit")').click()

        # Wait 10 seconds
        page.wait_for_timeout(10000)

        print("Shutting down...")
        page.close()
        browser.close()

if __name__ == "__main__":
    inputs = {
        "superpower": "Invisibility",
        "features_used": [
            "Stealth Mode",
            "Proxies",
            "Session Replay"
        ],
        "coolest_build": "A bot that automates form submissions across multiple sites.",
    }
    fill_form(inputs)