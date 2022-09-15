## Object Segmentation web app
This is an object segmentation model for detecting organelles and some other objects from medical images using a pre-trained model called StarDist

## *StarDist Library*
![](https://github.com/stardist/stardist/raw/master/images/stardist_overview.png)

### Quick look

The following figure illustrates the general approach for 2D images. The training data consists of corresponding pairs of input (i.e. raw) images and fully annotated label images (i.e. every pixel is labeled with a unique object id or 0 for background).
A model is trained to densely predict the distances (r) to the object boundary along a fixed set of rays and object probabilities (d), which together produce an overcomplete set of candidate polygons for a given input image. The final result is obtained via non-maximum suppression (NMS) of these candidates.

![](https://github.com/stardist/stardist/raw/master/images/overview_2d.png)

The approach for 3D volumes is similar to the one described for 2D, using pairs of input and fully annotated label volumes as training data.

![](https://github.com/stardist/stardist/raw/master/images/overview_3d.png)

## Our App
To use our app:
- install streamlit library
- Open the terminal and go to the directory where your model file is in , then write "streamlit run 'file-name.py' "
- Upload the image you want to test from your local device
 -- Note : the image should be a pathology image for tissues
- click on the submit button

![](https://github.com/DevMed22/Summer-training-22/blob/main/AI/CellOrganelles-ObjectSegmentation/images/star.png)

### Thanks for your time 😊

## Resources
[StarDist](https://github.com/stardist/stardist)

