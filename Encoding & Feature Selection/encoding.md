Nominal categorical variable:
Nominal categorical variables are those for which we do not have to worry about the arrangement of the categories.

Example,

i. suppose we have a gender column with categories as Male and Female.
ii. We can also have a state column in which we have different states like NY, FL, NV, TX
So here we don’t have to worry about the arrangement of the categories.

Ordinal Categorical variable :
Ordinal categories are those in which we have to worry about the rank. These categories can be rearranged based on ranks.

Example,

i. Suppose in a dataset there is an education column which we will use to predict the salary of the person. The education column has categories like ‘bachelors’,’masters’,’PHD’. Based on the above categories we can rearrange this and assign ranks to each category. Based on the education level ‘PHD’ will get the highest rank (PHD-1, masters-2, bachelors-3)

Which Encoder to Use?
Nominal Features: Use OneHotEncoder.
Ordinal Features: Use OrdinalEncoder.
Target Labels: Use LabelEncoder or TargetEncoder (external).
Mixed Types: Use ColumnTransformer to combine different encoders.
