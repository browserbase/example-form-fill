# Python Form Fill Demo

This demo shows how to automate form filling using Playwright and Browserbase.

## Setup

1. Create and activate a virtual environment:

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your API keys:
     - `BROWSERBASE_API_KEY`: Your Browserbase API key
     - `BROWSERBASE_PROJECT_ID`: Your Browserbase project ID

## Running the Demo

The `form_fill.py` script demonstrates automated form filling. It will:
- Create a new Browserbase session
- Navigate to a Google Form
- Fill in various fields
- Submit the form

Run the script:
```bash
python form_fill.py
```

You can modify the input values in the `inputs` dictionary at the bottom of `form_fill.py` to change the form responses.

The script will print a URL where you can view the session replay on Browserbase.

