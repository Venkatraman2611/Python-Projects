import pickle
import os
import pathlib
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

class Account:
    accNo = 0
    name = ''
    deposit = 0
    acc_type = ''

    def createAccount(self):
        account_numbers = []
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            mylist = pickle.load(infile)
            account_numbers = [item.accNo for item in mylist]
            infile.close()

        while True:
            accNo = simpledialog.askinteger("Account", "Enter the account number:")
            if accNo in account_numbers:
                messagebox.showinfo("Account number already exists", "Please enter a different account number.")
            else:
                break

        
        self.accNo = accNo
        self.name = simpledialog.askstring("Account", "Enter the account holder's name:")
        self.acc_type = simpledialog.askstring("Account", "Enter the type of account [C/S]:")
        self.deposit = simpledialog.askinteger("Account", "Enter the initial amount:")
        messagebox.showinfo("Account Created", f"Account for {self.name} created.")

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        if amount > self.deposit:
            messagebox.showerror("Error", "Insufficient funds.")
        else:
            self.deposit -= amount

    def getDetails(self):
        return f"Account Number: {self.accNo}\nAccount Holder: {self.name}\nAccount Type: {self.acc_type}\nBalance: {self.deposit}"


def save_account(account):
    file_path = pathlib.Path("accounts.data")
    if file_path.exists():
        with open("accounts.data", "rb") as infile:
            accounts = pickle.load(infile)
    else:
        accounts = []

    accounts.append(account)

    with open("accounts.data", "wb") as outfile:
        pickle.dump(accounts, outfile)


def load_accounts():
    file_path = pathlib.Path("accounts.data")
    if file_path.exists():
        with open("accounts.data", "rb") as infile:
            accounts = pickle.load(infile)
            return accounts
    else:
        return []


def create_account():
    new_account = Account()
    new_account.createAccount()
    save_account(new_account)


def deposit_to_account():
    accNo = simpledialog.askinteger("Deposit", "Enter the account number:")
    accounts = load_accounts()

    for account in accounts:
        if account.accNo == accNo:
            amount = simpledialog.askinteger("Deposit", "Enter the amount to deposit:")
            account.depositAmount(amount)
            save_all_accounts(accounts)
            messagebox.showinfo("Success", "Deposit successful.")
            return

    messagebox.showerror("Error", "Account not found.")


def withdraw_from_account():
    accNo = simpledialog.askinteger("Withdraw", "Enter the account number:")
    accounts = load_accounts()

    for account in accounts:
        if account.accNo == accNo:
            amount = simpledialog.askinteger("Withdraw", "Enter the amount to withdraw:")
            account.withdrawAmount(amount)
            save_all_accounts(accounts)
            messagebox.showinfo("Success", "Withdrawal successful.")
            return

    messagebox.showerror("Error", "Account not found.")


def display_account():
    accNo = simpledialog.askinteger("Display", "Enter the account number:")
    accounts = load_accounts()

    for account in accounts:
        if account.accNo == accNo:
            messagebox.showinfo("Account Details", account.getDetails())
            return

    messagebox.showerror("Error", "Account not found.")


def save_all_accounts(accounts):
    with open("accounts.data", "wb") as outfile:
        pickle.dump(accounts, outfile)


def list_all_accounts():
    accounts = load_accounts()

    details = "\n".join(
        [f"{acc.accNo}: {acc.name}, {acc.acc_type}, Balance: {acc.deposit}" for acc in accounts]
    )

    if details:
        messagebox.showinfo("All Accounts", details)
    else:
        messagebox.showerror("Error", "No accounts found.")


def delete_account():
    accNo = simpledialog.askinteger("Delete", "Enter the account number:")
    accounts = load_accounts()

    accounts = [acc for acc in accounts if acc.accNo != accNo]

    save_all_accounts(accounts)

    messagebox.showinfo("Success", "Account deleted.")


# Main application
root = tk.Tk()
root.title("Bank Management System")
root.geometry("300x300")

menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="Create Account", command=create_account)
file_menu.add_command(label="Deposit", command=deposit_to_account)
file_menu.add_command(label="Withdraw", command=withdraw_from_account)
file_menu.add_command(label="Display Account", command=display_account)
file_menu.add_command(label="List All Accounts", command=list_all_accounts)
file_menu.add_command(label="Delete Account", command=delete_account)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
