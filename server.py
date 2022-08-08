from skimage import io, color
import numpy as np

import json
from flask import Flask,  request
from werkzeug.serving import WSGIRequestHandler
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello!!"
@app.route('/upload', methods=['POST'])
def upload():
    if(request.method=="POST"):
        imagefile = request.files['image']
       
        # npimg = np.fromstring(imagefile, np.uint8)
       
        # img = imdecode(npimg, IMREAD_UNCHANGED)
        img = io.imread(imagefile)
        lab = color.rgb2lab(img)
        lightness_avg = np.average(lab[0])
        organic_c = 10.44-0.1998*lightness_avg
        print(organic_c)
        val = {
            'message':str(organic_c)
        }
        return json.dumps(val)

if __name__ == "__main__":
    app.run(debug=False,port='8000')



