
def sum(value1,value2):
    return value1 +value2

print(sum(2,3))

print('______________Default Arguments -----------------------')

def greet(name, age = 30):
    print('Hello ' +name+ ',I am '+str(age))

greet('Maxy')



print('______________blockchain -----------------------')

blockchain = [[1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_coins_blockchain(transactionAmount):
    blockchain.append([get_last_blockchain_value(),transactionAmount])
    print(blockchain)

add_coins_blockchain(3.2)
add_coins_blockchain(4.9)
add_coins_blockchain(7.9)