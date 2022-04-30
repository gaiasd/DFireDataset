""" Some functions that can be useful for dealing with coordinates. """

def non_negative(coord):
    
    """
        Sets negative coordinates to zero. This fixes bugs in some labeling tools.
        
        Input:
            coord: Int or float
            Any number that represents a coordinate, whether normalized or not.
    """
    
    if coord < 0:
        return 0
    else:
        return coord
    
def pixel2yolo(dim, pixel_coords):
    
    """
        Transforms coordinates in YOLO format to coordinates in pixels.
        
        Input:
            dim: Tuple or list
            Image size (width, height).
            pixel_coords: List
            Bounding box coordinates in pixels (xmin, ymin, xmax, ymax).
        Output:
            yolo_coords: List
            Bounding box coordinates in YOLO format (xcenter, ycenter, width, height).
    """
    
    dw = 1/dim[0]
    dh = 1/dim[1]
    xcenter = non_negative(dw*(pixel_coords[0] + pixel_coords[2])/2)
    ycenter = non_negative(dh*(pixel_coords[1] + pixel_coords[3])/2)
    width = non_negative(dw*(pixel_coords[2] - pixel_coords[0]))
    height = non_negative(dh*(pixel_coords[3] - pixel_coords[1]))
    
    yolo_coords = [xcenter, ycenter, width, height]
    
    return yolo_coords

def yolo2pixel(dim, yolo_coords):
    
    """
        Transforms coordinates in YOLO format to coordinates in pixels.
        
        Input:
            dim: Tuple or list
            Image size (width, height).
            yolo_coords: List
            Bounding box coordinates in YOLO format (xcenter, ycenter, width, height).
        Output:
            pixel_coords: List
            Bounding box coordinates in pixels (xmin, ymin, xmax, ymax).
    """
    
    xmin = non_negative(round(dim[0] * (yolo_coords[0] - yolo_coords[2]/2)))
    xmax = non_negative(round(dim[0] * (yolo_coords[0] + yolo_coords[2]/2)))
    ymin = non_negative(round(dim[1] * (yolo_coords[1] - yolo_coords[3]/2)))
    ymax = non_negative(round(dim[1] * (yolo_coords[1] + yolo_coords[3]/2)))
    
    pixel_coords = [xmin, ymin, xmax, ymax]
    
    return pixel_coords