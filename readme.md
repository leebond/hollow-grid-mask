# Hollow Grid Mask
## Description
Image augmentation is preprocessing step done prior of network training to improve the robustness of its predictions. This is a Hollow Grid Mask image augmentation implementation in Python that is can be accepted as a `preprocessing_function=` argument in `ImageDataGenerator` class of Tensorflow Keras.

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
