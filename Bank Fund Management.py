import os
a=open(r"D:\python project\pythonProject1\project_file.txt","w+")
class Reserve_Bank:
  def __init__(self):
        self.Rsrve_Tl_Acnt = 20
        self.Rsrve_Tl_Fnd = 1000
        self.Stg_Data_RS = {}
        self.Stg_Data_RS.update({"RS": {'ACC': self.Rsrve_Tl_Acnt, 'FND': self.Rsrve_Tl_Fnd}})
class State_Bank(Reserve_Bank):
    def __init__(self):
        self.Ste_Tl_Acnt = 10
        self.Ste_Tl_Fnd = 500
        self.Stg_Data_ST = {}
        super().__init__()
        self.Stg_Data_ST.update({"ST": {'ACC': self.Ste_Tl_Acnt, 'FND': self.Ste_Tl_Fnd}})

class Tamil_Nadu_Bank(State_Bank):
    def __init__(self):
        self.Tn_Tl_Acnt = 5
        self.Tn_Tl_Fnd = 250
        super().__init__()
        self.Stg_Data_TN = {}
        # self.Stg_Data_ST = {"ST": {self.Ste_Tl_Acnt: self.Ste_Tl_Fnd, self.Tn_Tl_Acnt: self.Ste_Tl_Fnd}}
        # self.Stg_Data_RS = {"RS": {self.Rsrve_Tl_Acnt: self.Rsrve_Tl_Fnd, self.Ste_Tl_Acnt: self.Ste_Tl_Fnd}}
        # self.Stg_Data_TN = {"TN": {self.Ste_Tl_Acnt: self.Ste_Tl_Fnd, self.Tn_Tl_Acnt: self.Tn_Tl_Fnd}}
        self.Stg_Data_TN = {"TN": {"ACC": self.Tn_Tl_Acnt, "FND": self.Tn_Tl_Fnd}}


