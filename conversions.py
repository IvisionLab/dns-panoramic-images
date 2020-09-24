"""
Functions used for conversion
"""
import cv2
import numpy as np

def decode_segs(mask, segmentations, fill_color=255):
    """
    Decode COCO format segmentations into a single mask
    Code based on https://gist.github.com/tzing/7d8020e411c0679282c734911c5df96b
    """
    pts = [
        np
            .array(anno)
            .reshape(-1, 2)
            .round()
            .astype(int)
        for anno in segmentations
    ]
    mask = cv2.fillPoly(mask, pts, fill_color)

    return mask

def annotations2mask(annotations, height, width, binary=False):
    """
    Convert COCO format to a single mask (non-binary or binary)
    """
    mask = np.zeros((height, width), np.uint8)
    for ann in annotations:
        segmentations = ann['segmentation']
        if binary:
            fill_color = 255
            mask = decode_segs(mask, segmentations, fill_color)
        else:
            fill_color = ann['category_id']
            mask = decode_segs(mask, segmentations, fill_color)

    return mask

def mask2instances(mask):
    """
    Return a mask for each instance present in the original mask.
    The instances in the original mask must be encoded with different colors,
    which also represent their categories (two instances of the same category is not allowed)
    Edited from: https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html
    """
    cat_ids = np.unique(mask)

    # remove the background
    cat_ids = cat_ids[1:]

    # split the color-encoded mask into a set of binary masks
    masks = (mask == cat_ids[:, None, None])

    # get bounding box coordinates for each mask
    num_objs = len(cat_ids)
    bboxes = np.zeros((num_objs, 4))
    for i in range(num_objs):
        pos = np.where(masks[i])
        xmin = np.min(pos[1])
        xmax = np.max(pos[1])
        ymin = np.min(pos[0])
        ymax = np.max(pos[0])
        width = xmax - xmin
        height =  ymax - ymin
        bboxes[i, :] = np.array([[xmin, ymin, width, height]]) # COCO format

    return masks, bboxes, cat_ids

def get_bbox_coordinates(bbox):
    """
    Get the bounding box coordinates from a length four array in the COCO format
    """
    x1, y1, w, h = bbox
    return np.array([[x1,     y1    ],
                     [x1 + w, y1    ],
                     [x1 + w, y1 + h],
                     [x1,     y1 + h]], np.int32)
