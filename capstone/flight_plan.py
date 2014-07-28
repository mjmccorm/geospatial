#Flight_plan.py - a script to build a flight plan for a quadcopter around
#   a building.

#import arcpy

#units of measurement
v_units = "Feet"
#distance between buffers
v_interval = 10
#max distance from the building
v_max_distance = 70
#target building
v_input_polygon = ""
v_output_point = ""

#
v_output_table_name = ""
v_output_table_path = ""

def openOutputTable(v_path, v_name):
    try:
        f_outputfile = open(v_path+v_name)

        return True;
    
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

def getCentroid(v_polygon):

    #use arcpy to find centroid of input polygon
    v_Centroid = v_polygon
    
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
    
    print(stradd(getCentroid(v_input_polygon), " hello world"))

if __name__ == "__main__":
    main()
    
