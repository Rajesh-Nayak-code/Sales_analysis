import numpy as np
class Sales():
    def __init__(self,sales):
        self.sales=sales
        self.arr=np.array(self.sales)
    def total_sales(self):
        return f"Total sales is : {np.sum(self.arr)}"
    def average_sales(self):
        return f"Average sales is : {np.mean(self.arr)}"
    def min_max_sales(self):
        return f"Minimum sales is : {np.min(self.arr)} and Maximum sales is : {np.max(self.arr)}"
    def sales_above_avg(self):
        return self.arr[self.arr>np.mean(self.arr)]
    def percent_contribution(self):
        return (self.arr/np.sum(self.arr))*100
    def Sort(self):
        return np.sort(self.arr)
obj=Sales([1200,1500,900,2000,1800,2200,1700])
