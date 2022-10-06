# Example 1
# Convert all letters of the given string expression to uppercase.
# Put space instead of commas and periods, separate them word by word.

text = "The goal is to turn data into information, and information into insight."

text.replace(",", "").replace(".", "").upper().split()


# Example 2
# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def altering(string):
    after = ""
    for letter in range(len(string)):
        if letter % 2 == 0:
            after += string[letter].upper()
        else:
            after += string[letter].lower()
    return after


# Example 3
# Complete the following tasks for the given list.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Look at the number of elements of the given list.

len(lst)
# Step 2: Call the elements at index zero and ten.

lst[0]
lst[10]
# Step 3: Create a list ["D","A","T","A"] from the given list.

lst[0:4]
# Step 4: Delete the element in the eighth index.

lst.pop(8)
# Step 5: Add a new element.

lst.append("!")
# Step 6: Re-add element "N" to the eighth index.
lst.insert(8, "N")
lst

# Example 4
# Apply the following steps to the given dictionary structure.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
# Step 1: Access the key values.
dict.keys()
# Step 2: Access the values.
dict.values()
# Step 3: Update the value 12 of the Daisy key to 13.
dict.update({"Daisy": ["England", 13]})
# Second way
dict['Daisy'][1] = 13
# Step 4: Add a new value whose key value is Ahmet value [Turkey,24].
dict.update({"Ahmet": ["Turkey", 24]})
# Step 5: Delete Antonio from dictionary.
dict.pop("Antonio")
dict

# Example 5
# Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists,
# and returns these lists.

l = [2, 13, 18, 93, 22]


def func(number_list):
    even_list = []
    odd_list = []
    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return odd_list, even_list


# Example 6
# write divide_students function
# Add even index students to a list
# Add odd index students to another list
# Both lists must be returned as the same list.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(list):
    groups = [[], []]

    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(list[index])
        else:
            groups[1].append(list[index])
    print(groups)


divide_students(students)


# Without enumerate

def divider(list):
    evenoddgroup = [[], []]
    for student_index in range(len(students)):
        if student_index % 2 == 0:
            evenoddgroup[0].append(students[student_index])
        else:
            evenoddgroup[1].append(students[student_index])
    return evenoddgroup


odd_list, even_list = func(l)

# Example 7
# Using the List Comprehension structure,
# Capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
["NUM_" + col.upper() if col in num_cols else col.upper() for col in df.columns]

# Example 8
# Using the List Comprehension structure, select the names of the variables
# that are DIFFERENT from the variable names given below and create a new dataframe.
# Expected output
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols].head()

# Example 9
# Using the List Comprehension structure, write "FLAG" after the names of the variables
# that do not contain "number" in their names in the car_crashes data.

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# Example 10
#######################
# Goal is to create a dictionary with string key and value like given below.
# Only numerical variables must be changed.
#######################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

soz

# shortcut
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)
