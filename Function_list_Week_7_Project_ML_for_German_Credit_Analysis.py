Function_list_Week_7_Project_ML_for_German_Credit_Analysis

_____Functions for Data Cleaning_____
'''

# ___for all Columns___

# Drop Columns
def drop_columns(df):
    df = df.drop(columns=["Unnamed: 0"])
    return df

# Drop Duplicates
def drop_duplicates(df):
    df = df.drop_duplicates()
    return df

# ___each Column seperatly___

# Rename Column
def change_age_column(df):
    df = df.rename(columns={"Age": "age"})
    return df

# Rename Column
def change_sex_column(df):
    df = df.rename(columns={"Sex": "sex"})
    return df

# Rename Column
def change_job_column(df):
    df = df.rename(columns={"Job": "job"})
    return df

# Rename Column and replace " " with "_"
def change_housing_column(df):
    df = df.rename(columns={"Housing": "housing"})
    df['housing'] = df['housing'].str.replace(" ", "_")
    return df

# Rename Column # Rename Column and replace " " with "_"
def change_saving_accounts_column(df):
    df = df.rename(columns={"Saving accounts": "saving_accounts"})
    df['saving_accounts'] = df['saving_accounts'].str.replace(" ", "_")
    df = df.dropna(subset=['saving_accounts'])
    return df

# Rename Column and replace " " with "_"
def change_checking_account_column(df):
    df = df.rename(columns={"Checking account": "checking_account"})
    df['checking_account'] = df['checking_account'].str.replace(" ", "_")
    df = df.dropna(subset=['checking_account'])
    return df

def change_credit_amount_column(df):
    df = df.rename(columns={"Credit amount": "credit_amount"})
    mean_credit_amount = df['credit_amount'].mean()
    mean_credit_amount_rounded = int(mean_credit_amount)
    df['credit_amount'] = df['credit_amount'].fillna(mean_credit_amount)
    return df

# Rename Column
def change_duration_column(df):
    df = df.rename(columns={"Duration": "duration"})
    return df

# Rename Column and replace " " with "_"
def change_purpose_column(df):
    df = df.rename(columns={"Purpose": "purpose"})
    df['purpose'] = df['purpose'].str.lower()
    df['purpose'] = df['purpose'].str.replace(" ", "_")
    return df

# Rename Column
def change_risk_column(df):
    df = df.rename(columns={"Risk": "risk"})
    return df


'''
_____Functions for Data Cleaning for Machine Learing_____
'''

# Function to transform sex column
def transform_sex(df):
    df['sex_male'] = df['sex'].apply(lambda x: 1 if x == 'male' else 0)
    df['sex_female'] = df['sex'].apply(lambda x: 1 if x == 'female' else 0)

# Function to transform housing column
def transform_housing(df):
    df['housing_own'] = df['housing'].apply(lambda x: 1 if x == 'own' else 0)
    df['housing_free'] = df['housing'].apply(lambda x: 1 if x == 'free' else 0)
    df['housing_rent'] = df['housing'].apply(lambda x: 1 if x == 'rent' else 0)

# Function to transform saving_accounts column
def transform_saving_accounts(df):
    saving_map = {'little': 0, 'moderate': 1, 'quite_rich': 2, 'rich': 3}
    df['saving_accounts'] = df['saving_accounts'].map(saving_map)

# Function to transform checking_account column
def transform_checking_account(df):
    checking_map = {'moderate': 0, 'little': 1, 'rich': 2}
    df['checking_account'] = df['checking_account'].map(checking_map)

# Function to transform purpose column into seperate columns
def transform_purpose(df):
    df['purpose_radio/tv'] = df['purpose'].apply(lambda x: 1 if x == 'radio/tv' else 0)
    df['purpose_furniture/equipment'] = df['purpose'].apply(lambda x: 1 if x == 'furniture/equipment' else 0)
    df['purpose_car'] = df['purpose'].apply(lambda x: 1 if x == 'car' else 0)
    df['purpose_business'] = df['purpose'].apply(lambda x: 1 if x == 'business' else 0)
    df['purpose_domestic_appliances'] = df['purpose'].apply(lambda x: 1 if x == 'domestic_appliance' else 0)
    df['purpose_repairs'] = df['purpose'].apply(lambda x: 1 if x == 'repairs' else 0)
    df['purpose_vacation/others'] = df['purpose'].apply(lambda x: 1 if x == 'vacation/others' else 0)
    df['purpose_education'] = df['purpose'].apply(lambda x: 1 if x == 'education' else 0)

# Function to transform the entire dataframe and add risk column back and move to end
def transform_dataframe(df):
    transform_sex(df)
    transform_housing(df)
    #transform_saving_accounts(df)
    #transform_checking_account(df)
    transform_purpose(df)
    # Adding the 'risk' column back
    df['risk'] = df['risk'].apply(lambda x: 1 if x == 'good' else 0)  # Assuming 'good' = 1, 'bad' = 0
    # Move risk column to end
    cols = df.columns.tolist()
    cols.remove('risk')  # Remove risk column temporarily
    cols.append('risk')  # Append risk column at the end
    df = df[cols]  # Reorder columns with risk at the end
    
'''
_____Functions Checking Dataset_____
'''

def Dataset_Information(df):
    
    def print_yellow_and_bold(text):
        print("\033[1m\033[93m" + text + "\033[0m")
    
    # Display the entire DataFrame
    display(df)
    
    # Display column names in yellow
    print_yellow_and_bold("Column names:")
    display(df.columns)

    # Display shape of the DataFrame in yellow
    print_yellow_and_bold("\nShape of the DataFrame:")
    display(df.shape)

    # Display info of the DataFrame in yellow
    print_yellow_and_bold("\nInfo of the DataFrame:")
    display(df.info())
    
    # Display data types of each column in yellow
    print_yellow_and_bold("\nData types of each column:")
    display(df.dtypes)

    # Check for null values in each column in yellow
    print_yellow_and_bold("\nCheck for null values in each column:")
    display(df.isna().any())

    # Checking for Null Values (Returns a DataFrame with True where values are null) in yellow
    print_yellow_and_bold("\nDataFrame with True where values are null:")
    display(df.isnull())

    # Count the number of null values in each column in yellow
    print_yellow_and_bold("\nCount of null values in each column:")
    display(df.isna().sum())


'''
_____Functions for Initial Exploration / Univariate Analysis_____
'''
def Initial_Exploration(df):
    
    def print_yellow_and_bold(text):
        print("\033[1m\033[93m" + text + "\033[0m")
    
    # Extracting column names with numerical data types
    print_yellow_and_bold("Column names with numerical data types:")
    display(", ".join(df.select_dtypes("number").columns.tolist()))
    
    # Check for null values in each column in yellow
    print_yellow_and_bold("\nCheck for null values in each column:")
    display(df.isna().any())

    # Checking for Null Values (Returns a DataFrame with True where values are null) in yellow
    print_yellow_and_bold("\nDataFrame with True where values are null:")
    display(df.isnull())

    # Count the number of null values in each column in yellow
    print_yellow_and_bold("\nCount of null values in each column:")
    display(df.isna().sum())    
    
    # Counting and sorting unique values for each numerical column in descending order
    print_yellow_and_bold("\nNumber of unique values for each numerical column (descending order):")
    display(df.select_dtypes("number").nunique().sort_values(ascending=False))
    
    # Display unique values for each column in yellow
    print_yellow_and_bold("\nUnique values for each column:")
    for col in df.columns:
        unique_values = df[col].unique()
        print_yellow_and_bold(f"\n{col}:")
        display(unique_values)
    
    # Extracting column names with object (string) data types
    print_yellow_and_bold("\nColumn names with object data types:")
    display(", ".join(df.select_dtypes("object").columns.tolist()))
    
    # Counting and sorting unique values for each object column in descending order
    print_yellow_and_bold("\nNumber of unique values for each object column (descending order):")
    display(df.select_dtypes("object").nunique().sort_values(ascending=False))
    
    # Extracting columns with object data types to create a categorical dataframe
    df_categorical = df.select_dtypes("object")
    df_numerical = df.select_dtypes("number")
    
    # Verify that the total number of columns matches the sum of object and numerical columns
    print_yellow_and_bold("\nVerification of total columns:")
    total_columns_correct = len(df.columns) == len(df_categorical.columns) + len(df_numerical.columns)
    print(f"Total columns match expectation: {total_columns_correct}")