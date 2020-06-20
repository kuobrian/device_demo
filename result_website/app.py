from flask import Flask, render_template
import os
import time

RESLUTS_FOLDER = "./static"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = RESLUTS_FOLDER


# @app.route('/index')
@app.route('/')
def show_index():
    result_files = os.listdir(os.path.join(RESLUTS_FOLDER, "results"))
    # print(result_files)

    # image_paths = [os.path.join(app.config['UPLOAD_FOLDER'], 'a.jpg')]

    
    full_filename = [os.path.join(app.config['UPLOAD_FOLDER'], "results", r) for r in result_files]

    result_array = [r.split(".")[0] + " , " + "EFG-456" for r in result_files]

    results_time = [time.ctime(os.path.getmtime(f)) for f in full_filename]

    print(results_time)

    return render_template("index.html", result_time =results_time, result_array = result_array, image_name = full_filename)
    # return "ok"

@app.route('/test')
def show_image():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'a.jpg')
    print(full_filename)
    return render_template("test.html", r1 = full_filename)

if __name__ == "__main__":
    app.debug = True
    app.run() 