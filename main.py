import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="CSV Data Analyzer",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 CSV Data Analyzer")
st.write("Upload a CSV file to analyze and explore your dataset.")

# CSV Upload
file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if file is not None:

    try:
        # Read CSV file
        data = pd.read_csv(file)

        st.success("CSV file uploaded successfully!")

        # --------------------------------
        # Dataset
        # --------------------------------
        st.header("📋 Dataset")

        st.dataframe(
            data,
            use_container_width=True
        )

        # --------------------------------
        # Dataset Information
        # --------------------------------
        st.header("📌 Dataset Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Number of Rows",
                data.shape[0]
            )

        with col2:
            st.metric(
                "Number of Columns",
                data.shape[1]
            )

        # --------------------------------
        # Statistics
        # --------------------------------
        st.header("📈 Statistics")

        numeric_columns = data.select_dtypes(
            include="number"
        ).columns

        if len(numeric_columns) > 0:

            st.write("Statistical Summary")

            st.dataframe(
                data[numeric_columns].describe(),
                use_container_width=True
            )

        else:

            st.info(
                "No numeric columns found in this dataset."
            )

            st.write("Column Information")

            column_info = pd.DataFrame({
                "Column": data.columns,
                "Data Type": data.dtypes.astype(str).values,
                "Unique Values": [
                    data[column].nunique()
                    for column in data.columns
                ]
            })

            st.dataframe(
                column_info,
                use_container_width=True
            )

        # --------------------------------
        # Missing Values
        # --------------------------------
        st.header("🔍 Missing Values")

        missing_values = data.isnull().sum()

        missing_data = pd.DataFrame({
            "Column": missing_values.index,
            "Missing Values": missing_values.values
        })

        st.dataframe(
            missing_data,
            use_container_width=True
        )

        # --------------------------------
        # Filter Data
        # --------------------------------
        st.header("🔎 Filter Data")

        selected_column = st.selectbox(
            "Select a column",
            data.columns
        )

        search_value = st.text_input(
            "Enter value to search"
        )

        if search_value:

            filtered_data = data[
                data[selected_column]
                .astype(str)
                .str.contains(
                    search_value,
                    case=False,
                    na=False
                )
            ]

            st.write(
                "Number of Filtered Rows:",
                len(filtered_data)
            )

            st.dataframe(
                filtered_data,
                use_container_width=True
            )

            # Download filtered data
            csv_data = filtered_data.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="⬇️ Download Filtered Data",
                data=csv_data,
                file_name="filtered_data.csv",
                mime="text/csv"
            )

        # --------------------------------
        # Summary
        # --------------------------------
        st.header("📝 Summary")

        total_rows = data.shape[0]
        total_columns = data.shape[1]
        numeric_count = len(numeric_columns)
        text_count = total_columns - numeric_count
        total_missing = data.isnull().sum().sum()

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "Total Rows",
                total_rows
            )

        with col2:
            st.metric(
                "Total Columns",
                total_columns
            )

        with col3:
            st.metric(
                "Numeric Columns",
                numeric_count
            )

        with col4:
            st.metric(
                "Text Columns",
                text_count
            )

        with col5:
            st.metric(
                "Missing Values",
                total_missing
            )

    except Exception as e:

        st.error(
            "Unable to read the CSV file. "
            "Please upload a valid CSV file."
        )

else:

    st.info(
        "Please upload a CSV file to begin."
    )