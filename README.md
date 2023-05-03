# Code-exercises

---
### 1. Exercise

---

There is a sequence of words in CamelCase as a string of letters, , having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given , determine the number of words in .

**Example**

**_Sample Input_:** 
> saveChangesInTheEditor

**_Sample Output_:** 
> 5
> 
**_Explanation_:** String  contains five words:

1. save
2. Changes
3. In
4. The
5. Editor
---

### 2. Exercise

---

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

**Input Format** \
The first line of input contains the original string. The next line contains the substring.

**Output Format**\
Output the integer number indicating the total number of occurrences of the substring in the original string.

**Example**

**Sample Input**
> ABCDCDC\
CDC

**Sample Output**
> 2

---
### 3. Exercise

---
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .
Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.\
In the second line, print True if  has any alphabetical characters. Otherwise, print False.\
In the third line, print True if  has any digits. Otherwise, print False.\
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.\
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

**Sample Input**
> qA2

**Sample Output**
> True\
> True\
> True\
> True\
> True

---
### 4. Exercise

---
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: 
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

__<u>Example</u>__ 

- s = '12:01:00PM' _Return_ '12:01:00'.
- s = '12:01:00AM' _Return_ '00:01:00'.

**Function Description**

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

- string s: a time in 12 hour format

**Returns**

- string: the time in 24 hour format

**Input Format**

A single string  that represents a time in -hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

**Constrains**
- All input times are valid

**Sample Input**
> 07:05:45PM
sd
**Sample Output**
> 19:05:45


---
### 5. Exercise

---
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

**Input Format**

- A single line of input containing the full name, S.

**Note**: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

**Output Format**
- Print the capitalized string, S.

**Sample Input** 
> hello world 

**Sample Output**
> Hello World

