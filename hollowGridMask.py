# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:29:49 2020

@author: guanhua
"""
import numpy as np

def getHollowGridMask(tessel = 'odd', p=0.5, tessel_p = 0.5, hollow = True, s_l=0.01, s_h=0.05, v_l=0, v_h=255):
    '''
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

    Returns
    -------
    3D numpy array
        Image.

    '''
    def HollowGridMask(image):
        def cartesian(arrays, out=None):
            '''
            source: https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/extmath.py
            '''
            arrays = [np.asarray(x) for x in arrays]
            shape = (len(x) for x in arrays)
            dtype = arrays[0].dtype

            ix = np.indices(shape)
            ix = ix.reshape(len(arrays), -1).T

            if out is None:
                out = np.empty_like(ix, dtype=dtype)

            for n, arr in enumerate(arrays):
                out[:, n] = arrays[n][ix[:, n]]

            return out

        img_h, img_w, img_c = image.shape
        p_1 = np.random.rand()
        if p_1 > p:
            return image

        # get grid squares relative to the size of the image
        relative_square_pixel_area = np.random.uniform(s_l, s_h) * img_h * img_w
        # get the side of a grid square
        relative_square_side = np.ceil(np.sqrt(relative_square_pixel_area))
        # randomly choose a H and W origin to start the grid squares
        h_origin = np.random.randint(0, img_h//10)
        w_origin = np.random.randint(0, img_w//10)
        # determine the locations of all grid squares also stop before it bleeds out of the image
        h_marks = np.arange(h_origin, img_h - relative_square_side, relative_square_side)
        w_marks = np.arange(w_origin, img_w - relative_square_side, relative_square_side)

        # to toggle between alternating grid patterns
        def getGridTesselPattern(tessel):
            if tessel == 'odd':
                result = cartesian((w_marks[0::2], h_marks[0::2]))
                res = result.copy()
                return res
            elif tessel == 'even':
                result = cartesian((w_marks[1::2], h_marks[1::2]))
                res = result.copy()
                return res
            elif tessel == 'random': # random for each image
                if np.random.rand() > tessel_p:
                    return getGridTesselPattern('odd')
                else:
                    return getGridTesselPattern('even')

        res = getGridTesselPattern(tessel)
        res_end = res + relative_square_side

        color = np.random.uniform(v_l, v_h)

        if hollow:
            first_w = res_end[0][0].copy()
            first_h = res_end[0][1].copy()
            last_w = res_end[len(res_end)-1][0].copy()
            last_h = res_end[len(res_end)-1][1].copy()
            for i in range(0, res.shape[0]):
                if int(res_end[i][0]) <= first_w or int(res_end[i][1]) <= first_h or\
                int(res_end[i][0]) >= last_w or int(res_end[i][1]) >= last_h:
                    image[int(res[i][0]):int(res_end[i][0]), int(res[i][1]):int(res_end[i][1]), :] = color
            return image
        else:
            for i in range(0, res.shape[0]):
                image[int(res[i][0]):int(res_end[i][0]), int(res[i][1]):int(res_end[i][1]), :] = color
            return image
    return HollowGridMask