class Cuddalore_Branch(Tamil_Nadu_Bank):
    def __init__(self):
        self.Cdlr_Br_AC = 2
        self.Cdlr_Br_FnD = 85
        self.AN = 1
        self.data = {}
        self.dataName = {}
        super().__init__()
        # self.Stg_Data_RS = {"RS": {'ACC': self.Rsrve_Tl_Fnd, 'FND': self.Rsrve_Tl_Fnd}}
        # self.Stg_Data_ST = {"ST": {'ACC': self.Ste_Tl_Fnd, 'FND': self.Ste_Tl_Fnd}}
        # self.Stg_Data_TN = {"TN": {'ACC': self.Ste_Tl_Fnd, 'FND': self.Tn_Tl_Fnd}}
        # self.data = {"TN_Cdlr": {'ACC': self.Cdlr_Br_AC, 'FND': self.Cdlr_Br_FnD}}
        self.data = {"TN_Cdlr": {'ACC': self.Cdlr_Br_AC, 'FND': self.Cdlr_Br_FnD}}


    def Storage(self):
        print(self.Cdlr_Br_AC)
        print(self.Tn_Tl_Acnt)

        self.Tn_Tl_Acnt += self.Cdlr_Br_AC
        self.Ste_Tl_Acnt += self.Cdlr_Br_AC
        self.Rsrve_Tl_Acnt += self.Cdlr_Br_AC

        self.Tn_Tl_Fnd += self.Cdlr_Br_FnD
        self.Ste_Tl_Fnd += self.Cdlr_Br_FnD
        self.Rsrve_Tl_Fnd += self.Cdlr_Br_FnD

        self.Stg_Data_RS.update({"RS": {'ACC': self.Rsrve_Tl_Acnt, 'FND': self.Rsrve_Tl_Fnd}})
        self.Stg_Data_ST.update({"ST": {'ACC': self.Ste_Tl_Acnt, 'FND': self.Ste_Tl_Fnd}})
        self.Stg_Data_TN .update({"TN": {'ACC': self.Tn_Tl_Acnt, 'FND': self.Tn_Tl_Fnd}})
        self.data.update({"TN_Cdlr": {'ACC': self.Cdlr_Br_AC, 'FND': self.Cdlr_Br_FnD}})

        a.write(str(self.Tn_Tl_Acnt)+'\n')
        a.write(str(self.Tn_Tl_Fnd)+'\n')
        a.write(str(self.Ste_Tl_Acnt)+'\n')
        a.write(str(self.Ste_Tl_Fnd)+'\n')
        a.write(str(self.Rsrve_Tl_Acnt)+'\n')
        a.write(str(self.Rsrve_Tl_Fnd)+'\n')

        print(self.Stg_Data_RS.items())
        print(self.Stg_Data_ST.items())
        print(self.Stg_Data_TN.items())
        print(self.data.items())

        print("----------ENF OF THE BANK WORKING DAY-----------")
        print("ACCOUNTS: "+"\n")
        print("     Cuddalore Branch Accounts :", self.Cdlr_Br_AC)
        print("     Tamil Nadu Accounts :", self.Tn_Tl_Acnt)
        print("     State Bank Accounts :", self.Ste_Tl_Acnt)
        print("     Reserve Bank Accounts :", self.Rsrve_Tl_Acnt)
        print("     FUND: "+"\n")
        print("     Cuddalore Branch Fund :", self. Cdlr_Br_FnD)
        print("     Tamil Nadu Fund: ", self.Tn_Tl_Fnd)
        print("     State Bank Fund: ", self.Ste_Tl_Fnd)
        print("     Reserve Bank: ", self.Rsrve_Tl_Fnd)
        print("-----------------------------------------------------------")
    def AC_Opn_Cdlr(self, NAME):

        print("ACCOUNT NUMBERS IS: ", self.AN, ",NAME is : ", NAME)
        self.data[self.AN] = 0
        self.dataName[self.AN] = NAME
        self.AN += 1
        self.Cdlr_Br_AC += 1
        # self.data["TN_Cdlr"]['ACC'] += 1
        print(self.Cdlr_Br_AC)

        print("-----------------------------------------------------------")
    def AC_Cls_Cdlr(self, AN):

        try:
            print("Wait a few Seconds...")
            self.data[AN]

        except KeyError:
            print("Your Account already Closed...")
            print("-----------------------------------------------------------")
        else:
            self.data.pop(AN)
            print(AN, "ACCOUNT WAS CLOSE...THANK YOU!!!")
            self.Cdlr_Br_AC -= 1

            print("-----------------------------------------------------------")

    def DP_Cdlr(self, AN, MONEY):

        try:
            print("Wait a few Seconds...")
            self.data[AN]

        except KeyError:
            print("Please...Check your Account Number")
            print(AN)
            print("-----------------------------------------------------------")
        else:
            print("Thank you for waiting...")
            print("Amount of deposit: ", MONEY)
            self.data[AN] += MONEY
            print("After Total Amount of deposit: ", self.data[AN])
            self.Cdlr_Br_FnD += MONEY
            print("-----------------------------------------------------------")

    def WD_Cdlr(self, AN, MONEY):
        try:
            self.data[AN]
            print("Wait a few Seconds...")

        except KeyError:
            print(self.data[AN], "Please...Check your Account number ...")
            print(self.data[AN])
            print("-----------------------------------------------------------")

        else:

            if self.data[AN] > MONEY:
                print("Thank you for waiting...")
                print("Amount of Withdraw: ", MONEY)
                self.data[AN] -= MONEY
                print("Total Amount After Withdraw", self.data[AN])
                self.Cdlr_Br_FnD -= MONEY

            else:
                print("BALANCE:", self.data[AN], "...your Account Balance is Low....")
                print("-----------------------------------------------------------")
    def Bl_Cdlr(self, AN):

        try:
            print("Wait a few Seconds...")
            self.dataName[AN]

        except KeyError:
            print("Please...Check your ACCOUNT NUMBER: ", AN)
            print("-----------------------------------------------------------")
        else:
            print("Thank you for waiting...")
            print("NAME: ", self.dataName[AN])
            print("ACCOUNT NUMBER: ", AN)
            print("BALANCE AMOUNT: ", self.data[AN])
            print("-----------------------------------------------------------")
