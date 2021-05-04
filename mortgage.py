import pandas as pd
import numpy as np
import numpy_financial as npf
from datetime import date

class Mortgage:

    def __init__(self):
        return
  
    def menu(self):

        self.choice = input("""Please choose from the following options-
        A- Calculate Monthly Payment
        B- Calculate Monthly Interest
        C- Calculate Monthly Principle

        """)

        if self.choice == "A":
            self.estimatePayment()
        elif self.choice == "B":
            self.estimateInterest()
        elif self.choice == "C":
            self.estimatePrinciple()

    def getValues(self):

        self.principle = input("What is your principle loan amount? ")
        self.principle = int(self.principle)

        self.interest = input("What is your interest rate? (ex. 2.5) ")
        self.interest = float(self.interest)
        self.interest = self.interest/100

        self.term = input("What is the term of your loan (ex. 15 or 30)? ")
        self.term = int(self.term)

        self.numPayments = input("How many payments per year? ")
        self.numPayments = int(self.numPayments)
        
    def estimatePayment(self):
        self.getValues()
        monthlyTotal = npf.pmt(self.interest/self.numPayments, self.numPayments*self.term, self.principle)
        print('\n Estimated monthly payment is $%5.2f' %abs(monthlyTotal))

    def estimateInterest(self):
        self.getValues()
        monthlyInterest = npf.ipmt(self.interest/self.numPayments, 1, self.numPayments*self.term, self.principle)
        print('\n Estimated monthly interest payment is $%5.2f' %abs(monthlyInterest))

    def estimatePrinciple(self):
        self.getValues()
        monthlyPrinciple = npf.ppmt(self.interest/self.numPayments, 1, self.numPayments*self.term, self.principle)
        print('\n Estimated monthly principle payment is $%5.2f' %abs(monthlyPrinciple))

# TODO add amortization schedule 

new = Mortgage()
new.menu()



