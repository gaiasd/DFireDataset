""" Some functions that can be useful for dealing with coordinates. """
import glob
import cv2


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

    dw = 1 / dim[0]
    dh = 1 / dim[1]
    xcenter = non_negative(dw * (pixel_coords[0] + pixel_coords[2]) / 2)
    ycenter = non_negative(dh * (pixel_coords[1] + pixel_coords[3]) / 2)
    width = non_negative(dw * (pixel_coords[2] - pixel_coords[0]))
    height = non_negative(dh * (pixel_coords[3] - pixel_coords[1]))

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

    xmin = non_negative(round(dim[0] * (yolo_coords[0] - yolo_coords[2] / 2)))
    xmax = non_negative(round(dim[0] * (yolo_coords[0] + yolo_coords[2] / 2)))
    ymin = non_negative(round(dim[1] * (yolo_coords[1] - yolo_coords[3] / 2)))
    ymax = non_negative(round(dim[1] * (yolo_coords[1] + yolo_coords[3] / 2)))

    pixel_coords = [xmin, ymin, xmax, ymax]

    return pixel_coords


def visualize(sample_index: int, path_to_data: str) -> None:
    """Visualize bounding boxes of sample with given index.
    Index is computed based on alphabetical order of image names.

    Args:
        sample_index (int): Index of image to be visualized
        path_to_data (str): Path to data. Data contains 'images' and 'labels' folder.
    """

    # Get image and labels names.
    images = list(glob.glob(f"{path_to_data}/images/*"))
    labels = list(glob.glob(f"{path_to_data}/labels/*"))

    # Sort image and label names. They will have the same order because their basenames are same.
    images.sort()
    labels.sort()

    # Open the annotation file.
    with open(labels[sample_index], "r") as annotation_file:

        # Read image
        image = cv2.imread(images[sample_index])
        h, w = image.shape[:2]

        annotation_found = False

        # Iterate over lines in the annotation file
        for line in annotation_file.readlines():

            annotation_found = True

            # Read line and convert its values from string to float
            values = line.split()
            values = [float(v) for v in values]

            # Get bounding box coordinates and clsas label
            xmin, ymin, xmax, ymax = yolo2pixel(dim=(w, h), yolo_coords=values[1:])
            class_label = int(values[0])

            # Draw bounding box and display class label
            cv2.rectangle(img=image, pt1=(xmin, ymin), pt2=(xmax, ymax), color=(255, 255, 255), thickness=2)
            cv2.putText(
                img=image,
                text=str(class_label),
                org=(xmin, ymin),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(255, 255, 255),
                thickness=1,
            )

        # Don't show anything if there is no annotation
        if annotation_found == False:
            print("Empty annotation:", images[sample_index])

        # Display annotation
        else:
            cv2.imshow(images[sample_index], image)
            cv2.waitKey()
            cv2.destroyAllWindows()

