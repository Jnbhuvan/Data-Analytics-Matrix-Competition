---------------------------------------------------------------------------------------------------------------------------------------------------------------

About this file

---> Nike Sales (Uncleaned) Dataset

> Context
This synthetic dataset simulates retail and online sales transactions from Nike, one of the world's leading sportswear and footwear brands. It is intentionally filled with messy, uncleaned records to replicate real-world business data—perfect for practicing data cleaning, exploratory data analysis (EDA), and building dashboards or portfolio projects.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

>What’s Inside

Over 6000+ transaction records containing:
    Multiple product lines (Running, Basketball, Lifestyle, Training, Soccer)
    Gender-specific sales (Men, Women, Kids)
    Sales from both Retail Stores and Online Channels

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Common data issues like:
    Null values

    Typos in regions

    Wrong data types

    Negative values in numeric columns

    Inconsistent date formats (e.g., 2023/07/21, 21-07-2023, etc.)

    Discounts > 100%

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Columns Description

Order_ID ----Transaction/order ID (some duplicate entries)
Gender_Category------- Buyer segment: Men, Women, or Kids
Product_Line------ Product type: Running, Basketball, etc.
Product_Name -------Specific product sold (e.g., Air Force 1, Pegasus Turbo)
Size -----Product size (e.g., 7, M, L – includes missing/inconsistent)
Units_Sold-------- Quantity sold (can be negative or null)
MRP---------- Maximum retail price (some are null or zero)
Discount_Applied------ Discount applied on sale (some are over 100%)
Revenue -------Final amount after discount (some miscalculated)
Order_Date --------Date of transaction (multiple formats & nulls)
Sales_Channel -----------Online or Retail
Region -------------Indian cities (includes typos like "Delhii", "Banglore")
Profit --------------Profit made (can be unrealistic or negative)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Note:

This dataset is 100% synthetic and generated for the competition. No actual Nike customer data is used.

---------------------------------------------------------------------------------------------------------------------------------------------------------------
