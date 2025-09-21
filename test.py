import pandas as pd
import numpy as np

def dataset_purity(df):
    total_cells = df.shape[0] * df.shape[1]
    org_csv_size = 2500;
    actual_csv_size = df.size;
    print(f"Actual_csv_file_size:{actual_csv_size}")
    # 1. Missing values
    missing_count = df.isnull().sum().sum()
    missing_pct = (missing_count / total_cells) * 100

    # 2. Duplicate rows
    duplicate_count = df.duplicated().sum()
    duplicate_pct = (duplicate_count / len(df)) * 100 if len(df) > 0 else 0
    numeric_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(include='object').columns
    dtype_consistency = ((len(numeric_cols) + len(cat_cols)) / df.shape[1]) * 100 if df.shape[1] > 0 else 0

    # 4. Outlier detection (IQR method for numeric cols)
    outlier_count = 0
    total_numeric = 0
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outlier_count += ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
        total_numeric += len(df[col])
    outlier_pct = (outlier_count / total_numeric) * 100 if total_numeric > 0 else 0

    # Combine into purity score (weights adjustable)
    purity_score = 100 - (0.4*missing_pct + 0.3*duplicate_pct + 0.2*outlier_pct)

    # FIX: removed commas that made these tuples instead of numbers
    Missing = round(missing_pct, 2)
    Duplicate = round(duplicate_pct, 2)
    Outlier = round(outlier_pct, 2)
    Purity = max(0, round(purity_score, 2))

    Data_cleaning_score = int(0)
    if int(Missing) > 1.11:
        Data_cleaning_score -= 20
        print("Score for handling Missing Values = -20")
    elif Missing == 0:
        Data_cleaning_score += 20
        print("Score for handling Missing Values = 20")
    if Duplicate > 0:
        Data_cleaning_score -= 20
        print("Score for handling Duplicate Values = -20")
    else:
        Data_cleaning_score += 20
        print("Score for handling Duplicate Values = 20")

    if Outlier < 1.11 and Outlier > 0:
        Data_cleaning_score += 20
        print("Score for handling Outliers = 20")
    elif Outlier == 0:
        Data_cleaning_score += 50
        print("Score for handling Outliers Values = 50")
    elif Outlier == 1.11:
        Data_cleaning_score += 10 
        print("Score for handling Outliers Values = 10")
    else:
        Data_cleaning_score -= 40
        print("Score for handling Outliers Values = -40")

    if int(Purity) == 100:
        
        Data_cleaning_score += 60
        print("Score for handling Purity = 60")
        print('\n The Participant is qualified for the next round!')
    elif int(Purity) == 93.28:
        Data_cleaning_score += 10
        print("Score for handling Purity = 10")
    
    elif int(Purity) > 93.28 and int(Purity) < 100:
        Data_cleaning_score += 40
        print("Score for handling Purity = 40")
    
    else:
        Data_cleaning_score -= 20
        print("Score for handling Purity = -20")
    
    try:
        unique_count = df['Region'].nunique()
        # print(f"Unique values in column '{Region}': {unique_count}")
        if unique_count == 6:
            Data_cleaning_score += 30
            print("Score for handling Categorical Values = 30")
        else:
            Data_cleaning_score -= 30
            print("Score for not handling Categorical Values = -30")
    except Exception as e:
        Data_cleaning_score -= 50
        print("Score for removing Regions columns from the dataset = -50")
        
    percentage = 0

    if (df.size/325)>68:
        #Data_cleaning_score+=10
        pass
    
    elif (df.size/325)>=50 and (df.size/325)<=68:
        # Data_cleaning_score-=20
        percentage = 20

    elif (df.size/325)>30 and (df.size/325)<=49:
        #Data_cleaning_score-=30
        percentage = 30

    else:
        #Data_cleaning_score-=40
        percentage = 40

    # print(Data_cleaning_score)
    if(actual_csv_size>32500):
        Data_cleaning_score-=100
        print("Score for not removing redundancy = -100")
    else:
        print(f"Score for qualitative data loss ={Data_cleaning_score * (1 - percentage / 100)} ")
        Data_cleaning_score = Data_cleaning_score * (1 - percentage / 100)
    # print(Data_cleaning_score)
        
    return {
        "Missing %": round(missing_pct, 2),
        "Duplicate %": round(duplicate_pct, 2),
        "Outlier %": round(outlier_pct, 2),
        "Purity Score": max(0, round(purity_score, 2)),
        "Data_cleaning_score for 180 marks": int(Data_cleaning_score)
    }

# Example usage
df = pd.read_csv("Nike_Sales_Cleaned.csv")
result = dataset_purity(df)

# Open test.txt in append mode (creates the file if it doesn't exist)
with open('dummy.txt', 'a') as file:
    file.write('The participant is qualified for the next round.\n')

# print("Text added to test.txt!")


for key, value in result.items():
    print(f"{key}: {value}")
