# To-Do List for Commercial Real Estate Search App

## 1. Set Up the Project

- [] Create a new project directory (if not already done).
- [ ] Set up a Python virtual environment (optional but recommended).
- [x] Install required packages:  
      `pip install streamlit pandas requests openpyxl`

## 2. Prepare Data Files

- [x] Create a `keywords.txt` file with some initial keywords (one per line).

## 3. Develop main.py

- [ ] Implement a function (e.g., `get_simplified_list`) that:
  - [ ] Accepts filters: keywords, page number, page size, sale method.
  - [ ] Fetches or mocks commercial real estate listings from [commercialrealestate.com.au](https://www.commercialrealestate.com.au/).
  - [ ] Returns a pandas DataFrame with columns:  
        `adid`, `keyword`, `seoUrl`, `shortDescription`, `displayableStreet`, `suburb`, `state`, `postcode`.

## 4. Develop app.py (Streamlit App)

- [ ] Set up the Streamlit page with a title.
- [ ] Load keywords from `keywords.txt`.
- [ ] Add a multiselect widget for keywords.
- [ ] Add a text input to allow users to add new keywords (and update `keywords.txt`).
- [ ] Add input fields for page number and page size.
- [ ] Add input for sale method (comma-separated integers).
- [ ] Add a button to fetch listings.
- [ ] On button click:
  - [ ] Call `get_simplified_list` with the selected filters.
  - [ ] Show a loading spinner while fetching.
  - [ ] Display the number of results found.
  - [ ] Display the results in a table, with the `seoUrl` column as clickable links.
  - [ ] Handle and display any errors.

## 5. Testing

- [ ] Test the app with different keyword and filter combinations.
- [ ] Test adding new keywords and ensure they persist.
- [ ] Test error handling (e.g., with invalid input or no results).

## 6. Documentation

- [ ] Write a `README.md` with:
  - [ ] Project description.
  - [ ] Setup and run instructions.
  - [ ] Any notes or requirements.

## 7. (Optional) Bonus Features

- [ ] Allow users to remove keywords from the list.
- [ ] Add basic styling/customization to improve the app’s appearance.

---

**Reference:**  
Listings are sourced from [Commercial Real Estate Australia](https://www.commercialrealestate.com.au/).
