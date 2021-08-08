from flask import Flask, config, render_template, request, send_from_directory
from os import remove, listdir, getcwd
from random import choices
from string import ascii_letters, digits


def CreateFileName(FileExtintion) -> str:
    '''
    @@ first thing the function will check it " how many files on directory "
        - You can change the limit of files before auto remove.
        - You can disable this feature by comment it #.
    '''
    limit = 50 
    PATH = getcwd() + '/tmp/'
    FilesOnDir = listdir(PATH) 

    if len(FilesOnDir) > limit:
        for File in FilesOnDir:
            remove(PATH + File)

    return ''.join(choices(ascii_letters + digits, k=4)) + '.' + FileExtintion


app = Flask(__name__, template_folder='template')
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        FileExtintion = file.filename.split('.')[-1] if file.filename.split('.')[-1].isalpha() else ''     # // .jpg, .txt, .pdf, ...Etc 
        FileName = CreateFileName(FileExtintion)
        file.save('tmp/' + FileName)

        url = request.url_root + FileName
        return f'<pre> Access your file here: <a href="{url}">{url}</a></pre>'
    
    return render_template('index.html')


@app.route('/<filename>', methods=['GET'])
def tmp(filename):
    if request.method == 'GET':
        return send_from_directory('tmp/', filename)

if __name__ == '__main__':
    app.run()
