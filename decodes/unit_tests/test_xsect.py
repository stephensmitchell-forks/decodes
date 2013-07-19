import unittest
import decodes.core as dc
from decodes.core import *


class Tests(unittest.TestCase):

    def test_bad_combonations(self):
        xsec = Intersector()
        with self.assertRaises(NotImplementedError): xsec.of(CS().xy_plane,Point())
        with self.assertRaises(NotImplementedError): xsec.of("afsd",10)
        with self.assertRaises(NotImplementedError): xsec.of(Point(),Ray(Point(2,2,-1),Vec(0,0,1)))

    def test_ray_plane(self):
        xsec = Intersector()

        ray = Ray(Point(2,2,1),Vec(0,0,-1))
        pln = CS().xy_plane
        self.assertEqual(xsec.of(ray,pln),True)
        self.assertEqual(xsec[0],Point(2,2,0))

        ray = Ray(Point(2,2,-1),Vec(0,0,1)) # ray behind plane
        self.assertEqual(xsec.of(ray,pln),True)
        self.assertEqual(xsec[0],Point(2,2,0))
        
        self.assertEqual(xsec.of(ray,pln,ignore_backface=True),False)
        self.assertEqual(len(xsec),0)

        ray = Ray(Point(2,2,1),Vec(0,0,1)) # plane behind ray
        self.assertEqual(xsec.of(ray,pln),False)
        self.assertEqual(len(xsec),0)
        
    def test_line_plane(self):
        xsec = Intersector()

        line = Line(Point(2,2,1),Vec(0,0,-1))
        pln = CS().xy_plane
        self.assertEqual(xsec.of(line,pln),True)
        self.assertEqual(xsec[0],Point(2,2,0))

        line = Line(Point(2,2,-1),Vec(0,0,1)) # line behind plane
        self.assertEqual(xsec.of(line,pln),True)
        self.assertEqual(xsec[0],Point(2,2,0))

        self.assertEqual(xsec.of(line,pln,ignore_backface=True),False)
        self.assertEqual(len(xsec),0)

        line = Line(Point(2,2,1),Vec(0,0,1)) # plane behind line
        self.assertEqual(xsec.of(line,pln),True)
        self.assertEqual(xsec[0],Point(2,2,0))

        line = Line(Point(2,2,0),Vec(0,1)) # line lies in plane
        self.assertEqual(xsec.of(line,pln),False)
        self.assertEqual(len(xsec),0)

        line = Line(Point(2,2,2),Vec(0,1)) # line parallel to plane
        self.assertEqual(xsec.of(line,pln),False)
        self.assertEqual(len(xsec),0)

    def test_seg_plane(self):
        xsec = Intersector()

        seg = Segment(Point(2,2,0.5),Vec(0,0,-1)) # seg crosses plane from front
        pln = CS().xy_plane
        self.assertEqual(xsec.of(seg,pln),True)
        self.assertEqual(xsec[0],Point(2,2,0))

        seg = Segment(Point(2,2,-0.5),Vec(0,0,1)) # seg crosses plane from behind
        self.assertEqual(xsec.of(seg,pln),True)
        self.assertEqual(xsec[0],Point(2,2,0))

        seg = Segment(Point(2,2,0.5),Vec(0,0,1)) # seg points away from plane
        self.assertEqual(xsec.of(seg,pln),False)
        self.assertEqual(len(xsec),0)

        seg = Segment(Point(2,2,1.5),Vec(0,0,-1)) # seg points toward plane
        self.assertEqual(xsec.of(seg,pln),False)
        self.assertEqual(len(xsec),0)

        seg = Segment(Point(2,2,0),Vec(0,1)) # seg lies in plane
        self.assertEqual(xsec.of(seg,pln),False)
        self.assertEqual(len(xsec),0)

        seg = Segment(Point(2,2,2),Vec(0,1)) # seg parallel to plane
        self.assertEqual(xsec.of(seg,pln),False)
        self.assertEqual(len(xsec),0)

    def test_circ_circ(self):
        xsec = Intersector()

        circ_a = Circle(CS().xy_plane,1.0)
        circ_b = Circle(CS.on_xy(1,0).xy_plane,1.0)
        self.assertEqual(xsec.of(circ_a,circ_b),True)
        