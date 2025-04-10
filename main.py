import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
from PIL import Image as PILImage
from io import BytesIO
import sys
from IPython.display import Image, display

import cv2

model = load_model('inceptionv3f.weights.h5')

def preprocess_imagefromfile(image):
    # response = requests.get(image_url)
    # img = Image.open(BytesIO(response.content))
#     image=cv2.imread(image_path)
#     if image is not None:
#       img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = image.resize((299, 299))
        img_array=np.array(img)
        img_array=img_array.astype('float64')
        img_array = np.expand_dims(img_array, axis=0)
        img_array=img_array[...,:3]
        img_array /= 255.0
        return img_array
#     else:
#         print("No file Found try to relocate the file in the same source folder to get the results")
#         return


def predict_imagefromfile(image):
#     if image is not None:
        img_array = preprocess_imagefromfile(image)
#         if img_array is not None:
        prediction = model.predict(img_array)
        label = 1 if prediction[0] > 0.5 else 0
        return label,prediction[0]
#         else:
#             print("No file Found try to relocate the file in the same source folder to get the results")
#             return 2, 0.00
#     else:
#         print("No file Found try to relocate the file in the same source folder to get the results")
#         return 2, 0.00

def preprocess_image(image_url):
    response = requests.get(image_url)
    img = PILImage.open(BytesIO(response.content))
    # image=cv2.imread(image)
    img = img.resize((299, 299))
    img_array = np.array(img)
    img_array=img_array.astype('float64')
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    return img_array


def predict_image(image):
    img_array = preprocess_image(image)
    prediction = model.predict(img_array)
    label = 1 if prediction[0] > 0.5 else 0

    return label,prediction[0]

def final_resultURL(image_url):
#     image_url = 'https://cdn.pixabay.com/photo/2024/04/13/10/20/peacock-8693634_1280.jpg' #enter url here
    result,p = predict_image(image_url)
    if result==1:
        print('real')
    else:
        print('fake')
    print('probability of real_image is ',p.item())
    
def final_resultPath():
    image_path = 'img1- (30).jpg' #enter url here
    image=cv2.imread(image_path)
    result,p = predict_imagefromfile(image)
    if result==1:
        print('real')
    else:
        print('fake')
    print('probability of real_image is ',p.item())