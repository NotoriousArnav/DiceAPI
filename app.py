from flask import Flask, redirect, request
import base64
import random
import os

die_faces = {}

app=Flask(__name__)

for i in os.listdir('media'):
    if "_die.jpg" in i:
        with open(f'media/{i}','rb') as f:
            die_faces[i.replace("_die.jpg", '')]=base64.b64encode(f.read()).decode()

@app.get('/rolladie')
def rolladie():
    global die_faces
    number = random.choice(list(range(1,6+1)))
    die_face = die_faces[str(number)]
    base64_url=f"data:image/jpg;base64,{die_face}"
    return redirect(base64_url)



@app.get('/rolladie/json')
def rolladie_json():
    global die_faces
    number = random.choice(list(range(1,6+1)))
    die_face = die_faces[str(number)]
    base64_url=f"data:image/jpg;base64,{die_face}"
    return {'number':number, 'image':base64_url}


if __name__ == "__main__":
    app.run()
