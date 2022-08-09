from skimage import io, color
from numpy import average
from json import dumps
from flask import Flask,  request
from werkzeug.serving import WSGIRequestHandler
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Viraj...!!!"
@app.route('/upload', methods=['POST'])
def upload():
    if(request.method=="POST"):
        print(request.content_length)
        lightness_avg = average(color.rgb2lab(io.imread(request.files['image']))[0])
        organic_c = 10.44-0.1998*lightness_avg
        print(organic_c)
        val = {
            'message':str(organic_c)
        }
        return dumps(val)

if __name__ == "__main__":
    app.run(debug=False,port='8000')