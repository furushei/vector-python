# Vector3D
If you want to perform vector or matrix operation with Python, [numpy](http://www.numpy.org/) is a popular solution. However, in situations where numpy can not be used, this module will provide one of the alternative options.

## Simple Usage
```python
>>> from vector3d import Vector3D
>>> a = Vector3D(1, 2, 3)
>>> b = Vector3D(3, -1, 4)
>>> a + b
Vector3D(4, 1, 7)
>>> 2 * a
Vector3D(2, 4, 6)
>>> abs(a)
3.7416573867739413
```

Note: `Vector3D` class can also be used as 2D vector.
```python
>>> Vector3D(3, 0) + Vector3D(0, 4)
Vector3D(3, 4)
```
