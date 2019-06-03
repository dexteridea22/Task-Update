# Task-Update


:star: **Star me on GitHub — it helps!**

### Table of content
- [Analysis](#analysis)
- [Design Assumptions](#design-assumptions)
- [Technology](#tech)
- [Test driven development](#test-driven-dev)
- [Output File](#output-file)
- [Demo Screenshots](#Demo-Screenshots)
## Analysis
I carefully analysed for following solutions:
1. Using Ajax call
2. Web sockets

## Design Assumptions
For this solution since the updates are server side push events and updates are only for single column
I thought of choosing ajax calls , here I assumed the users(client) to be fewer.  
In case users increase and updates are also multiple from both server and client side(Publish Subscribe mechanism)
I think using web sockets is better in that case.

## Technology :
- Backend : Django,DRF
- Database : sqlite

## Test driven development:
- created test cases to test CRUD Operations
in DRF apis
- Tested from rest apis 

## Output file:
Log file to log json data after status is completed

## Demo Screenshots

![image](Images/Screenshot_2.png)

![image](Images/Screenshot_1.png)

![image](Images/Screenshot_3.png)

![image](Images/Screenshot_4.png)
