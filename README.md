# Flood Fill Algorithm Implementation

This Python program implements the Flood Fill Algorithm, a technique used in image processing and computer graphics to fill connected regions with a particular color.

## Description

The Flood Fill Algorithm starts from a given point (seed) in an image and floods outwards, filling neighboring pixels with a target color until all connected pixels of the same color are filled. This implementation provides a step-by-step flood fill process with visualization capabilities.

## Features

- **Node and Graph Classes**: The program defines classes for nodes and graphs to represent the image and its connectivity.
- **Flood Fill Step-by-Step**: Implements flood fill algorithm step by step, allowing visualization of the process.
- **Boundary Checking**: Ensures that the algorithm doesn't exceed image boundaries during flood fill.

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Open a terminal or command prompt and navigate to the directory containing the program files.
4. Run the program by executing the following command: python floodFillAlgorithm.py
5. The program will prompt you to input the starting coordinates and the target color for flood fill.
6. Once the flood fill process is complete, the modified image will be displayed, and the total number of possible edges will be printed.

## Example

```python
image = [ [1, 0, 0, 0, 0],
 [1, 1, 0, 1, 0],
 [0, 1, 1, 1, 0],
 [0, 1, 1, 1, 1],
 [0, 1, 1, 0, 1]
]

graph = Graph()
print(graph.floodFillStepByStep(image, 2, 2, 2))
print("Total Possible Edges:", graph.edgeCount)
