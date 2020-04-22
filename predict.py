
from tensorflow.keras.models import load_model
from keras.preprocessing import image
import numpy as np

# In[18]:

model=load_model('animalopediamodel.h5')
model._make_predict_function()
def preprocess(img):
    img=image.load_img(img,target_size=(224,224))
    img=image.img_to_array(img)
    img= np.expand_dims(img, axis=0)
    return img


def prediction(img):
    img=preprocess(img)
    value=model.predict(img)
    prediction=np.argmax(value[0])
    class2animal={0:"Reindeer",1:"Elephant",2:"Ant",3:"Crocodile",4:"Penguin",5:"Wolf",6:"Tiger",7:"Parrot"}
    return class2animal[prediction]

