## UK Register of licensed sponsors
This is a Streamlit web application that displays the UK Register of Licensed Sponsors for workers.

### Features
- Fetches the latest sponsor list data directly from the UK government website
- Displays the data in an interactive table format using Streamlit
- Automatically updates when the source data is updated

### How it works
1. The app scrapes the [UK government website](https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers) to find the latest data file URL
2. Downloads and parses the CSV data using pandas
3. Presents the data in a searchable, sortable table format

### Requirements
- Python 3.x
- Required packages:
  - streamlit
  - pandas
  - beautifulsoup4
  - requests

### Running the app
1. Clone the repository
2. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app using streamlit:
   ```bash
   streamlit run app.py
   ```

