## Detect mirror symmetry

#### Author: yiran jing
#### Date: Feb 2020 


import sys
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob
from mirror_symmetry import * # class and helper function


def main():
    argc = len(sys.argv)
    if not (argc == 2):
        print("Usage: python detect.py choice")
        return
    
    elif sys.argv[1] =='example': # run butter fly example
        detecting_mirrorLine('butterfly.png', "butterflywith Mirror Line", show_detail = True)
        return
    
    elif sys.argv[1] =='test': # run test case
        """
        test animal and people image
        """
        test_case("images/1_*.png")
        
        """
        test symmetry architecture
        """
        test_case("images/2_*.png")
        
        """
        test other natural phenomenon
        """
        test_case("images/3_*.png")
        
        """
        test symmetry object with reflection
        """
        test_case("images/4_*.png")
        
        """
        test symmetry object with shadow
        """
        test_case("images/5_*.png")
        
        """
        test rotational symmetry
        """
        test_case("images/6_*.png")
        
        """
        test images includes multiple symmetry objects
        """
        test_case("images/7_*.png")
        
        """
        test non-symmetry object
        """
        test_case("images/8_*.png")
        return
    else:
        print("Error")
        return


    
if __name__ == '__main__':
    main()
