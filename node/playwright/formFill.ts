import { chromium } from "playwright-core";
import Browserbase from "@browserbasehq/sdk";
import { config } from "dotenv";
config();

async function createSession() {
    const bb = new Browserbase({ apiKey: process.env.BROWSERBASE_API_KEY! });
    const session = await bb.sessions.create({
        projectId: process.env.BROWSERBASE_PROJECT_ID!,
        // Add configuration options here
      });
    return session;
}

async function fillForm(inputs: any) {
    const session = await createSession()
    const browser = await chromium.connectOverCDP(session.connectUrl);

    // Getting the default context to ensure the sessions are recorded.
    const defaultContext = browser.contexts()[0];
    const page = defaultContext?.pages()[0];

    console.log(`View sessionreplay at https://browserbase.com/sessions/${session.id}`,);
    // Navigate to page
    await page.goto("https://forms.gle/f4yNQqZKBFCbCr6j7");

    // fill superpower
    await page.locator(`[role="radio"][data-value="${inputs.superpower}"]`).click();
    await page.waitForTimeout(1000);

    // fill features_used
    for (const feature of inputs.features_used) {
        await page.locator(`[role="checkbox"][aria-label="${feature}"]`).click();
    }
    await page.waitForTimeout(1000);

    // fill coolest_build
    await page.locator('input[jsname="YPqjbf"]').fill(inputs.coolest_build);
    await page.waitForTimeout(1000);

    // click submit button
    await page.locator('div[role="button"]:has-text("Submit")').click();

    // wait 10 seconds
    await page.waitForTimeout(10000);

    console.log("Shutting down...");
    await page.close();
    await browser.close();
}

const inputs = {
    "superpower": "Invisibility",
    "features_used": [
        "Stealth Mode",
        "Proxies",
        "Session Replay"
    ],
    "coolest_build": "A bot that automates form submissions across multiple sites.",
}
fillForm(inputs);