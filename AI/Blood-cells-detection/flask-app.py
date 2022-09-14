from flask import Flask, render_template, request
from keras.models import load_model
from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
import numpy as np


app = Flask(__name__)


# model.make_predict_function()


def predict_label(img_path):
    model = load_model('model_3.h5')
    image = load_img(img_path, target_size=(240, 320))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    # image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # Expand dimentions only for vgg
    image = np.expand_dims(image, axis=0)
    # prepare the image for the VGG model only
    # image = preprocess_input(image)
    # predict the probability across all output classes
    label = model.predict(image)
    print(label)
    label_list = []
    if label[0][0] == 1:
        result_0 = 'Eosinophil'
        label_list.append(result_0)
    if label[0][1] == 1:
        result_1 = 'Lymphocyte'
        label_list.append(result_1)
    if label[0][2] == 1:
        result_2 = 'Monocyte'
        label_list.append(result_2)

    if label[0][3] == 1:
        result_3 = 'Neutrophil'
        label_list.append(result_3)
    return label_list


# Flask
# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return "Please subscribe  Artificial Intelligence Hub..!!!"


@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)

        pr = predict_label(img_path)
        for i in pr:
            print(i)

    return render_template("index.html", prediction=pr, img_path=img_path)


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