a1=open(r"D:\python project\pythonProject1\project_file.txt","w+")
class Trichy_Branch(Tamil_Nadu_Bank):
    def __init__(self):
        self.Tri_Br_AC = 2
        self.Tri_Br_FnD = 85
        self.AN = 1
        self.data = {}
        self.dataName = {}
        super().__init__()
        self.data = {"TN_Tri": {'ACC': self.Tri_Br_AC, 'FND': self.Tri_Br_FnD}}

    def Storage(self):
        print(self.Tri_Br_AC)
        print(self.Tn_Tl_Acnt)

        self.Tn_Tl_Acnt += self.Tri_Br_AC
        self.Ste_Tl_Acnt += self.Tri_Br_AC
        self.Rsrve_Tl_Acnt += self.Tri_Br_AC

        self.Tn_Tl_Fnd += self.Tri_Br_FnD
        self.Ste_Tl_Fnd += self.Tri_Br_FnD
        self.Rsrve_Tl_Fnd += self.Tri_Br_FnD

        self.Stg_Data_RS.update({"RS": {'ACC': self.Rsrve_Tl_Acnt, 'FND': self.Rsrve_Tl_Fnd}})
        self.Stg_Data_ST.update({"ST": {'ACC': self.Ste_Tl_Acnt, 'FND': self.Ste_Tl_Fnd}})
        self.Stg_Data_TN.update({"TN": {'ACC': self.Tn_Tl_Acnt, 'FND': self.Tn_Tl_Fnd}})
        self.data.update({"TN_Tri": {'ACC': self.Tri_Br_AC, 'FND': self.Tri_Br_FnD}})

        a1.write(str(self.Tn_Tl_Acnt) + '\n')
        a1.write(str(self.Tn_Tl_Fnd) + '\n')
        a1.write(str(self.Ste_Tl_Acnt)+'\n')
        a1.write(str(self.Ste_Tl_Fnd)+'\n')
        a1.write(str(self.Rsrve_Tl_Acnt)+'\n')
        a1.write(str(self.Rsrve_Tl_Fnd)+'\n')

        print(self.Stg_Data_RS.items())
        print(self.Stg_Data_ST.items())
        print(self.Stg_Data_TN.items())
        print(self.data.items())

        print("----------ENF OF THE BANK WORKING DAY-----------")
        print("ACCOUNTS: " + "\n")
        print("     Trichy Branch Accounts :", self.Tri_Br_AC)
        print("     Tamil Nadu Accounts :", self.Tn_Tl_Acnt)
        print("     State Bank Accounts :", self.Ste_Tl_Acnt)
        print("     Reserve Bank Accounts :", self.Rsrve_Tl_Acnt)
        print("     FUND: "+"\n")
        print("     Trichy Branch Fund :", self.Tri_Br_FnD)
        print("     Tamil Nadu Fund: ", self.Tn_Tl_Fnd)
        print("     State Bank Fund: ", self.Ste_Tl_Fnd)
        print("     Reserve Bank: ", self.Rsrve_Tl_Fnd)

        print("-----------------------------------------------------------")
    def AC_Opn_Tri(self, NAME):
        print("ACCOUNT NUMBERS IS: ", self.AN, ",NAME is : ", NAME)
        self.data[self.AN] = 0
        self.dataName[self.AN] = NAME
        self.AN += 1
        self.Tri_Br_AC += 1
        print(self.Tri_Br_AC)
        print("-----------------------------------------------------------")

    def AC_Cls_Tri(self,AN):

        try:
            print("Wait a few Seconds...")
            self.data[AN]

        except KeyError:
            print("Your Account already Closed...")
            print("-----------------------------------------------------------")
        else:
            self.data.pop(AN)
            print(AN, "ACCOUNT WAS CLOSE...THANK YOU!!!")
            self.Tri_Br_AC -= 1
            print("-----------------------------------------------------------")

    def DP_Tri(self,AN, MONEY):
        try:
            print("Wait a few Seconds...")
            self.data[AN]
        except KeyError:
            print("Please...Check your Account Number")
            print(AN)
            print("-----------------------------------------------------------")
        else:
            print("Thank you for waiting...")
            print("Amount of deposit: ", MONEY)
            self.data[AN] += MONEY
            print("After Total Amount of deposit: ", self.data[AN])
            self.Tri_Br_FnD += MONEY
            print("-----------------------------------------------------------")

    def WD_Tri(self,AN,MONEY):
        try:
            self.data[AN]
            print("Wait a few Seconds...")
        except KeyError:
            print(self.data[AN], "Please...Check your Account number ...")
            print(self.data[AN])
            print("-----------------------------------------------------------")
        else:
            if self.data[AN] > MONEY:
                print("Thank you for waiting...")
                print("Amount of Withdraw: ", MONEY)
                self.data[AN] -= MONEY
                print("Total Amount After Withdraw", self.data[AN])
                self.Tri_Br_FnD -= MONEY
            else:
                print("BALANCE:", self.data[AN], "...your Account Balance is Low....")
                print("-----------------------------------------------------------")

    def Bl_Tri(self,AN):
        try:
            print("Wait a few Seconds...")
            self.dataName[AN]
        except KeyError:
            print("Please...Check your ACCOUNT NUMBER: ", AN)
            print("-----------------------------------------------------------")
        else:
            print("Thank you for waiting...")
            print("NAME: ", self.dataName[AN])
            print("ACCOUNT NUMBER: ", AN)
            print("BALANCE AMOUNT: ", self.data[AN])
            print("-----------------------------------------------------------")
