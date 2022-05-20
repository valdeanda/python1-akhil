File = open("TransactionList.txt", "r")
total = 0
TransactionList = File.readlines()
for transaction in TransactionList:
    total += int(transaction)
File.close()
File = open("TransactionOut.txt", "w")
File.write(str(total))
