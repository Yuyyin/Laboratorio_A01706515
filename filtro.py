"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/

Modified by Uriel Sánchez
"""

import numpy as np   #numpy es una libreria de python
import cv2           #import cv2 libreria de python
import matplotlib.pyplot as plt #marplotlib.pyplot es otra de las librerias de python

def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def convolution(image, kernel):
    """Aplica una convolucion sin padding (valida) de una dimesion 
    y devuelve la matriz resultante de la operación
    """

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = kernel.shape #asigna alto y ancho del filtro
    
    output_x = (image_col - (kernel_col / 2) * 2) + 1 
    output_y = (image_row - (kernel_row / 2) * 2) + 1 
    
    output = np.zeros([int(output_y), int(output_x)]) #matriz donde guardo el resultado

    for row in range(int(output_y)):
        for col in range(int(output_x)):
            output[row, col] = conv_helper(
                                image[row:row + kernel_row, 
                                col:col + kernel_col],kernel)

if __name__ == '__main__':

    image = cv2.imread("index.jpg")

    filter = np.array([[1/9,1/9,1/9],
                    [1/9,1/9,1/9],
                    [1/9,1/9,1/9]]) 
plt.imshow(image, cmap='gray')
plt.title('woow')
plt.show()

print("Filter: ")
print(filter)
convolution(image, filter) 