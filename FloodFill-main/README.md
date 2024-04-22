# Flood Fill Algorithm

This Python program implements the flood fill algorithm, which is commonly used in image processing to fill connected regions with a certain color or pattern.

## How it works

The program uses a `Graph` class to represent the image and a `Node` class to represent each pixel in the image. Each `Node` has a list of its neighboring nodes.

The `floodFillStepByStep` method in the `Graph` class is the main implementation of the flood fill algorithm. It starts from a given pixel and changes the color of all connected pixels that have the same color as the starting pixel.

The `neighbours` method is used to find the valid neighbors of a given pixel. A neighbor is valid if it is within the image boundaries and its color is the same as the starting pixel's color.

The `displayImage` method is used to print the current state of the image to the console for visualization.

## How to run the program

1. Ensure you have Python installed on your machine.
2. Clone this repository or download the `floodFillAlgorithm.py` file.
3. Open a terminal/command prompt and navigate to the directory containing the `floodFillAlgorithm.py` file.
4. Run the command `python floodFillAlgorithm.py`.
5. The program will start and you can see the flood fill algorithm in action.

## Example

```python
image = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 0, 1]
]

graph = Graph()

print(graph.floodFillStepByStep(image, 2, 2, 2))
In this example, the program starts the flood fill algorithm from the pixel at position (2, 2) and changes all connected pixels with the same color to the color 2.

Note
This is a simple program and does not use real-world images. The image is represented as a 2D array of numbers, where each number represents a pixel color. The flood fill algorithm is demonstrated step by step, with a 1-second pause between each step for visualization.

```
