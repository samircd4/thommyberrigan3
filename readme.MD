# Commercial Real Estate Search App

This is a Streamlit web application for searching commercial real estate listings using keywords and other filters.

## Features

- Select one or more keywords from a list
- Specify page number and page size
- Optionally filter by sale method
- View results in a table

## Setup Instructions

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/samircd4/thommyberrigan3.git

   cd thommyberrigan3
   ```

2. **Install dependencies**:

   Make sure you have Python 3.7+ installed. Then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the data files**:

   Ensure the following files are present in the project directory:

   - `keywords.txt` (list of keywords, one per line)
   - `ads_details.xlsx` (Excel file with listing details)

4. **Run the app**:

   ```bash
   streamlit run app.py
   ```

5. **Open in your browser**:

   Streamlit will provide a local URL (usually http://localhost:8501) where you can use the app.

## Notes

- If you encounter any errors, make sure all required files are present and formatted correctly.
- You can modify `keywords.txt` to update the list of available keywords.

---

Feel free to customize this README as needed for your project!
