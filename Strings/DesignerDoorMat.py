'''
Title     : Designer Door Mat
Subdomain : Strings
Domain    : Python
Author    : Ayush Garg
Created   : 01 October 2020
Problem   : https://www.hackerrank.com/challenges/designer-door-mat/problem
'''
n, m = map(int,input().split())
p = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(p + ['WELCOME'.center(m, '-')] + p[::-1]))
