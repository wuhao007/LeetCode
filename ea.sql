Customer
Customer_id
Customer_name
Address
...

Orders
Order_Id
Customer_id
amount
date
...

Customer_id No_Of_orders

SELECT Customer_id, COUNT(Order_Id)
FROM Orders 
GROUP BY Customer_id

Customer_name No_Of_orders

SELECT Customer_name, COUNT(Order_Id)
FROM Orders JOIN Customer on Customer.Customer_id = Orders.Customer_id
GROUP BY Customer.Customer_id

Placed more than 10 orders

SELECT Customer_name
From Orders JOIN Customer on Customer.Customer_id = Orders.Customer_id GROUP by Customer_id
Having COUNT(*) > 10

SELECT Customer_name, COUNT(Order_Id)
From Orders JOIN Customer on Customer.Customer_id = Orders.Customer_id  
where count(Order_Id) > 10 
GROUP by Customer_id


1. I created an account on Amazon.com
2. You created an account on Amazon.com
3. I placed an order on Amazon.com

SELECT Customer_name, COUNT(Order_Id) 
FROM Customer LEFT JOIN Orders on Customer.Customer_id = Orders.Customer_id
GROUP BY Customer.Customer_id

Selected column not a part of the aggregate clause

User[] getFifaUsers();
User[] getBattlefieldUsers();


def getCommonUsers():
    user_set = set()
    for user in getFifaUsers():
        user_set.add(user)
    common_user = []
    for user in getBattlefieldUsers():
        if user in user_set:
            common_user += [user]
    return common_user
    
def getCommonUsers():
    user_set = set()
    fifa_array = getFifaUsers()
    battle_array = getBattlefieldUsers()
    common_user = []
    if len(fifa_array) < len(battle_array):
        for user in fifa_array:
            user_set.add(user)
        for user in getBattlefieldUsers():
            if user in user_set:
                common_user += [user]
    else:
        for user in battle_array:
            user_set.add(user)
        for user in getfifaUsers():
            if user in user_set:
                common_user += [user]
   return common_user
    
BST

        a
       / \
       b  c
           \
            d
            
Node getSecondHighestValuesNode(Node root);

class Solution:
    def __init__(self):
        self.prev = None
        self.current = None
    def getSecondHighestValuesNode(self, Node root):
        if root.left:
            self.getSecondHighestValuesNode(root.left)
        self.prev = self.current   
        self.current = root.val
        if root.right:
            self.getSecondHighestValuesNode(root.right)   
        return self.prev  
        
        a
       / \
      b   c
           \
            d
prev = None
current = None

prev = None
current = b

prev = b
current = a

prev = a
current = c

prev = c
current = d
