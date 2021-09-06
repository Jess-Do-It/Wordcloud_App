from flask import * 
from word_design import create_word_cloud
app = Flask(__name__,
            static_url_path='/images', 
            static_folder='images')  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['txt_file']  
        f.save('text/temp_words.txt')
        create_word_cloud('text/temp_words.txt')  
        return render_template("success.html", name = f.filename)  
  
#if __name__ == '__main__':  
 #   app.run(debug = True)  
