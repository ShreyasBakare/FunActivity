# Calculating pi using random numbers
---
The ```random.random()``` function in python can generate a random number between 0 and 1. A pair of such random numbers will represent random points on a square of unit area on the first quadrant. Inside this square, a circle of radius 0.5 at the center (0.5, 0.5) will have an area of ```0.25*pi*pi```. Thus, the ratio of area of the circle to that of the square is ```pi/4```.

The random points we generated using the ```random()``` function falls randomly on the square. Some of them will fall outside the circle, some of them will fall inside the cirle. Here is the key point.

##### The fraction of points falling inside the circle approaches the ratio of areas (circle:square = pi/4)

The more points you have, the more 'correct' this relation becomes. You can use this relation to calculate pi numerically.

##### Commments on this method:
- This method involves a while loop running for each random point.
- Loops (iterative methods) are slow with python.
- C++ may be faster for the same algorithm (I'll have to try it).