### ------------ Folder name : Data --------------------

- here is all the information about the data folder, the way folder is structured and the stuff inside each one of them

- inside we have 3 more subfolders : 
1. raw
2. split_global
3. model_ready


### ************** subfolder : raw *********************

- it has the file 'housing.csv' which is complete raw data, with missing values, no split and transformations, basically in other words 'an entry point' for our project


### ************* subfolder : split_global ******************

- the files inside after the first pure split i.e. train and valid data, to avoid the leakage, from the valid, the target feature 'median_house_value' was dropped, to keep the pipeline clean, and the logic behind the earliest split is to make the model learn first and then use it to test the performance while acting like the data is raw and never seen before.

- all of the files are raw i.e. no processing, but only the split

- it has the following files : 

1. train.csv : the raw split file with the target feature : 'median_house_value'
2. valid.csv : split file, with no target feature and later to be used to act for the model as a fresh and unseen data
3. y_true_valid.csv : the true values(target feature's values) of the valid.csv features, this is just to act as a backup copy, not to be treated during the training phase of the models


### ************** subfolder : model_ready ********************

- it has the preprocessed data, with nan values handled, categorical columns encoded, graphs tested, transformation and scaling done (for the distance based models only).

- the files are : 

1. train_tree.csv
2. train_distance.csv
3. valid_tree.csv
4. valid_distance.csv