import unittest
from vector3d import Vector3D

import math

class TestVector3DClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Vector3D(1, 2, 3) + Vector3D(4, 5, 6), Vector3D(5, 7, 9))

    def test_sub(self):
        self.assertEqual(Vector3D(1, 2, 3) - Vector3D(4, 5, 6), Vector3D(-3, -3, -3))

    def test_mul(self):
        self.assertEqual(Vector3D(1, 2, 3) * 1, Vector3D(1, 2, 3))
        self.assertEqual(Vector3D(1, 2, 3) * 1.5, Vector3D(1.5, 3.0, 4.5))

    def test_rmul(self):
        self.assertEqual(1 * Vector3D(1, 2, 3), Vector3D(1, 2, 3))
        self.assertEqual(1.5 * Vector3D(1, 2, 3), Vector3D(1.5, 3.0, 4.5))

    def test_mul_and_rmul(self):
        self.assertEqual(2 * Vector3D(1, 2, 3) * 3, Vector3D(6, 12, 18))

    def test_truediv(self):
        self.assertEqual(Vector3D(1, 2, 3) / 2, Vector3D(0.5, 1.0, 1.5))

    def test_floordiv(self):
        self.assertEqual(Vector3D(1, 2, 3) // 2, Vector3D(0, 1, 1))

    def test_eq(self):
        self.assertTrue(Vector3D(1, 2, 3) == Vector3D(1, 2, 3))

        self.assertFalse(Vector3D(1, 2, 3) == Vector3D(1, 2, 0))
        self.assertFalse(Vector3D(1, 2, 3) == Vector3D(1, 0, 3))
        self.assertFalse(Vector3D(1, 2, 3) == Vector3D(0, 2, 3))

    def test_ne(self):
        self.assertTrue(Vector3D(1, 2, 3) != Vector3D(1, 2, 0))
        self.assertTrue(Vector3D(1, 2, 3) != Vector3D(1, 0, 3))
        self.assertTrue(Vector3D(1, 2, 3) != Vector3D(0, 2, 3))

        self.assertFalse(Vector3D(1, 2, 3) != Vector3D(1, 2, 3))

    def test_abs(self):
        self.assertAlmostEqual(abs(Vector3D(1, 2, 3)), 3.7416573867739413)
        self.assertEqual(abs(Vector3D(3, 4, 0)), 5)

        test_cases = [
            (-4.5, 4, 3),
            (math.pi, math.e, -1),
        ]
        for x, y, z in test_cases:
            actual = abs(Vector3D(x, y, z))
            excepted = math.sqrt(x * x + y * y + z * z)
            self.assertAlmostEqual(actual, excepted)

if __name__ == '__main__':
    unittest.main()

