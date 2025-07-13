# Assignment: Build a Commercial Real Estate Search Web App

## Objective

Create a web application for searching commercial real estate listings. The app should allow users to filter listings by keywords, pagination, and sale method, and display the results in an interactive table with clickable links.

---

## Requirements

### 1. User Interface

- Use [Streamlit](https://streamlit.io/) to build the web interface.
- The app should have a clear title: **"Commercial Real Estate Search"**.

### 2. Keyword Filtering

- Load a list of keywords from a file named `keywords.txt`.
- Allow users to select one or more keywords from this list.
- Provide an input for users to add new keywords (comma-separated).
  - New keywords should be appended to `keywords.txt` if they do not already exist.
  - Newly added keywords should immediately become available for selection.

### 3. Pagination Controls

- Provide input fields for:
  - **Page Number** (minimum value: 1, default: 1)
  - **Page Size** (minimum: 1, maximum: 200, default: 200)

### 4. Sale Method Filter

- Provide an input for users to enter one or more sale method codes (comma-separated integers).
- If left blank, no sale method filter should be applied.

### 5. Fetching Listings

- When the user clicks a button (e.g., "Get Listings"), fetch the filtered listings by calling a function (e.g., `get_simplified_list`) with the selected filters.
- Show a loading spinner while fetching data.

### 6. Results Display

- Display the number of results found.
- Show the results in a table.
  - The table should include a column (`seoUrl`) with clickable links labeled "Go to Listing" that open in a new tab.

### 7. Error Handling

- If an error occurs during data fetching, display an error message to the user.

---

## Deliverables

- `app.py`: The Streamlit app implementing the above requirements.
- `keywords.txt`: A sample file with some initial keywords (one per line).
- `main.py`: Should contain a function to fetch and process data as described below.
- `README.md`: Brief instructions on how to run the app.

---

## Additional Task: main.py

- Create a `main.py` file that contains a function (e.g., `get_simplified_list`) to fetch and process commercial real estate listings from [Commercial Real Estate Australia](https://www.commercialrealestate.com.au/).
- The function should accept filters such as keywords, page number, page size, and sale method, and return a pandas DataFrame with the following columns:

| adid  | keyword     | seoUrl                                      | shortDescription    | displayableStreet | suburb | state | postcode |
| ----- | ----------- | ------------------------------------------- | ------------------- | ----------------- | ------ | ----- | -------- |
| 12345 | Liquidation | https://www.commercialrealestate.com.au/xyz | "Prime location..." | "123 Main St"     | Sydney | NSW   | 2000     |

- You may mock the data if you do not have access to the real API, but the DataFrame structure should match the above.

---

## Bonus (Optional)

- Allow users to remove keywords from the list.
- Add basic styling to improve the appearance of the app.

---

**Note:**  
You may mock the data returned by `get_simplified_list` if you do not have access to a real data source.

> Thank you Samir
>
> > Best of luck
