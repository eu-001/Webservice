from flask import Flask, render_template, url_for, request,json

app = Flask(__name__)
tardata = {"이름":"홍길동","나이":20}
@app.route("/examp")
def examp():
    return render_template("test.html")
@app.route("/responsejson")
def repjson():
    jtardata = json.jsonify(tardata) #dict -> json 문자화
    return jtardata

@app.route("/")
def hello_world():
    return "<p>Hello, Phthon!</p>"
@app.route("/aaa")
def aaa():
    return "<p>AAA 페이지에 접속함</p>"
@app.route("/bbb")
def bbb():
    return "<p> bbb 페이지에 접속함</p>"
# 웹페이지 서비스
@app.route("/mypage")
def mmm():
    return render_template("mytest.html")
@app.route("/service/")
@app.route("/service/<name>")
def service(name="인공지능"):
    return f"다음 파라미터를 주소로 전송하였네요:{name}"
@app.route("/paramservice/<param>")
def paramservice(param):
    return render_template('param.html',person=param)
#post, get 방식 전송 데이터 수신
@app.route("/login",methods=["post","get"])
def login():
    if request.method=="POST":
        print("포스트 전송")
        print(request.form["username"])
        print(request.form["userpw"])
    else:
        print("겟방식의 전송")
    return (f"보내신 아이디는 {request.form['username']}\
            비밀번호는 {request.form['userpw']}") if request.method=="POST"  else\
            f"겟방식으로 전송 하였네요{request.args.get('username','anony')}"
app.run("127.0.0.1",8888,True)


