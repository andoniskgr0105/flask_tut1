from flask import Flask, render_template, redirect, url_for, request, send_from_directory, session, make_response
import handle_images as imgs
import main

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = './files'

app.secret_key = 'someKey'

IMAGES_FOLDER = './static/photos/wd/'

@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='GET':
        return render_template('login.html',title='Login Page')
    elif request.method=='POST':
        status=False
        username = request.form.get('usr').lower()
        password = request.form.get('pwd')
        if (username == 'tony' and password == '1234'):
            status=True
            return render_template('admin.html',login_status=status)
        else:
            return render_template('login.html',title='Login Page')
    
    
@app.route('/')
def index():
    return render_template('index.html', message='index page',title='Index Page')
        


@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    return "file ok"


@app.route('/gallery')
def gallery():
    thumb_photos=imgs.get_thumbnail_photos()
    return render_template('gallery.html', thumb_photos=thumb_photos, message='index page', title="My Gallery")


@app.route('/photos/<filename>')
def photos(filename):
    result = send_from_directory(IMAGES_FOLDER, filename)
    print('result',filename)
    return result

@app.route('/test')
def test():
    main.get_all_photos()
    return 'test'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
