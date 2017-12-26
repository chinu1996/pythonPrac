# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())

# Think of column-wise concatenation of data as stitching data together from the sides instead of the top and bottom.
#  To perform this action, you use the same pd.concat() function, but this time with the keyword argument axis=1. The
#  default, axis=0, is for a row-wise concatenation.


# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())
