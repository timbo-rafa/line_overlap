from line_overlap import line_overlap
import math

class TestLineOverlap:
    def test_x1_x2_x3_x4_should_not_overlap(self):
        assert line_overlap(1,2,3,4) == False
    
    def test_x3_x4_x1_x2_should_not_overlap(self):
        assert line_overlap(3, 4, 1, 2) == False

    def test_x3_x1_x2_x4_should_overlap(self):
        assert line_overlap(2,3,1,4) == True

    def test_x3_x1_x4_x2_should_overlap(self):
        assert line_overlap(2,4,1,3) == True

    def test_x1_x2_x1_x2_should_overlap(self):
        assert line_overlap(1, 2, 1, 2) == True

    def test_x1_x3_x4_x2_should_overlap(self):
        assert line_overlap(1,4,2,3) == True

    def test_x1_x3_x2_x4_should_overlap(self):
        assert line_overlap(1,3,2,4) == True