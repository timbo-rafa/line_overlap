from line_overlap import line_overlap
import math

class TestReversedLineOverlap:
    def test_x2_x1_x4_x3_should_not_overlap(self):
        assert line_overlap(2,1,4,3) == False
    
    def test_x4_x3_x2_x1_should_not_overlap(self):
        assert line_overlap(4, 3, 2, 1) == False

    def test_x4_x2_x1_x3_should_overlap(self):
        assert line_overlap(3,2,4,1) == True

    def test_x4_x2_x3_x1_should_overlap(self):
        assert line_overlap(4,2,3,1) == True

    def test_x2_x1_x2_x1_should_overlap(self):
        assert line_overlap(2, 1, 2, 1) == True

    def test_x2_x4_x3_x1_should_overlap(self):
        assert line_overlap(4,1,3,2) == True

    def test_x2_x4_x1_x3_should_overlap(self):
        assert line_overlap(3,1,4,2) == True