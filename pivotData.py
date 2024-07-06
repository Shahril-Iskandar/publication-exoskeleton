import pandas as pd

# Read Excel file
loadsol = pd.read_excel('Loadsol_GRF variables.xlsx')

def pivot_data(df, output_filename: str):
    """
    Pivot the DataFrame to transform the data and save it to a CSV file.

    Parameters:
    - df: DataFrame to be pivoted.
    - output_filename: Name of the output CSV file.
    """
    # Pivot the DataFrame
    pivot_df = df.pivot_table(index='ID', columns=['Exo', 'Condition', 'Load'], values=['Impact_Peak_Force_L', 'Impact_Peak_Force_R'])
                                                   
    # Flatten the multi-level columns
    pivot_df.columns = ['_'.join(col).strip() for col in pivot_df.columns.values]

    # Reset index to make 'ID' a column
    pivot_df.reset_index(inplace=True)

    # Save to CSV
    pivot_df.to_csv(output_filename, index=False)

    return pivot_df

loadsol_impact_force = pivot_data(loadsol, 'Loadsol_Impact_Force.csv')
loadsol_active_force = pivot_data(loadsol, 'Loadsol_Active_Force.csv')