a2=open(r"D:\python project\pythonProject1\project_file.txt","w+")
class Chennai_Branch(Tamil_Nadu_Bank):
    def __init__(self):
        self.Chn_Br_AC = 1
        self.Chn_Br_FnD = 80
        self.AN = 1
        self.data = {}
        self.dataName = {}
        super().__init__()
        self.data = {"TN_Chn": {"ACC": self.Chn_Br_AC, "FND": self.Chn_Br_FnD}}
    def Storage(self):

        print(self.Chn_Br_AC)
        print(self.Tn_Tl_Acnt)

        self.Tn_Tl_Acnt += self.Chn_Br_AC
        self.Ste_Tl_Acnt += self.Chn_Br_AC
        self.Rsrve_Tl_Acnt += self.Chn_Br_AC

        self.Tn_Tl_Fnd += self.Chn_Br_FnD
        self.Ste_Tl_Fnd += self.Chn_Br_FnD
        self.Rsrve_Tl_Fnd += self.Chn_Br_FnD

        self.Stg_Data_RS.update({"RS": {'ACC': self.Rsrve_Tl_Acnt, 'FND': self.Rsrve_Tl_Fnd}})
        self.Stg_Data_ST.update({"ST": {'ACC': self.Ste_Tl_Acnt, 'FND': self.Ste_Tl_Fnd}})
        self.Stg_Data_TN.update({"TN": {'ACC': self.Tn_Tl_Acnt, 'FND': self.Tn_Tl_Fnd}})
        self.data.update({"TN_Chn": {'ACC': self.Chn_Br_AC, 'FND': self.Chn_Br_FnD}})

        a2.write(str(self.Tn_Tl_Acnt) + '\n')
        a2.write(str(self.Tn_Tl_Fnd) + '\n')
        a2.write(str(self.Ste_Tl_Acnt) + '\n')
        a2.write(str(self.Ste_Tl_Fnd) + '\n')
        a2.write(str(self.Rsrve_Tl_Acnt) + '\n')
        a2.write(str(self.Rsrve_Tl_Fnd) + '\n')

        print(self.Stg_Data_RS.items())
        print(self.Stg_Data_ST.items())
        print(self.Stg_Data_TN.items())
        print(self.data.items())
        print("----------ENF OF THE BANK WORKING DAY-----------")
        print("ACCOUNTS: " + "\n")
        print("     Chennai Branch Accounts :", self.Chn_Br_AC)
        print("     Tamil Nadu Accounts :", self. Tn_Tl_Acnt)
        print("     State Bank Accounts :", self. Ste_Tl_Acnt)
        print("     Reserve Bank Accounts :", self. Rsrve_Tl_Acnt)
        print("FUND: " + "\n")
        print("     Chennai Branch Fund :", self. Chn_Br_FnD)
        print("     Tamil Nadu Fund: ", self.Tn_Tl_Fnd)
        print("     State Bank Fund: ", self.Ste_Tl_Fnd)
        print("     Reserve Bank: ", self.Rsrve_Tl_Fnd)

        print("-----------------------------------------------------------")
    def AC_Opn_Chn(self,NAME):
        print("ACCOUNT NUMBERS IS: ", self.AN, ",NAME is : ", NAME)
        self.data[self.AN] = 0
        self.dataName[self.AN] = NAME
        self.AN += 1
        self.Chn_Br_AC += 1
        print("-----------------------------------------------------------")

    def AC_Cls_Chn(self,AN):

        try:
            print("Wait a few Seconds...")
            self.data[AN]

        except KeyError:
            print("Your Account already Closed...")
            print("-----------------------------------------------------------")
        else:
            self.data.pop(AN)
            print(AN, "ACCOUNT WAS CLOSE...THANK YOU!!!")
            self.Chn_Br_AC -= 1
            print("-----------------------------------------------------------")

    def DP_Chn(self,AN, MONEY):

        try:
            print("Wait a few Seconds...")
            self.data[AN]

        except KeyError:
            print("Please...Check your Account Number")
            print(AN)
            print("-----------------------------------------------------------")
        else:
            print("Thank you for waiting...")
            print("Amount of deposit: ", MONEY)
            self.data[AN] += MONEY
            print("After Total Amount of deposit: ", self.data[AN])
            self.Chn_Br_FnD += MONEY
            print("-----------------------------------------------------------")
    def WD_Chn(self,AN,MONEY):
        try:
            self.data[AN]
            print("Wait a few Seconds...")

        except KeyError:
            print(self.data[AN], "Please...Check your Account number ...")
            print(self.data[AN])
            print("-----------------------------------------------------------")

        else:

            if self.data[AN] > MONEY:
                print("Thank you for waiting...")
                print("Amount of Withdraw: ", MONEY)
                self.data[AN] -= MONEY
                print("Total Amount After Withdraw", self.data[AN])
                self.Chn_Br_FnD -= MONEY
            else:
                print("BALANCE:", self.data[AN], "...your Account Balance is Low....")
                print("-----------------------------------------------------------")

    def Bl_Chn(self, AN):
        try:
            print("Wait a few Seconds...")
            self. dataName[AN]

        except KeyError:
            print("Please...Check your ACCOUNT NUMBER: ", AN)
            print("-----------------------------------------------------------")
        else:
            print("Thank you for waiting...")
            print("NAME: ", self.dataName[AN])
            print("ACCOUNT NUMBER: ", AN)
            print("BALANCE AMOUNT: ", self.data[AN])
            print("-----------------------------------------------------------")

