import numpy as np

def pading(image,pad):

    irow,icol=image.shape


    output = np.zeros(image.shape)
    
    padded_image = np.zeros((irow + (2 * pad), icol + (2 * pad)))
    padded_image[pad:padded_image.shape[0] - pad, pad:padded_image.shape[1] - pad] = image
    
    print(padded_image)

if __name__ == '__main__':

    image = np.array([[1,3,43,1,2,3],
                    [7,0,0,9,1,12],
                    [0,1,2,16,17,20],
                    [0,0,0,7,100,22],
                    [1,0,0,0,4,3]])

    pad = 1

pading(image,pad)
