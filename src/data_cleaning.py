import pandas as pd


def load_data(file_path):
    """Load the Online Retail Excel dataset."""
    df = pd.read_excel(file_path)

    print("Dataset loaded successfully!")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df


def clean_data(df):
    """Clean and preprocess the Online Retail dataset."""

    # Make a copy
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove missing CustomerID
    df = df.dropna(subset=["CustomerID"])

    # Convert CustomerID to integer
    df["CustomerID"] = df["CustomerID"].astype(int)

    # Remove cancelled invoices
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

    # Keep only positive quantity
    df = df[df["Quantity"] > 0]

    # Keep only positive unit price
    df = df[df["UnitPrice"] > 0]

    # Create Revenue column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Reset index
    df = df.reset_index(drop=True)

    print("\nCleaning completed!")
    print(f"Remaining rows: {df.shape[0]}")
    print(f"Remaining columns: {df.shape[1]}")

    return df


if __name__ == "__main__":

    input_file = "../data/Online Retail.xlsx"

    df = load_data(input_file)

    df_clean = clean_data(df)

    # Save cleaned dataset
    df_clean.to_csv("../data/cleaned_online_retail.csv", index=False)

    print("\nCleaned dataset saved successfully!")