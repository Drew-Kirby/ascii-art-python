from flask import Flask, render_template, request
from PIL import UnidentifiedImageError

from ascii_converter import generateAscii

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

@app.route('/', methods=["GET", "POST"])
def hello():
    ascii_art = None
    error = None

    if request.method == "POST":
        uploaded_image = request.files.get("image")

        if uploaded_image is None or uploaded_image.filename == "":
            error = "Please select an image."
        else:
            try: 
                ascii_art = generateAscii(uploaded_image)
            except UnidentifiedImageError:
                error = "The selected file is not a valid image."
            except OSError:
                error = "The image could not be processed."

    return render_template('index.html', output=ascii_art, error=error) 

if __name__ == "__main__":
    app.run(debug=True)