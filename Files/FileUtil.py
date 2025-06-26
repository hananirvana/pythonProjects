"""
Sort Excel/CSV File Utility - Reads a file of records, sorts them, and then
writes them back to the file. Allow the user to choose various sort style and
sorting based on a particular field.
"""
import pandas as pd

def sort_csv(file_path, sort_by=None, ascending=True):
    # Read CSV into DataFrame
    df = pd.read_csv(file_path)

    # Perform sorting
    if sort_by is not None:
        df.sort_values(by=sort_by, ascending=ascending, inplace=True)
    else:
        # Default sorting by the first column if sort_by is not specified
        df.sort_index(axis=0, ascending=ascending, inplace=True)

    # Write sorted DataFrame back to CSV
    df.to_csv(file_path, index=False)

# Example usage
file_path = 'records.csv'
sort_by_field = 'Name'  # Example field to sort by
sort_csv(file_path, sort_by=sort_by_field, ascending=True)
