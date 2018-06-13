#Name: Michelle Arthars
#AUID: 564540995

"""
This program takes list.txt as input
and outputs the adjacency list for the reverse digraph(
where all arcs point the opposite way) in a file reverselist.txt
"""

def main():
    inputs = open("list.txt", "r")
    contents = inputs.read()
    outputs = open("reverselist.txt", "w")
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








main()
