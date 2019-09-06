from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
    <html>
        <style>
            form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
            }}
            text area {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
        <label for="rot">Rotate by: </label>
        <input type="text" id="rot" name="rot" value="0" />
        <p>
        <textarea name="text" rows="10" cols="85">{0}</textarea>
        </p>
        <br>
        <input type="submit" />
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def ecrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    rotated = rotate_string(text, rot)
    return form.format(rotated)

app.run()