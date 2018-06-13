#Name: Michelle Arthars
#AUID: 564540995

"""
This program will
1) Read the matrix.txt file;
2) Convert the matrix.txt to a list;
3) Create the list of the reversed graph;
4) Perform a DFS on the reversed graph and output the trees 
5) Perform a DFS on the original graph: whenever it starts a new tree
in the search forest, it always picks the white node that is closest to the
bottom of the list created in step 4)
6) Finally, the program outputs a text file components.txt that contains a
comma-separated list of the strongly connected components in matrix.txt. 
"""

def matrix_list ():
    inputs = open("matrix.txt", "r")
    contents = inputs.read()
    outputs = open("list3.txt", "w") #write to a different file
    inputs.close()
    u_list = contents.split("\n")
    for i in u_list: #going through each rows of the matrix
        data = ''
        count = 0
        for j in i: #going through each column of the matrix
            if j == ',':
                count -=1
            elif j == '1':
                c = str(count) #get index for intersection
                data += c + ', '
            count += 1
        outputs.write((data[:-2] + "\n")) #removing the last comma
    outputs.close()


def reverse_list():
    inputs = open("list3.txt", "r") #read the reverselist
    contents = inputs.read()
    outputs = open("reverselist3.txt", "w") #write to another file
    inputs.close()
    uv_list = contents.split("\n")
    r_list = [[]for i in range (len(uv_list))] #creates number of empty list based on num of rows
    node = 0
    for i in uv_list: #starts at all nodes u of original list
        a_list = i.split(', ')
        for j in a_list: #goes through all nodes that were v of original list before reverse
            if not j: #stop if meets empty list at the end
                break
            num = int(j)
            r_list[num].append(node)
        node += 1

    for i in r_list:
        row = str(i)
        outputs.write(row[1:-1] +"\n") #write data into file
    outputs.close()



def dfs_visit(uv_list, node, white, grey, black):
    if node in white:
        white.remove(node)
        grey.append(node)
        path = uv_list[node].split(', ')
        for i in path:
            if i != '':
                index = int(i)
                if index in white:
                    dfs_visit(uv_list, index, white, grey, black)
        black.append(node)
        grey.pop()
        return black

def dfs_reverse(alist, dfs_text):
    inputs = open(alist, "r") #read the reverse list
    contents = inputs.read()
    outputs = open(dfs_text, "w") #write to a new file
    inputs.close()
    uv_list = contents.split("\n")
    for i in uv_list:
        if (i == '') or (i == '\n'):
            uv_list.remove(i)
    white = [i for i in range(len(uv_list)- 1)]
    grey = []
    black = []
    while len(white) > 0:
        new = dfs_visit(uv_list, white[0], white, grey, black)
        black.append('')
    index = 0
    for i in range (len(black)):
        if black[i] != '':
            outputs.write(str(index) + ',' + str(black[i]) + "\n")
            index += 1
        else:
            outputs.write('\n')
    outputs.close()
    return black

def dfs(alist, dfs_text, rblack):
    inputs = open(alist, "r") #read the reverse list
    contents = inputs.read()
    outputs = open(dfs_text, "w") #write to a new file
    inputs.close()
    uv_list = contents.split("\n")
    white = [i for i in rblack]
    grey = []
    black = []
    while len(white) > 0:
        new = dfs_visit(uv_list, white[0], white, grey, black)
        black.append('')
    index = 0
    for i in range (len(black)):
        component = []
        if black[i] != '':
            #outputs.write(str(index) + ',' + str(black[i]) + "\n")
            component.append(black[i])
        else:
            connect = ''
            print(component)
            for i in component:
                connect += str(i)
            print(connect)
            outputs.write(connect)
    outputs.close()
    return black


def main():
    matrix_list()
    reverse_list()
    black = dfs_reverse("reverselist3.txt", "dfs3r.txt")
    for i in black:
        if i == '':
            black.remove(i)
    rblack = black[::-1]
    dfs("list3.txt", "dfs3.txt", rblack)





main()
