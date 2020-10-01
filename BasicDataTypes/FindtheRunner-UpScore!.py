'''
Title     : Find the Second Largest Number
Subdomain : Data Types
Domain    : Python
Author    : Ayush Garg
Created   : 01 October 2020
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int, input().split()))

max1=-100
max2=-100
for i in range(n):
    if arr[i]>max1:
        max2=max1
        max1=arr[i]
    elif(max2<arr[i]<max1):
        max2=arr[i]

print(max2)
