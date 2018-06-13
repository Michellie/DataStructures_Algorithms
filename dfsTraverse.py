#Name: Michelle Arthars
#AUID: 564540995

"""
This is a ython program that performs a
DFS traverse on a given digraph in list.txt
and outputs its result to a file dfs.txt.
The format of dfs.txt is as follows:
Each line will have 2 digits, the node prcess order and its value
An empty line will separate the tree from the forest
"""

def dfs(uv_list, node, white, grey, black):
    if node in white:
        white.remove(node)
        grey.append(node)
        path = uv_list[node].split(', ')
        #print("path", path)
        for i in path:
            index = int(i)
            if index in white:
                dfs(uv_list, index, white, grey, black)
        black.append(node)
        grey.pop()
        return black

def main():
        inputs = open("list.txt", "r")
        contents = inputs.read()
        outputs = open("dfs.txt", "w")
        inputs.close()
        uv_list = contents.split("\n")
        white = [i for i in range(len(uv_list))]
        grey = []
        black = []
        while len(white) > 0:
            new = dfs(uv_list, white[0], white, grey, black)
            black.append('')
        index = 0
        for i in range (len(black)):
            if black[i] != '':
                outputs.write(str(index) + ',' + str(black[i]) + "\n")
                index += 1
            else:
                outputs.write('\n')
        outputs.close()

main()
