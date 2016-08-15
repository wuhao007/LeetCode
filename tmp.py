class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m=len(matrix)
        if m==0:
            return None
        n=len(matrix[0])
        if n==0:
            return None
        
        self.matrix=list(matrix)
        self.m=m
        self.n=n
        self.dic=[[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.build(i,j,matrix[i-1][j-1])
                
    def build(self,i,j,value):
        x=[]
        y=[]
    
        while i<=self.m:
            x.append(i)
            i+=i&(-i)
        
        while j<=self.n:
            y.append(j)
            j+=j&(-j)
    
        for i in x:
            for j in y:
                self.dic[i][j]+=value
                
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        value=val-self.matrix[row][col]
        self.matrix[row][col]=val
        self.build(row+1,col+1,value)

        
        
    def getsum(self,i,j):
        x=[]
        y=[]

        while i:
            x.append(i)
            i-=i&(-i)
        
        while j:
            y.append(j)
            j-=j&(-j)
        
        temp=0
        for i in x:
            for j in y:
                temp+=self.dic[i][j]
        
        return temp
            
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getsum(row2+1,col2+1)-self.getsum(row1,col2+1)-self.getsum(row2+1,col1)+self.getsum(row1,col1)
