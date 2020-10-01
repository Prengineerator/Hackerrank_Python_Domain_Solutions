'''
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
m=len(student_marks[query_name])
sum1=00.00
for i in range(0,m):
    sum1=student_marks[query_name][i]+sum1
print("{:.2f}".format(sum1/m));

