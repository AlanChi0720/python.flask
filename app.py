from flask import Flask
from flask import request #載入request物件
from flask import redirect
from flask import render_template
from flask import session
import json

app = Flask(
    __name__,
    static_folder = "public" , # 靜態檔案資料夾名稱(可以自己決定)
    static_url_path= "/youdecide" # 靜態檔案對應網址路徑(可以自己決定)
) 
# 要使用session 要先設定session 密碼
app.secret_key= "any string but secret"
# __name__ 代表執行的模組
# 建立app 物件, 可以設定靜態檔案的路徑處理
# 所有在static 資料夾， 都對應到 "/youdecide/檔案名稱" #可空白 = "/"

# 使用GET方法 建立路徑 / 對應的處裡函式
@app.route("/" , methods= ['GET']) # 函式的裝飾(decortor): 以函式為基礎，提供附加功能
def home():
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好" , request.headers.get("accept-language"))
    # print("引薦網址" , request.headers.get("referrer"))
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        # return redirect("/en/")
        return json.dumps({
            "status":"ok",
            "text":"Hello Flask"
        })
    else: # json.dumps()把字典轉換成json格式的字串 # 新版flask可直接轉換dic to JSON
        # return redirect("/zh/")
        # return json.dumps({
        #     "status":"ok",
        #     "text":"你好 Flask"
        # }, ensure_ascii=False) # 指示"不要用" ASCII 編碼處理中文
        # return render_template("index", name="Alan")
        return render_template("index.html")

# 使用GET 方法處理路徑 /hello
@app.route("/hello", methods= ["GET"])
def hello():
    name = request.args.get("name","")
    session["username"] = name #session["欄位名稱"]=資料
    return "你好, "+name

# 使用GET 方法處理路徑 /talk
@app.route("/talk", methods=["GET"])
def talk():
    name = session["username"] # 從session取出資料
    return "來聊聊吧, " +name

# 處理路降 /page
@app.route("/page")
def page():
    return render_template("page.html" ,name="alan")

# 處理路徑 /submited 的對應函式
@app.route("/submited", methods=["POST"])
def submited():
    # inputname= request.args.get("n", "") 
    inputname= request.form["n"]
    return "恭喜你 "+str(inputname)

# @app.route("/en/")
# def index_english():
#     return json.dumps({
#         "status":"ok",
#          "text":"Hello Flask"
#     })
# @app.route("/zh/")
# def index_chinese():
#     return json.dumps({
#             "status":"ok",
#             "text":"你好 Flask"
#     }, ensure_ascii=False)

# 使用GET方法 利用要求字串 (Query String) 提供彈性 :/getSum?min=最小值&max=最待數字
@app.route("/getSum", methods=["POST"])
def getsum(): # min + (min+1)+....+ max
    # 接收GET 方法的Queryt String
    # inputmax= request.args.get("maxnum", "") 
    # inputmin= request.args.get("minnum", "") 
    # max = request.args.get("max", 100)
    # min = request.args.get("min", 1)
    # 接收POST 方法的Queryt String
    inputmax= request.form["maxnum"]
    inputmin= request.form["minnum"]
    # maxnum = int(max)
    # minnum = int(min)
    maxnum= int(inputmax)
    minnum= int(inputmin)
    result = 0
    if maxnum >minnum:
        for i in range(minnum,maxnum +1):
            result += i
    else:
        for i in range(maxnum,minnum +1):
            result += i
    return render_template("result.html", data=result)

# 建立路徑 /test 對應的處裡函式
@app.route("/test") #代表處理的網站路徑
def test():
    return redirect("https://www.google.com/") # 重新導向到 "/en/" 的路徑 or 指定url

# 建立動態路由 /user/使用者名稱 對應的處裡函式
@app.route("/user/<username>")
def handleuser(username):
    if username == "alan":
        return "Hello 大帥哥 " + username
    else:
        return "Hello " + username
 
if __name__ == "__main__": #如果以主程式執行
    app.run(port=3000) #立刻啟動伺服器, 可透過 port參數 指定埠號