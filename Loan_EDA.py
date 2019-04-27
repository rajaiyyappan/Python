# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:51:49 2019

@author: ssn
"""
#Load libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt
import seaborn as ssn

#set working directory
os.chdir("D:/employee/Step 1")
#Import file
data = pd.read_csv('loan.csv')

#To rename values in column
loan['credit.policy']=loan['credit.policy'].replace(1,'met')
loan['credit.policy']=loan['credit.policy'].replace(0,'Not met')
loan['not.fully.paid']=loan['not.fully.paid'].replace(1,'Not paid')
loan['not.fully.paid']=loan['not.fully.paid'].replace(0,'paid')

#To rename column of dataframe
loan.rename(columns={'credit.policy':'credit_policy','int.rate':'int_rate','log.annual.income':'log_annual_income',
                     'days.with.cr.line':'days_with_cr_line',
                     'revol.bal':'revol_bal','revol.util':'revol_util',
                     'inq.last.6mths':'enqui_last_6mths','delinq.2yrs':'delinq_2yrs',
                     'pub.rec':'pub_rec','not_fully_paid':'Loan',
                     'Annual income':'annual_income'}, inplace=True)

#To find summary of all the variables

a=loan.describe()
b=loan.info()

#To drop column 
loan=loan.drop('log.annual.inc', axis=1)

#To find dimension of dataset
loan.shape

#To find data type
type(loan)

#To find column names
loan.columns

#To find first 10 rows
loan.head(10)

#To find last 10 rows 
loan.tail(10)

#Slicing the dataset
loan.iloc[0:5,0:5]
loan.iloc[:,[3,4,8]]

#To find unique values
loan['credit_policy'].unique()
loan['purpose'].unique()
loan['enqui_last_6mths'].unique()
loan['delinq_2yrs'].unique()
loan['pub_rec'].unique()


#To find length of unique values 
loan['credit_policy'].nunique()
loan['purpose'].nunique()
loan['delinq_2yrs'].nunique()
loan['pub_rec'].nunique()

#To find count of categories in variables
loan['credit_policy'].value_counts()
loan['purpose'].value_counts()
loan['enqui_last_6mths'].value_counts()
loan['delinq_2yrs'].value_counts()
loan['pub_rec'].value_counts()

#To find Mean
loan['dti'].mean()

#To find Median
loan['Annual_income'].meadian()

#To find variance
loan['Annual_income'].var()

#To find standard deviation
loan['revol_util'].std()

#To sort ascending
loan=loan.sort_values('annual_income',ascending=True)

#To sort descending
loan=loan.sort_values('annual_income',ascending=False)

#Write file to csv
loan.to_csv('loan_p.csv',index=None)

