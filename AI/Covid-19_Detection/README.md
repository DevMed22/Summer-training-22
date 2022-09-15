## Covid-19 Detection App
This is a flask app for Covid-19 Detection using VGG-16.

You can look at this [notebook](https://www.kaggle.com/code/ahmedtarek26/covid-19-detection-using-vgg-16)

## Quick look at VGG-16

VGG16 is a convolution neural net (CNN ) architecture which was used to win ILSVR(Imagenet) competition in 2014. 
It is considered to be one of the excellent vision model architecture till date. Most unique thing about VGG16 
is that instead of having a large number of hyper-parameter they focused on having convolution layers of 3x3 
filter with a stride 1 and always used same padding and maxpool layer of 2x2 filter of stride 2. 
It follows this arrangement of convolution and max pool layers consistently throughout the whole architecture. 
In the end it has 2 FC(fully connected layers) followed by a softmax for output. The 16 in VGG16 refers to it has 
16 layers that have weights. This network is a pretty large network and it has about 138 million (approx) parameters.

Very Deep Convolutional Networks for Large-Scale Image Recognition. [https://arxiv.org/abs/1409.1556]

![vgg16 architecture](https://user-images.githubusercontent.com/35737777/69682136-5bdd4780-10a8-11ea-9079-50283f5451df.png)

### Model structure

1. 2 x convolution layer of 64 channel of 3x3 kernal and same padding
2. 1 x maxpool layer of 2x2 pool size and stride 2x2
3. 2 x convolution layer of 128 channel of 3x3 kernal and same padding
4. 1 x maxpool layer of 2x2 pool size and stride 2x2
5. 3 x convolution layer of 256 channel of 3x3 kernal and same padding
6. 1 x maxpool layer of 2x2 pool size and stride 2x2
7. 3 x convolution layer of 512 channel of 3x3 kernal and same padding
8. 1 x maxpool layer of 2x2 pool size and stride 2x2
9. 3 x convolution layer of 512 channel of 3x3 kernal and same padding
10. 1 x maxpool layer of 2x2 pool size and stride 2x2

We have also add ReLU activation to each layers so that all the negative values are not passed to the next layer.

After creating all the convolution we pass the data to the dense layer:

11. 1 x Dense layer of 4096 units
12. 1 x Dense layer of 4096 units
13. 1 x Dense Softmax layer of 2 units


## To use the app :

- Open the notebook , train the model and download model file or download the model from this [link](https://drive.google.com/file/d/1yAddjEG6980R-Duy-awinmEt7FZxijTt/view?usp=sharing)

- open [flask-app](https://github.com/DevMed22/Summer-training-22/blob/main/AI/Covid-19_Detection/flask-app.py) file, then run the file or open the terminal and open the file then write 'flask run'


- Upload the figure you want to test from Upload your image


- Click on sumit button and wait seconds to see the results.

## Resources
[VGG-16 GitHub page](https://github.com/ashushekar/VGG16)
