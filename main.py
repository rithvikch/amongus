from flask import Flask, render_template, redirect, url_for, request, flash
from random import randint




app = Flask(__name__)

@app.route("/home")
@app.route("/", methods = ['POST','GET'])
def home():
    
    if request.method == "POST":
        players = request.form['play']
        imposters = request.form['imp']
        print(imposters)
        players = int(players)
        imposters = int(imposters)
        imps = []
        for i in range(imposters):
            impo = randint(1,players)
            if (impo not in imps):
                imps.append(impo)
        
        
        listo = []
        for i in range(1, players+1):
           if i in imps:
                listo.append(True)
           else:
                listo.append(False)
            
        print(listo)
        return render_template("index.html", content = listo)
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run()

