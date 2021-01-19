from flask import Flask
from flask import request

# simdi app olusturacagiz

app= Flask(__name__)   #flaskin kendisini cagirip app diye birsey üzerine atiyoruz

# http://127.0.0.1:5000/home -> bu bizim base Url. Sagina ne yazacagimizi @app. kisminda belirleniyor

#API dedigimiz bazi entpointler olusturacagiz. /user, /home, /test, /bost..

@app.route('/home') #route yönlendirme oluyor. Yani API sitemin su kismina yönlendiriyoruz. home olmali
def index():  #index adi önemli degil ama anlasilmasi icin önemli. Bu fonksiyonu modeli deploy etmek icin kullanacagiz
    return 'Hello Flask'

@app.route('/users/<user_id>', methods=['GET','POST','PUT','DELETE']) #parantez icine dinamik bir user_id gelecek. Biz database den bu id ile ilgili verileri cekebiliriz
def parameter(user_id):
    if request.method=='GET':
        return 'GET method'
    elif request.method=='POST':
        data = request.form
        return data
    elif request.method=='PUT':
        return 'Put method'
    elif request.method=='DELETE':
        return 'Delete method'
    else:
        return 'Method not Allowed'


    return user_id
app.run()  #0.0.0.0 local host demek. 81 kullanilmayan bir porttur. normalde home=0.0.0.0 parantez icinde yaziliyor.