#CUDDALORE

print("CUDDALORE:---------")
result_Cdlr=Cuddalore_Branch()
result_Cdlr.AC_Opn_Cdlr((input("NAME for account open:")))                          # Account Open
result_Cdlr.AC_Opn_Cdlr((input("NAME for account open:")))


result_Cdlr.DP_Cdlr(int(input("Account Number for deposit: ")),int(input("Money:")))      # Deposit
result_Cdlr.DP_Cdlr(int(input("Account Number for deposit: ")),int(input("Money:")))

result_Cdlr.WD_Cdlr(int(input("Account Number for withdraw: ")),int(input("Money:")))       # Withdraw

# result.AC_Cls_Cdlr(int(input("Account Number for close: ")))                      # Account Close

result_Cdlr.Bl_Cdlr(int(input("Account Number for balance: ")))

# TO VIEW TOTAL ACCOUNTS AND FUND FROM ALL BANK

result_Cdlr.Storage()
a.close()


# trichy
b=open(r"D:\python project\pythonProject1\project_file.txt","r+")
# b = open(r"C:\Users\Danger Vishva\Desktop\demo.txt","r+")
read_Tri = b.readlines()
result_tri = Trichy_Branch()
#read_Tri = read_Tri[0].split(',')
result_tri.Tn_Tl_Acnt = int(read_Tri[0].replace("\n", ""))
result_tri.Tn_Tl_Fnd = int(read_Tri[1].replace("\n", ""))
result_tri.Ste_Tl_Acnt = int(read_Tri[2].replace("\n", ""))
result_tri.Ste_Tl_Fnd = int(read_Tri[3].replace("\n", ""))
result_tri.Rsrve_Tl_Acnt = int(read_Tri[4].replace("\n", ""))
result_tri.Rsrve_Tl_Fnd = int(read_Tri[5].replace("\n", ""))


