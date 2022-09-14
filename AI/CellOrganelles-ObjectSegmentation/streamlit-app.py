

# Packages required for Streamlit web app and Image fetching
import streamlit as st
# import requests

# Stardist packages
from stardist.models import StarDist2D
from csbdeep.utils import normalize
import matplotlib.pyplot as plt
from skimage import io


# To predict the image
def predict(image1):
    he_model = StarDist2D.from_pretrained('2D_versatile_he')
    he_img = io.imread(image1)
    he_labels, _ = he_model.predict_instances(normalize(he_img))

    return he_labels


st.title("Image segmentation and organelles detection using Stardist pretrained Model")
st.write("Using Stardist pretrained Model to detect objects")

st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

if image_file is not None:
    # To See details
    file_details = {"filename": image_file.name, "filetype": image_file.type,
                    "filesize": image_file.size}
    # st.write(file_details)

    # To View Uploaded Image
    image = image_file

st.image(image)
classify_and_localize = st.button("Submit")
if classify_and_localize:
    st.write("")
    # To classify object in image
    label_img = predict(image)

    # To draw boundbox
    plt.axis('off')
    plt.imshow(label_img)
    # bbox, label, conf = cv.detect_common_objects(im)
    # output_image = draw_bbox(im, bbox, label, conf)
    plt.savefig('x.png')
    st.image('x.png')

else:
    st.write("Issue with file type")
