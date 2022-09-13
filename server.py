from skimage import io, color
from numpy import average
from json import dumps
from flask import Flask,  request
from werkzeug.serving import WSGIRequestHandler
app = Flask(__name__)  # Flask server code


@app.route('/')
def home():
    return "Hello from Viraj...!!!"
@app.route('/upload', methods=['POST']) # Routing for flask server 
def upload():
    if(request.method=="POST"):
        imagefile = request.files['image']  # Getting selected image from request sent by mobile application 
        typeofsoil = request.form.get('soiltype').split(".")[1]  # Getting selected soiltype from request sent by mobile application 

        img = io.imread(imagefile) # Reading image
        lab = color.rgb2lab(img)   # Converting RGB to LAB
        lightness_avg = average(lab[0]) # Average of LAB image's pixel's value
        if(typeofsoil=="mid"): 
            organic_c = 10.44-0.1998*lightness_avg # If soiltype is medium than oraganic_c's value = 10.44-0.1998*lightness
        elif(typeofsoil=="coarse"):
            organic_c= 9.16-0.163 * lightness_avg # If soiltype is Coarse than oraganic_c's value = 9.16 – 0.163* Lightness
        else:
            organic_c = 7.241 - 0.1342 * lightness_avg  # If soiltype is Fine than oraganic_c's value = 7.241 – 0.1342 * Lightness

        print(organic_c)
        val = {
            'message':str(organic_c) # Generating JSON for sending output to mobile.
        }
        return dumps(val) #Sending organic carbon value to mobile.

if __name__ == "__main__":                  # Flask server code
    app.run(debug=False,port='8000')