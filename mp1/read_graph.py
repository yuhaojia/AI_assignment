class Graph:
    def __init__(self, file):
        self.data = [];
        with open(file) as f:
            for line in f:
                self.data.append(list(line))
        for row in range(len(self.data) - 1):
            del self.data[row][-1];
    
        self.size = (len(self.data), len(self.data[0]))
        
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                if self.data[row][col] == 'P':
                    self.start = (row,col)
                    self.Position = [row,col]
                if self.data[row][col] == '.':
                    self.dot = (row,col)


    def pos_judge(self, row, col):
        return self.data[row][col]
    
    
    def showpath(self, path):
        for i in path:
            if i!= self.start:
                self.data[i[0]][i[1]] = '.'

    def writetofile(self, file):
        with open(file, 'w') as f:
            for i in self.data:
                f.write(''.join(i) + "\n")
