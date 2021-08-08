# Simple Flask ( Upload files )
- `curl -F 'file=@PATH/to/filename' 127.0.0.1:5000`<br>
- `echo "Test" | curl -F "file=@-;filename=.txt" 127.0.0.1:5000`
- `index.html`
```html
<form action="" method="post" enctype="multipart/form-data">
        <input type='file' name='file'>
        <input type='submit' value='Submit'>
</form>
```

# About APP
- `Random name of file .`<br>
- `Safe`<br>
- `The maximum allowed file size is 30 MB .`  #   you can change it if you want .
```python
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024
```
- `Remove files automatically after catch limit files on directory [ default  = 50 ] .`  #   you can change it if you want .
```python
limit = 50 
    PATH = getcwd() + '/tmp/'
    FilesOnDir = listdir(PATH) 

    if len(FilesOnDir) > limit:
        for File in FilesOnDir:
            remove(PATH + File)
```

# How to start
  - Install virtualenv using pip3 :<br>
    `pip3 install virtualenv`<br>
    
  - Create virtualenv :<br>
    `python3 -m venv UploadApp`<br>
  
  - Active your virtual environment :<br>
    `source UploadApp/bin/activate`<br>
  
  - Install Flask within the activated environment :<br>
    `pip3 install flask`<br>
  
  - Set the `FLASK_APP` environment variable :<br>
    `export FLASK_APP = 'APP.py' `<br>
  
  - Run the Flask application :<br>
    `flask run`
