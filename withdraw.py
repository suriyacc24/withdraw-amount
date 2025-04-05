cash=5000
while cash >0 :
    withdraw = int(input('how much withdraw?'))
    if cash >= withdraw:
        print('Transaction Successful')
        cash = cash - withdraw
    else:
        print('insufficient cash in machine')