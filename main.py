import pandas as pd


def clean_data(df, file_type):
    """
    Standardise incoming supermarket data.
    Returns a cleaned copy of the DataFrame.
    """

    df = df.copy()

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Clean text columns
    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in text_columns:
        df[column] = df[column].apply(
            lambda value: value.strip()
            if isinstance(value, str)
            else value
        )

    # Convert date columns
    date_columns = {
        "sales": ["sale_date"],
        "inventory": ["inventory_date"],
        "products": []
    }

    for column in date_columns.get(file_type, []):
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

    # Remove exact duplicate rows
    rows_before = len(df)
    df = df.drop_duplicates().copy()
    duplicates_removed = rows_before - len(df)

    # Convert numeric columns
    numeric_columns = {
        "products": [
            "product_id", "cost_price",
            "selling_price", "reorder_level"
        ],
        "sales": [
            "product_id", "quantity", "discount"
        ],
        "inventory": [
            "product_id", "opening_stock",
            "stock_received", "damaged_units",
            "stock_count", "closing_stock"
        ]
    }

    for column in numeric_columns.get(file_type, []):
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    print("Rows before cleaning:", rows_before)
    print("Duplicate rows removed:", duplicates_removed)
    print("Rows after cleaning:", len(df))

    return df