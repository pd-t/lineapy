import pandas as pd

raw_data_1 = {
    "subject_id": ["1", "2", "3", "4", "5"],
    "first_name": ["Alex", "Amy", "Allen", "Alice", "Ayoung"],
    "last_name": ["Anderson", "Ackerman", "Ali", "Aoni", "Atiches"],
}
raw_data_2 = {
    "subject_id": ["4", "5", "6", "7", "8"],
    "first_name": ["Billy", "Brian", "Bran", "Bryce", "Betty"],
    "last_name": ["Bonder", "Black", "Balwner", "Brice", "Btisan"],
}
data1 = pd.DataFrame(raw_data_1, columns=["subject_id", "first_name", "last_name"])
data2 = pd.DataFrame(raw_data_2, columns=["subject_id", "first_name", "last_name"])
all_data_col = pd.concat([data1, data2], axis=1)
linea_artifact_value = all_data_col
