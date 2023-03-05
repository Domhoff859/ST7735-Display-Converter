import cv2
from pathlib import Path
import numpy as np

if __name__ == '__main__':
    # Read Image
    current_path = Path(__file__).parent
    img1 = cv2.imread(str(current_path.joinpath('vac2.bmp')), cv2.IMREAD_COLOR)

    # Convert to RGB565
    R5 = (img1[...,0]>>3).astype(np.uint16) << 11
    G6 = (img1[...,1]>>2).astype(np.uint16) << 5
    B5 = (img1[...,2]>>3).astype(np.uint16)
    RGB565 = R5 | G6 | B5
    
    # Add '{' to begin and '},' to end of each line
    with open('vac.txt', "w") as file:
        for row in RGB565:
            file.write("{")
            for i, value in enumerate(row):
                if i < len(row) - 1:
                    file.write(f"{value}, ")
                else:
                    file.write(f"{value}")
            file.write("},\n")
