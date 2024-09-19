class UPGMA():    
    #finds the smallest distance in the matrix, not including the diagonal zeros
    def find_min_distance(matrix):
        min_value = float('inf')
        min_indices = (0, 1)
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                if matrix[i][j] < min_value:
                    min_value = matrix[i][j]
                    min_indices = (i, j)
        return min_indices
    
    #update matrix with new distances and nodes
    def updateMatrix(matrix, nodes, i, j, new_node):
        #TODO: update the matrix with the new distances

        #calculate the distances between new_node and all other nodes
        for n in range(len(nodes)):
            #skip the new_node
            if nodes[n] == new_node:
                continue

            #calculate the new distance between new_node and node[n]
            new_dist = (matrix[i][n] + matrix[j][n]) / 2

            #update the matrix with the new distance
            matrix[i][n] = new_dist
            matrix[n][i] = new_dist
                
        #remove the nodes that were combined
        matrix.pop(i)
        for row in matrix:
            row.pop(j)


    #builds the tree
    def buildTree(matrix, nodes):
        # initialize an empty tree
        rawTree = []

        #loop until there is only one label left
        while len(matrix) > 1: 
            i, j = UPGMA.find_min_distance(matrix)
            l1 = nodes[i]
            l2 = nodes[j]
            new_node = '(' + l1 + ',' + l2 + ')' #create new label, ex: (A,B)

            #adds the combine label to output tree
            rawTree.append(new_node)
            
            #remove the nodes that were combined
            nodes.remove(l1)
            nodes.remove(l2)

            #add the new label to the list of nodes
            nodes.append(new_node)

            #update the matrix with the new label with updated distances
            UPGMA.updateMatrix(matrix, nodes, i, j, new_node)
        
        #End of while loop
        return rawTree
        
if __name__ == "__main__":

    # Example usage with a distance matrix and corresponding nodes
    distance_matrix = [
        [0, 19, 27, 8, 3, 18],
        [19, 0, 31, 18, 36, 9],
        [27, 31, 0, 26, 41, 32],
        [8, 18, 26, 0, 31, 17],
        [3, 36, 41, 31, 0, 35],
        [18, 9, 32, 17, 35, 0]
    ]

    #create nodes based on the distance matrix
    aphla = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nodes = []
    for i in range(len(distance_matrix)):
        nodes.append(aphla[i])

    rawTree = UPGMA.buildTree(distance_matrix, nodes)

    print(rawTree)

    #format raw tree to print out a .txt file
    with open('UPGMA_Result.txt', 'w') as f:
        for r in rawTree:
            f.write(r + '\n')
        f.close()
        
            