import sys

def djkastras(graph,src,dest):
    inf = sys.maxsize

    node_data = {

        'A':{'cost': inf, 'path':[]},
        'B':{'cost': inf, 'path':[]},
        'C':{'cost': inf, 'path':[]},
        'D':{'cost': inf, 'path':[]},
        'E':{'cost': inf, 'path':[]},
        'F':{'cost': inf, 'path':[]}


    }
    unvisited = []#contains all the details of the unvisited nodes
    for i in node_data:
        unvisited.append(i)

    #initialise the cost of the source to 0
    node_data[src]['cost']= 0

    #add the src to the visited arr
    visited = []
    visited.append(src)
    unvisited.remove(src)

    #main code

#loop throught the neighbours
    for i in range(5):
   

        for neighbour in graph[src]:

            #check if the neighbours are in unvisited
            if neighbour in unvisited:
                
                if node_data[src]['cost']+graph[src][neighbour]< node_data[neighbour]['cost']:
                    #cost of neighbour is cost of source+ cost of weight
                    node_data[neighbour]['cost'] = node_data[src]['cost']+graph[src][neighbour]

                    node_data[neighbour]['path'].append(src)
                    node_data[neighbour]['path']+=node_data[src]['path']
                    #get the neighbour with the shortest distance
            
            #i need to make the node in the unvisited array with the shortest distance as the new src
            #assuming the first element in the list to be the smallest
        min = unvisited[0]
        for i in unvisited:
            #if the sd of the subsequent array is lesser that the sd of the min the i becomes the new min
        
            if node_data[i]['cost']< node_data[min]['cost']:
                min = unvisited[i]
        
        src = min

        unvisited.remove(min)

    print('the cost to move from source is',node_data[dest]['cost'])
   
    s = ''
    for i in node_data[dest]['path'][::-1]:
        s+= i 
        s+='--->'
   
    print('the path travelled is',s,dest)


graph = {

    'A':{'B':2,'C':4},
    'B':{'A':2,'C':3,'D':2},
    'C':{'A':4,'B':3,'E':5,'D':2},
    'D':{'B':8,'C':2,'E':11,'F':22},
    'E':{'C':5,'D':11,'F':22},
    'F':{'D':22,'E':22}
    

}

source = 'A'
destination = 'E'
djkastras(graph,source,destination)