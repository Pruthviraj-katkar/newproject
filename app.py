from flask import Flask,jsonify,render_template
import psutil
app=Flask(__name__)

@app.route("/hello",methods=["GET"])
def Hellomsg():
    return jsonify({"msg":"Hello User"})

@app.route("/",methods=["GET"])
def welcome():
    return "Hello User"

@app.route("/ping",methods=["GET"])
def ping():
    return "200 OK"


@app.route("/healthz",methods=["GET"])
def Helalth():
    cpu_percentage=psutil.cpu_percent()
    memory_info=psutil.virtual_memory()
    return render_template("index.html",cpu_percent=cpu_percentage,memory_percent=memory_info.percent)

if __name__=="__main__":
    app.run(debug=True)