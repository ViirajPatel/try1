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
        imagefile = request.files['image']
        typeofsoil = request.form.get('soiltype').split(".")[1]
        print(typeofsoil)
        img = io.imread(imagefile)
        lab = color.rgb2lab(img)
        lightness_avg = average(lab[0])
        if(typeofsoil=="mid"):
            organic_c = 10.44-0.1998*lightness_avg
        elif(typeofsoil=="coarse"):
            organic_c= 9.16-0.163 * lightness_avg
        else:
            organic_c = 7.241 - 0.1342 * lightness_avg

        print(organic_c)
        val = {
            'message':str(organic_c)
        }
        return dumps(val)

if __name__ == "__main__":
    app.run(debug=False,port='8000')