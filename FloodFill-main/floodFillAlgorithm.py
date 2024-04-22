import copy
import time


class Node:
    instance_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = list()
        Node.instance_count += 1


class Graph:
    explored = set()

    def __init__(self):
        self.edgeCount = 0

    def floodFillStepByStep(self, image, x, y, pixel):
        start = Node(x, y)
        queue = [start]
        image_copy = copy.deepcopy(image)  # Create a copy for visualization

        while queue:
            current_node = queue.pop(0)
            x, y = current_node.x, current_node.y

            if image_copy[y][x] == 1:
                image_copy[y][x] = pixel
                self.explored.add((x, y))

                # Visualization: Print the current image state
                self.displayImage(image_copy)
                time.sleep(1)  # Pause for visualization

                neighbors = self.neighbours(image_copy, x, y, current_node)
                queue.extend(neighbors)

        # Return the modified image represented as 2D array of numbers
        return image_copy

    def displayImage(self, image):
        for row in image:
            print(" ".join(map(str, row)))
        print("\n")

    def neighbours(self, image, x, y, currentNode):
        U = y - 1
        D = y + 1
        L = x - 1
        R = x + 1

        # Write the neighbours function to find the neighbours in four directions for a given pixel.
        # An edge is valid if the pixel is newly discovered, i.e. an edge is created when the neighbour's pixel value is one.
        # Append a valid new Node to the neighbours of the currentNode.
        # Remember to do boundary checking

        ###
        valid_neighbours = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if (
                0 <= new_x < len(image[0])
                and 0 <= new_y < len(image)
                and image[new_y][new_x] == 1
                and (new_x, new_y) not in self.explored
            ):
                valid_neighbours.append(Node(new_x, new_y))
                self.explored.add((new_x, new_y))
                self.edgeCount += 1

        return valid_neighbours


def start():
    image = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 1, 0, 1]
    ]

    graph = Graph()

    print(graph.floodFillStepByStep(image, 2, 2, 2))

    # DO NOT REMOVE THIS RETURN STATEMENT!
    return graph


graph = start()
# testing
print("Total Possible Edges:", graph.edgeCount)
