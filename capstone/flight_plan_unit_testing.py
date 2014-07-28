#https://docs.python.org/2/library/unittest.html

import flight_plan
import unittest

class flightplanTests(unittest.TestCase):

    def setUp(self):
        flight_plan.v_input_polygon = "testCentroid"
        flight_plan.v_output_table_path = "C\\Users\\mjmccorm\\Documents"
        flight_plan.v_output_table_name = "BuildingBearings"

    #def test_OpenOutputTable(self)
        #test success open
        #test file not found
        #test file read only 

    #def test_CloseOutputTable(self)
        #test success close
        #test nofileopen
        
    def test_1(self):
            self.assertEqual(flight_plan.getCentroid(flight_plan.v_input_polygon),"testCentroid")

    def test_2(self):
            self.assertEqual(flight_plan.stradd("a","c"),"ac")

    def test_3(self):
            self.assertTrue(flight_plan.stradd("a","c") != "")
    

if __name__ == "__main__":
        unittest.main()
