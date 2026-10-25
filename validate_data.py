import pandas as pd

REQUIRED_COLUMNS = {
    "products": [
        "product_id", "product_name", "category",
        "cost_price", "selling_price", "reorder_level"
    ],
    "sales": [
        "bill_number", "sale_date", "product_id",
        "quantity", "discount", "payment_method"
    ],
    "inventory": [
        "inventory_date", "product_id", "opening_stock",
        "stock_received", "damaged_units", "stock_count",
        "closing_stock"
    ]
}


def validate_file(file_path, file_type):

    if file_type not in REQUIRED_COLUMNS:
        return False, f"Unsupported file type: {file_type}"

    try:
        df = pd.read_csv(file_path)
    except Exception as error:
        return False, f"Could not read CSV: {error}"

    missing = set(REQUIRED_COLUMNS[file_type]) - set(df.columns)

    if missing:
        return False, f"Missing columns: {sorted(missing)}"

    if df.empty:
        return False, "CSV file is empty."

    if df[REQUIRED_COLUMNS[file_type]].isnull().any().any():
        return False, "Required columns contain missing values."

    return True, f"Validation successful: {len(df)} rows checked."