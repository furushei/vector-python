import unittest
from vector3d import Vector3D

class TestVector3DClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Vector3D(1, 2, 3) + Vector3D(4, 5, 6), Vector3D(5, 7, 9))

    def test_sub(self):
        self.assertEqual(Vector3D(1, 2, 3) - Vector3D(4, 5, 6), Vector3D(-3, -3, -3))

    def test_mul(self):
        self.assertEqual(1 * Vector3D(1, 2, 3), Vector3D(1, 2, 3))
        self.assertEqual(Vector3D(1, 2, 3) * 1, Vector3D(1, 2, 3))
        self.assertEqual(1.5 * Vector3D(1, 2, 3), Vector3D(1 * 1.5, 2 * 1.5, 3 * 1.5))
        self.assertEqual(Vector3D(1, 2, 3) * 1.5, Vector3D(1 * 1.5, 2 * 1.5, 3 * 1.5))
        self.assertEqual(2 * Vector3D(1, 2, 3) * 3, Vector3D(6, 12, 18))


if __name__ == '__main__':
    unittest.main()

