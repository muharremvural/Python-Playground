#Example 1
#Define the Titanic dataset from the Seaborn library.

import seaborn as sns
df = sns.load_dataset("titanic")

#Example 2
#Find the number of male and female passengers in the Titanic dataset.

df["sex"].value_counts()

#Example 3
#Find the number of unique values for each column.

df.nunique()

#Example 4
#Find the number of unique values of the variable pclass

df.loc[:, "pclass"].nunique()
df["pclass"].nunique()

#Example 5
#Find the number of unique values of pclass and parch variables

df.loc[:, ("pclass", "parch")].nunique()

#Example 6
#Check the type of the embarked variable. Change its type to category and check again.

df["embarked"].dtype

df["embarked"] = (df["embarked"].astype("category"))
df["embarked"].dtype

#Example 7
#Show all information of those with embarked value C

df[df["embarked"]== "C"].head()

#Example 8
#Show all information for those with embarked value not S

df[df["embarked"] != "S"].head()

#OR

df[~(df["embarked"] == "S")].head()

#Example 9
#Show all information for passengers younger than 30 years old and female.

df[(df["sex"] == "female") & (df["age"] < 30)].head()

#Example 10
#Show information for passengers whose Fare is over 500 or age is older than 70.

df[(df["fare"] > 500) | (df["age"] > 70)].head()

#Example 11
#Find the sum of the null values in each variable.

df.isnull().sum()

#Example 12
#Remove the who variable from the dataframe.

df.drop("who", axis=1, inplace=True)
#OR

df = df.drop("who", axis=1)

#Example 13
#Fill in the empty values in the deck variable with the most repeated value (mode) of the deck variable.

df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().any()

#Example 14
#Fill in the blank values in the age variable with the median of the age variable

df["age"].median()
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().any()

#Example 15
#Find the sum, count, mean values of the pclass and gender variables of the survived variable.

df.groupby(["pclass", "sex"]).agg({"survived": ["mean","sum","count"]})

#Example 16
#Write a function that will return 1 for those under 30, 0 for those equal to or above 30. titanic data using the function you wrote
#Using the function you wrote, create a variable named age_flag in the titanic data set. (use apply and lambda constructs)

def age_check(age):
    if age<30:
        return 1
    if age>=30:
        return 0

df["age_flag"] = df["age"].apply(lambda x: age_check(x))

#Example 17
#Define the Tips dataset from the Seaborn library.

import seaborn as sns
df_tip = sns.load_dataset("tips")

#Example 18
#Find the sum, min, max and mean values of the total_bill value according to the categories (Dinner, Lunch) of the time variable

df_tip.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

#Example 19
#Find the sum, min, max and mean values of the total_bill values according to day and time.

df_tip.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

#Example 20
#Find the sum, min, max and mean values of the total_bill and type values of the lunch time and female customers according to the day.

df_tip[(df_tip["sex"] == "Female") & (df_tip["time"] == "Lunch")].groupby("day").agg({"total_bill" : ["sum", "min", "max", "mean"],
                                                                                      "tip": ["sum", "min", "max", "mean"]})

#Example 21
#What is the average of orders with size less than 3 and total_bill greater than 10? (use loc)


df_tip.loc[(df_tip["size"]<3) & (df_tip["total_bill"]> 10), ("size", "total_bill")].mean()

#Example 22
#Create a new variable called total_bill_tip_sum. Define it to give the sum of the total bill and tip paid by each customer.

df_tip["total_bill_tip_sum"] = df_tip["total_bill"] + df_tip["tip"]

#Example 23
#Find the mean of the total_bill variable separately for men and women
#Create a new total_bill_flag variable where;
#Those below average are 0 and those equal or above the average are 1

m_avg = df_tip[df_tip["sex"] == "Female"]["total_bill"].mean()
f_avg = df_tip[df_tip["sex"] == "Male"]["total_bill"].mean()

def age_checker(bill, sex):
    if sex == "Female":
        if bill < f_avg:
            return 0
        if bill >= f_avg:
            return 1
    elif sex == "Male":
        if bill < m_avg:
            return 0
        if bill >= m_avg:
            return 1

df_tip["total_bill_flag"] = df_tip[["total_bill", "sex"]].apply(lambda x: age_checker(x["total_bill"], x["sex"]), axis=1)

#Example 24
#Using the total_bill_flag variable, observe the number of below and above average by gender.

df_tip.groupby("sex")["total_bill_flag"].head()

#Example 25
#Sort the data from largest to smallest according to the total_bill_tip_sum variable and assign the first 30 people to a new dataframe.

new_df_tip = df_tip.sort_values("total_bill_tip_sum", ascending=False)[:30]
