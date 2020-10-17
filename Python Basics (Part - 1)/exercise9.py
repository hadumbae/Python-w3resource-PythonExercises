# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).

# exam_st_date = (11, 12, 2014)
# Sample Output: The examination will start from: 11 / 12 / 2014

examDate = (11, 12, 2014)

# Method 1
print(
    f'The exam will start form : {examDate[0]} / {examDate[1]} / {examDate[2]}')

# Method 2
print('The exam will start form : %i / %i / %i' % examDate)
