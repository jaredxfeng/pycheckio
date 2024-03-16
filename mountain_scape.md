https://py.checkio.org/en/mission/mountain-scape/
![image](https://github.com/jaredxfeng/pycheckio/assets/92383408/b5d626eb-d080-422d-b918-5b534870dc92)

You are given the coordinates of the tops of the triangles as input values.

  - The slope angle is 45 degrees.
  - The base is always on the x-axis.

You must return the total area of all triangles. But count the overlapping areas only once.

**NOTE:**

- The sum of the X and Y coordinates is always even. (e.g. (1, 3) (0, 2) ...)

**Example:**
```
mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37
```

![image](https://github.com/jaredxfeng/pycheckio/assets/92383408/f0ec4f76-1454-432d-bdc1-04311aeded0c)

**Input:** A list of a tuple of two integers.

**Output:** An integer.

**Precondition:**
- 0 ≤ x ≤ 100
- 1 ≤ y ≤ 50
- (x+y) % 2 == 0
- 1 ≤ len(tops) ≤ 50
