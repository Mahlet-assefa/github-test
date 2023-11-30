class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        #min_salary = salary[0]
        #max_salary = salary[-1]
        avg_salary = sum(salary[1:-1])/(len(salary)-2)
        return avg_salary