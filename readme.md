# Hollow Grid Mask
## Description
Image augmentation is preprocessing step done prior of network training to improve the robustness of its predictions. This is a Hollow Grid Mask image augmentation implementation in Python that is can be accepted as a `preprocessing_function` argument in `ImageDataGenerator` class of Tensorflow Keras.

## Demonstration
`tessel = 'odd'`
`hollow = True`

<img src=".\public\demo1_tesselodd_hollowTrue.jpg" width="480px">

`tessel = 'random'`
`hollow = True`

<img src=".\public\demo1_tesselrandom_hollowTrue.jpg" width="480px">

`tessel = 'odd'`
`hollow = False`

<img src=".\public\demo1_tesselodd_hollowFalse.jpg" width="480px">

## Usage
#### ImageDataGenerator Class
Pass the getHollowGridMask function to the `preprocessing_function` of `ImageDataGenerator` class.

```
from hollowGridMask import getHollowGridMask

train_datagen = ImageDataGenerator(...
                                   preprocessing_function = getHollowGridMask(tessel='random', p=0.66))
```
#### Use as a function
```
from hollowGridMask import getHollowGridMask
masked_image = getHollowGridMask(image)
```

## Arguments
```
Parameters
    ----------
    tessel : str, optional
        The type of grid tessellation. 'even': even grids will be choosen. 'odd': odd grids will be choosen. 'random': toggles between even or odd grid for each image. The default is 'odd'.
    p : float, optional
        The probability that hollow grid mask is applied. The default is 0.5.
    tessel_p : float, optional
        The probability selecting 'odd' grid mask in 'random' mode. The default is 0.5.
    hollow : boolean, optional
        To activate or disable hollow or full grid mask. The default is True.
    s_l : float, optional
        The lower bound ratio of each grid square wrt the passed image. The default is 0.01.
    s_h : float, optional
        The upper bound ratio of each grid square wrt the passed image. The default is 0.05.
    v_l : int, optional
        Lower greyscale tone of the grid mask. The default is 0.
    v_h : int, optional
        Upper greyscale tone of the grid mask. The default is 255.
```
    Returns
    -------
    3D numpy array
        Image.

#### Authors
- [Leebond](https://github.com/leebond)
- [lawchekun](https://github.com/lawchekun)
- [dexterch](https://github.com/dexterch)
- [Noonteo](noontwm@gmail.com)
