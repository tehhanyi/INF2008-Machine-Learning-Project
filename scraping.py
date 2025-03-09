# group 1 , group 2 and group 1 + group 2 winning frequency at diff locations 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver with headless options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the webpage
    driver.get("https://www.singaporepools.com.sg/en/product/Pages/toto_wo.aspx")

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Find the table headers
    thead = driver.find_element(By.TAG_NAME, 'thead')
    headers = []
    for th in thead.find_elements(By.TAG_NAME, 'th'):
        # Extract the English text from the <span> element
        span = th.find_element(By.CLASS_NAME, 'english')
        headers.append(span.text.strip())

    # Debug: Print headers
    print("Number of headers:", len(headers))
    print("Headers:", headers)

    # Find the table body
    tbody = driver.find_element(By.TAG_NAME, 'tbody')

    # Extract rows
    rows = []
    for row in tbody.find_elements(By.TAG_NAME, 'tr'):
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells:
            # Extract data from the 'data-value' attribute of each cell
            row_data = [cell.get_attribute('data-value') for cell in cells]
            rows.append(row_data)

    # Debug: Print rows
    for i, row in enumerate(rows):
        print(f"Row {i + 1} has {len(row)} columns:", row)

    # Ensure headers and data have the same number of columns
    if len(headers) != len(rows[0]):
        print("Mismatch between headers and data columns. Adjusting headers.")
        headers = headers[:len(rows[0])]  # Truncate headers to match data columns

    # Handle inconsistent row lengths (if any)
    max_columns = max(len(row) for row in rows)
    rows = [row + [None] * (max_columns - len(row)) for row in rows]

    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Export to Excel
    df.to_excel('toto_winning_loc.xlsx', index=False)

    print("Data successfully saved to 'toto_winning_loc.xlsx'")

finally:
    # Close the browser
    driver.quit()