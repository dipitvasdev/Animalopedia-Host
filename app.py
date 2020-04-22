from flask import Flask,render_template,redirect,request

from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# In[18]:

model=load_model('animaleye.h5')
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


app=Flask(__name__)
@app.route('/')
def hello():
	return render_template("index.html")
@app.route('/',methods=['POST'])
def submit():
	if request.method=='POST':
		f=request.files['image'] 
		path = "{}".format(f.filename)
		prediction = predict.prediction(path)
		return render_template("index.html",your_result=prediction)
if __name__=='__main__':
	app.run(debug = True )