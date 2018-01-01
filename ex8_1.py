class BankAccount:
    def __init__ (self, name, number, balance):
        self.name=name
        self.number=number
        self.balance=balance
    def __str__ (self):
        if isinstance(self, BankAccount):
            accountType= 'bank account'
        if isinstance(self, InterestAccount):
            accountType= 'interest account'
        msg='Your name is '+self.name+'. You account type is '+accountType+'. your account number is '+str(self.number)+' and your balance is '+str(self.balance)+' shekels.'
        return (msg)
    def display_balance (self):
        print ('Your balance is '+str(self.balance)+', '+str(self.name)+'!')
    def deposit (self, sum_):
        self.balance+=sum_
    def withdraw (self, sum_):
        self.balance-=sum_
    def goal_ (self):
        goal=input ('Would you like to deposit, withraw or quit? Write "Deposit", "Withraw" or "Quit". ')
        if goal=='Deposit':
            deposit_=int(input ('How much money would you like to deposit? '))
            self.deposit (deposit_)
            self.display_balance ()
            self.goal_ ()
        elif goal=='Withraw':
            withdraw_=int(input ('How much money would you like to withdraw? '))
            self.withdraw (withdraw_)
            self.display_balance ()
            self.goal_ ()
        elif goal=='Quit':
            print ('Okay. We won\'t deposit or withraw.')
            self.display_balance ()
        else:
            print ('I don\'t understand what you are talking about. I\'ll ask the question again.')
            self.goal_    ()
class InterestAccount (BankAccount):
    def __init__ (self, name, number, balance, interest):
        BankAccount.__init__ (self, name, number, balance)
        self.interest=interest
    def addInterest (self):
        self.balance=(1+self.interest)*self.balance
    def goal_ (self):
        inter=input ('Would you like to pay interests? Write "Yes" or "Quit". ')
        if inter=='Yes':
            self.addInterest ()
            self.display_balance ()
            self.goal_a ()
        elif inter=='Quit':
            print ('Okay. You won\'t pay interests. You have a good economical mind!')
            InterestAccount.display_balance (self)
        else:
            print ('I don\'t understand what you are talking about. I\'ll ask the question again.')
            self.goal_ ()
    def goal_a (self):
        inter=input ('Would you like to pay interests again? Write "Yes" or "Quit". ')
        if inter=='Yes':
            self.addInterest ()
            self.display_balance ()
            self.goal_a ()
        elif inter=='Quit':
            print ('Okay. You won\'t pay interests again. You have a good economical mind!')
            InterestAccount.display_balance (self)
        else:
            print ('I don\'t understand what you are talking about. I\'ll ask the question again.')
            InterestAccount.goal_a ()
myBankAccount=BankAccount ('Yannai', 123456, 1295)
yourBankAccount=BankAccount ('Yonni', 345678, 123)
herBankAccount=InterestAccount ('Israela', 567890, 10, 0.05)
def allStar ():
    who=input ('Which account would you like to use? Write "Yannai", "Yonni" or "Israela". ')
    if who=='Yannai':
        print (myBankAccount)
        myBankAccount.goal_ ()
    elif who=='Yonni':
        print (yourBankAccount)
    elif who=='Israela':
        print (herBankAccount)
        herBankAccount.goal_ ()
    else:
       print ('I don\'t understand what are you talking about. I\'ll ask the question again.')
       allStar ()    
allStar ()
