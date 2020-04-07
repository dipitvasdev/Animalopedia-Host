from flask import Flask,render_template,redirect,request
import predict
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
		prediction = predict.prediction(path)
		return render_template("index.html",your_result=prediction)
if __name__=='__main__':
	app.run(debug = True )