# CSV Data Analyzer

## Project Description

CSV Data Analyzer is a web application developed using Python, Pandas, and Streamlit.

It allows users to upload a CSV file and analyze the dataset through an interactive and user-friendly interface.

## Problem Statement

Analyzing CSV datasets manually can be difficult and time-consuming, especially for beginners. Users may find it difficult to understand the dataset, identify missing values, calculate statistics, and filter required data.

## Proposed Solution

The CSV Data Analyzer provides a simple web-based solution where users can upload their own CSV files. The application automatically reads and analyzes the uploaded dataset and displays useful information such as rows, columns, statistics, missing values, and filtered data.

## Features

- Upload CSV files
- Display uploaded dataset
- Count rows and columns
- Analyze numeric data
- Display column information
- Detect missing values
- Filter data based on column values
- Download filtered data
- Display dataset summary
- Handle invalid CSV files
- Interactive Streamlit interface

## Technologies Used

- Python
- Pandas
- Streamlit

## How to Run

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit application

```bash
streamlit run main.py
```

### 3. Open the application

After running the command, Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open this URL in your web browser.

## How the Application Works

1. Open the CSV Data Analyzer application.
2. Upload a CSV file using the file uploader.
3. The application reads the uploaded CSV file using Pandas.
4. The complete dataset is displayed.
5. The number of rows and columns is calculated.
6. Numeric columns are analyzed and statistical information is displayed.
7. Column information and unique values are displayed.
8. Missing values are detected.
9. Users can search and filter the dataset.
10. Filtered data can be downloaded as a CSV file.
11. A final dataset summary is displayed.

## Expected Outcome

The application allows users to upload and explore CSV datasets without manually writing individual Python commands.

Users can:

- View the uploaded dataset
- Check the number of rows and columns
- Analyze numeric data
- Identify missing values
- View column information
- Filter required data
- Download filtered results
- View an overall dataset summary

## Project Structure

```text
CSV_Data_Analyzer/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Requirements

The project requires:

- Python 3.x
- Pandas
- Streamlit

## Future Enhancements

- Add data visualization charts
- Add multiple filtering options
- Add automatic data cleaning
- Add Excel file support
- Add more advanced statistical analysis

## Author

**Chandana-2006**

## License

This project is licensed under the MIT License.