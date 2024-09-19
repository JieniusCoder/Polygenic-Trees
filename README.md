README
This repository contains two Python classes used for constructing phylogenetic trees from a distance matrix: UPGMA (Unweighted Pair Group Method with Arithmetic Mean) and Neighbor Joining. Both classes are aimed at the molecular evolution research, but can be applied in other fields where hierarchical clustering is needed.

Classes and Methods:
Class UPGMA()
UPGMA is a simple hierarchical clustering method used in bioinformatics for the creation of phenetic trees (phenograms).

find_min_distance(matrix)
Finds the smallest distance in the provided matrix, excluding diagonal zeros. Returns the indices of the smallest distance.

updateMatrix(matrix, nodes, i, j, new_node)
Updates the provided distance matrix with new distances and nodes. It calculates the distances between the newly created node and all other nodes, updates the matrix with these new distances and removes the combined nodes.

buildTree(matrix, nodes)
Builds the phylogenetic tree based on the given distance matrix and nodes. The method repeatedly finds the smallest distance, combines the corresponding nodes into a new node, and updates the matrix until only one node remains. The result is a list of combined labels representing the phylogenetic tree.

Class Neighbor_Joining()
Neighbor Joining is a bottom-up (agglomerative) clustering method for the creation of phylogenetic trees, usually based on DNA or protein sequence data.

calculateDivergenceMatrix(matrix)
Calculates the divergence matrix from the provided distance matrix. The divergence of two nodes is defined as their distance minus the average distances of each node to all other nodes.

joinMatrixAndPairNodes(divergence_matrix, nodes, result)
Finds the minimum value in the divergence matrix and pairs the corresponding nodes. It also updates the matrix by joining the nodes and removing the combined rows and columns.

buildTree(matrix, nodes)
Builds the phylogenetic tree based on the given distance matrix and nodes. The method repeatedly calculates the divergence matrix, pairs the nodes with the smallest divergence, and updates the matrix until only three nodes remain. The result is a list of node pairs representing the phylogenetic tree.

Usage
Both classes can be used by providing a symmetric distance matrix and a list of node labels. Each class has a buildTree method which returns a raw tree, a list of combined node labels. For UPGMA, the output raw tree can be directly printed or written to a file. For Neighbor Joining, the output raw tree is converted to Newick format before being written to a file.

Example
The main part of each script contains an example usage with a sample distance matrix and corresponding nodes. The nodes are labeled as uppercase English letters ('A', 'B', 'C', etc.) in order of their appearance in the matrix. The resulting tree is written to a text file ('UPGMA_Result.txt' for UPGMA and 'NJ.txt' for Neighbor Joining).

How to run the code:
    Replace the distanec matrix in the main method with your own distance matrix, and run
    'py NJ.py' for neighbor joining tree
    'py UPGMA.py' for UPGMA Tree
    The output file in is newick format. 