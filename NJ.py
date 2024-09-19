class Neighbor_Joining():

    def calculateDivergenceMatrix(matrix):
        #initialize the divergence matrix with 0s
        divergence_matrix = [[0 for x in range(len(matrix))] for y in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                iMatrixSum = sum(matrix[i])
                jMAtrixSum = sum(matrix[j])
                divergence_matrix[i][j] = matrix[i][j] - (iMatrixSum + jMAtrixSum)/(len(matrix)-2)
        return divergence_matrix
    
    def joinMatrixAndPairNodes(divergence_matrix, nodes, result):
        #find the minimum value in the divergence matrix
        min_value = divergence_matrix[0][0]
        min_location = (0, 0)

        for i in range(len(divergence_matrix)):
            for j in range(len(divergence_matrix[i])):
                if divergence_matrix[i][j] < min_value:
                    min_value = divergence_matrix[i][j]
                    min_location = (i, j)
        
        #pair two nodes to output list
        result.append((min_location[0], min_location[1]))

        #join the two nodes
        joined_matrix = []
        for i in range(len(divergence_matrix)):
            if i != min_location[0] and i != min_location[1]:
                new_row = []
                for j in range(len(divergence_matrix[i])):
                    if j != min_location[0] and j != min_location[1]:
                        new_row.append(divergence_matrix[i][j])
                joined_matrix.append(new_row)

        return joined_matrix        

    def buildTree(matrix, nodes):
        result = []
        while (len(matrix) > 3):
            divergence_matrix = Neighbor_Joining.calculateDivergenceMatrix(matrix)
            joined_matrix = Neighbor_Joining.joinMatrixAndPairNodes(divergence_matrix, nodes, result)
            matrix = joined_matrix
        return result


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

    rawTree = Neighbor_Joining.buildTree(distance_matrix, nodes)
    
    #convert the raw tree to a newick tree
    newickTree = []
    for i in range(len(rawTree)):
        newickTree.append('(' + nodes[rawTree[i][0]] + ',' + nodes[rawTree[i][1]] + ')')
    newickTree.append('(' + nodes[rawTree[0][0]] + ',' + nodes[rawTree[0][1]] + ');')
    #print(''.join(newickTree))

    #write the newick tree to a file
    with open('NJ.txt', 'w') as f:
        f.write(''.join(newickTree))
        