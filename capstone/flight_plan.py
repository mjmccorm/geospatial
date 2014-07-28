#Flight_plan.py - a script to build a flight plan for a quadcopter around
#   a building.

import arcpy
from arcpy import env

#workspace
env.workspace = "C:/GIS/Adams Township/"

#target building
v_input_polygon = ""

#spatial reference
v_spatial_reference = ""

#units of measurement
v_measurement_units = "Feet"

#distance between buffers
v_buffer_interval = 10

#max distance from the building
v_max_distance = 70

#the centroid
v_output_point = ""

#bearing table
v_output_table_name = ""
v_output_table_path = ""

def setSpatialReference(v_input):
    #v_spatial_reference = arcpy.Describe(v_input).spatialReference

    return True

def addToOutputTable(v_X, v_Y, v_Bearing, v_Distance, v_Units):

    return True


def openOutputTable(v_path, v_name):
    try:
        f_outputfile = open(v_path+v_name)

        return True
    
    except IOError as e:
        print(e)
        return False
    
    else:
        return False

def closeOutputTable(f_outputfile):
    try:
        f_outputfile.close()

        return True;
    
    except IOError as e:
        print(e)
        return False
    
    else:
        return False

def setCentroid(v_polygon, v_output_point):
    #http://support.esri.com/cn/knowledgebase/techarticles/detail/41027

    #use arcpy to find centroid of input polygon
    v_Centroid = v_polygon

    #arcpy.FeatureToPoint_management(v_polygon, v_output_point,"CENTROID")
    
    return v_Centroid

def getCentroidX(v_point):
    v_X = 12.2

    return v_X

def getCentroidY(v_point):
    v_Y = 14.6

    return v_Y

def stradd(a, b):
    return a + b

def main():
    #set coordinate system
    #create buffers around input polygon
    #find centroid and get X, Y coordinates
    #open output table
    #for i in range(0,360,v_interval):
    #add new line (X,Y,i,v_max_distance+v_building_width)
    #run BearingToLine on this new table
    #clip the lines so they are not inside building polygon
    #set colors
    #display input polygons, buffers, and bearingLines
    
    print(stradd(getCentroid(v_input_polygon), " hello world"))

if __name__ == "__main__":
    main()
    