print(read_Tri)
print("TRICHY:--------")
result_tri.AC_Opn_Tri((input("NAME for account open:")))
result_tri.AC_Opn_Tri((input("NAME for account open:")))                            #Account Open
result_tri.AC_Opn_Tri((input("NAME for account open:")))

result_tri.DP_Tri(int(input("Account Number for deposit: ")),int(input("Money:")))      # Deposit
result_tri.DP_Tri(int(input("Account Number for deposit: ")),int(input("Money:")))

result_tri.WD_Tri(int(input("Account Number for withdraw: ")),int(input("Money:")))       # Withdraw

result_tri.AC_Cls_Tri(int(input("Account Number for close: ")))                      # Account Close

result_tri.Bl_Tri(int(input("Account Number for balance: ")))

#TO VIEW TOTAL ACCOUNTS AND FUND FROM ALL BANK

result_tri.Storage()
a1.close()
b.close()

# #chennai
b1=open(r"D:\python project\pythonProject1\project_file.txt","r+")
# # b = open(r"C:\Users\Danger Vishva\Desktop\demo.txt","r+")
read_Chn = b1.readlines()

print("CHENNAI:----------")
result_Chn = Chennai_Branch()

result_Chn.Tn_Tl_Acnt = int(read_Chn[0].replace("\n", ""))
result_Chn.Tn_Tl_Fnd = int(read_Chn[1].replace("\n", ""))
result_Chn.Ste_Tl_Acnt = int(read_Chn[2].replace("\n", ""))
result_Chn.Ste_Tl_Fnd = int(read_Chn[3].replace("\n", ""))
result_Chn.Rsrve_Tl_Acnt = int(read_Chn[4].replace("\n", ""))
result_Chn.Rsrve_Tl_Fnd = int(read_Chn[5].replace("\n", ""))

result_Chn.AC_Opn_Chn((input("NAME for account open:")))
result_Chn.AC_Opn_Chn((input("NAME for account open:")))                            #Account Open
result_Chn.AC_Opn_Chn((input("NAME for account open:")))

result_Chn.DP_Chn(int(input("Account Number for deposit: ")),int(input("Money:")))      # Deposit
result_Chn.DP_Chn(int(input("Account Number for deposit: ")),int(input("Money:")))

result_Chn.WD_Chn(int(input("Account Number for withdraw: ")),int(input("Money:")))       # Withdraw

result_Chn.AC_Cls_Chn(int(input("Account Number for close: ")))                      # Account Close

result_Chn.Bl_Chn(int(input("Account Number for balance: ")))

#TO VIEW TOTAL ACCOUNTS AND FUND FROM ALL BANK

result_Chn.Storage()
a2.close()
b1.close()

