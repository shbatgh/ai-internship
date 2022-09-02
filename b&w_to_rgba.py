import os.path
import numpy as np
from PIL import Image

def pil2numpy(img: Image = None) -> np.ndarray:
    if img is None:
        print("No image provided")

    np_array = np.asarray(img)
    return np_array

def numpy2pil(np_array: np.ndarray) -> Image:
    assert_msg = 'Input shall be a HxWx4 ndarray'
    assert isinstance(np_array, np.ndarray), assert_msg
    assert len(np_array.shape) == 3, assert_msg
    assert np_array.shape[2] == 3, assert_msg

    img = Image.fromarray(np_array, 'RGBA')

    return img
