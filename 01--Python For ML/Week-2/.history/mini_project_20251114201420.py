from abc import ABC, abstractmethod

# Abstraction
class BankService(ABC):
    @abstractmethod
    def transaction(self):
        pass



class Account :
    bank_name="islami Bank"

    def __init__(self,name,account_no,balance):
        self.name=name
        self.account_no= account_no
        self.__balance=balance # Private Attribute

    def get_balance(self):
        return self.__balance
    
    def deposite(self, money):
        self.__balance += money
        return f"{money} is added, New Balance is: {self.__balance}"

    def withdraw(self, withdrawMoney):

        if withdrawMoney > self.__balance:
            return f"Insufficient Balance"
        self.__balance -= withdrawMoney

        return f"{withdrawMoney} is Withdrawed, New Balance is: {self.__balance}"


class SavingAccount(Account):
    def __init__(self, name, account_no, balance, interest_rate):
        super().__init__(name, account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest_rate(self):
        interest = self.get_balance() * self.interest_rate / 100
        return f"Interest rate is : {interest}"

class CurrentAccount(Account):
    def __init__(self, name, account_no, balance, overlimit):
        super().__init__(name, account_no, balance)
        self.overlimit = overlimit

    def withdraw(self, withdrawMoney):
        if withdrawMoney > self.get_balance() + self.overlimit :
            return f"Insufficient Balance"

        balance = self.get_balance() - withdrawMoney

        return f"{withdrawMoney} is withdrawed , new balance is {balance}"


class ATM(BankService):
    def transaction(self):
        print("ATM Transaction: Cash Withdraw or Balance Check")



currentUser = CurrentAccount("Rakib", 123, 1000,5000)
# print(currentUser.get_balance())
# print(currentUser.withdraw(3000))

savingUSer = SavingAccount("Takib", 133, 100,2)
print(savingUSer.get_balance())
print(savingUSer.calculate_interest_rate())

atm = ATM()
atm.transaction(); 

