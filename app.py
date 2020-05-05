from flask import Flask,render_template,redirect,request
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

def predict2(path):
	np.set_printoptions(suppress=True)
	model = tensorflow.keras.models.load_model('keras_model.h5')
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
	image = Image.open(path)
	size = (224, 224)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)
	image_array = np.asarray(image)
	image.show()
	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
	data[0] = normalized_image_array
	prediction = model.predict(data)
	return prediction
app=Flask(__name__)
@app.route('/')
def hello():
	return render_template("index.html")
@app.route('/',methods=['POST'])
def submit():
	if request.method=='POST':
		f=request.files['image'] 
		path = "{}".format(f.filename)
		f.save(path)
		animal=predict2(path)
		animal2=np.argmax(animal)
		class2animal={0:"Ant",1:"Crocodile",2:"Elephant",3:"Parrot",4:"Penguin",5:"Reindeer",6:"Tiger",7:"Wolf"}
		return render_template("index.html",your_result=class2animal[animal2])
if __name__=='__main__':
	app.run(debug = True )