### Important decision points for the project : 

- To avoid data leakage, missing value imputation was performed after the train–test split. Imputation parameters were learned exclusively from the training data and then applied consistently to validation and test sets.

- The category “ISLAND” appeared only 5 times and showed significant overlap in price distribution with coastal categories. Since it represents an extreme minority and cannot form a stable pattern, and given its semantic proximity to ocean-adjacent regions, it was merged with “NEAR OCEAN”. This decision was validated through exploratory analysis and applied consistently across all data splits.

The function should not decide which columns are features — it should only act on what it’s given.