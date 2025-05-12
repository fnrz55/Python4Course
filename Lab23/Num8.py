from functools import reduce
import pandas as pd
my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums1 = reduce(lambda x, y: x + 1, my_nums)
print(nums1)
Employee_data = {'employee_id':['1','2','3','4'],
                 'name':['Anny Johnn','Alex Johnn','Johnn Anny','Anny Alex']}
sales_data = {'employee_id':['3','4','5','6'],
                 'cost':[122,222,333,444]}
dataframe = pd.DataFrame

