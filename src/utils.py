import pandas as pd


def get_null_percentage(df):
    """Return the percentage of missing values for a given column."""
    null_count = df.isna().sum() / len(df)
    null_percent = null_count * 100
    return pd.DataFrame({
        "Null Count": null_count,
        "Null Percent": null_percent
    })

# def missing_summary(df):
#     get_null_percentage(df)