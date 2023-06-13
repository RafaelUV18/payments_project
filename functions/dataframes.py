import pandas as pd


def find_incorrect_values(df):
    incorrect_positions = []
    column_types = {
        'Fecha': 'Timestamp',
        'Monto': 'float',
        'Cliente': 'str', 
        'Proveedor': 'str'
    }
    for index, row in df.iterrows():
        for column, expected_data_type in column_types.items():
            value = row[column]
            actual_data_type = type(value).__name__

            if actual_data_type != expected_data_type:
                incorrect_positions.append((column, index+2))

    return incorrect_positions