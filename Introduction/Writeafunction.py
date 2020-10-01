'''
Title     : Write a function
Subdomain : Introduction
Domain    : Python
Author    : Ayush Garg
Created   : 01 October 2020
Problem   : https://www.hackerrank.com/challenges/write-a-function/problem
'''
def is_leap(year):
    leap = False
    if(year%4==0 and year%100!=0 or year%400==0):
        leap = True
    return leap
