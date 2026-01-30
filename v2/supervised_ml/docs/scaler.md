### ------------ Folder name : scalers --------------------

- here is all the information about the 'scalers' folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- in the folder we have 2 files : 

1. price_scaler : scaler that was trained on the price column only and later scaled the price column, after scaling it was saved and later recalled during the prediction part for the distance based models. i.e. called to rescale the data to make the comparison realistic with the tree based models

2. rest_scaler : trained and scaled the rest of the column excluding the target feature 'median_house_value', it was recalled only on the valid data to scale the numeric columns for distance based models.