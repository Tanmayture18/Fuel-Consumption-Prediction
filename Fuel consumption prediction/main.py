from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
file=open('model.pk1','rb')
rr=pickle.load(file)
file.close()
@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        mydict=request.form
        # cylinders,Displacement,Weight,Acceleration,Model Year,Origin,
        Cylinders=int(mydict['Cylinders'])
        Displacement=int(mydict['Displacement'])
        Weight=int(mydict['Weight'])
        Acceleration=int(mydict['Acceleration'])
        Model_Year=int(mydict['Model Year'])
        Origin=int(mydict['Origin'])

        inputfeatures=[Cylinders,Displacement,Weight,Acceleration,Model_Year,Origin]

        Pred=rr.predict([inputfeatures])
        for i in Pred:
            pred=i
        print(pred)

        return render_template('show.html',inf=pred)
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True)  