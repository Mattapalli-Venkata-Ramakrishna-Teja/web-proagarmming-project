from email.utils import decode_rfc2231
from pickle import TRUE
from tokenize import group
from turtle import onclick
from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.models import Addstock
from app.models import Addbuyer
from flask import request, redirect, url_for
from datetime import date, datetime


s=0
@app.route('/')
@app.route('/index')
def index():
    list= Addstock.query.all()
    return render_template('index.html',list=list)

@app.route("/add_item", methods=['GET'])
def get_add_item():
    return render_template('add_item.html')

@app.route("/add_item", methods=['POST'])
def post_addstock():
    tabname1 = request.form.get("tabname", "<missing tabame>")
    company1=  request.form.get("company", "<missing company>")
    doe1=request.form.get("doe","<missing doe>")
    doe2=datetime.strptime(doe1, '%Y-%m-%d').date()
    u = Addstock(tabname=tabname1,company=company1,doe=doe2)
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete",methods=['GET'])
def get_delete_item():
    return render_template('delete.html')

@app.route("/delete",methods=['POST'])
def post_delete():
    id=request.form.get("delete","<missing delete>")
    print(id)
    u=Addstock.query.get(int(id))
    if u:
        db.session.delete(u)
        db.session.commit()
        return render_template('delete.html',submitted='submitted')
    else:
        return '<html><p>Item not found</p></html>'
@app.route("/expires")
def expires():
    t = datetime.today()
    expires=Addstock.query.filter(Addstock.doe<=t)
    return render_template('expires.html',expires=expires)

@app.route("/update", methods=['GET'])
def get_update():
    return render_template('update.html')


@app.route("/update", methods=['POST'])
def update():
    item={}
    id=request.form.get("update","<missing update>")
    u=Addstock.query.get(int(id))
    item=Addstock.query.filter(Addstock.id==int(id))
    if u:
        for item in item:
            print(item.tabname)
        return render_template('update_item.html',submitted='submitted',item=item )
    else:
        return '<html><p>Item not found</p></html>'

@app.route("/update_item", methods=['POST'])
def post_update():
    id=request.form.get("id", "<missing tabame>")
    tabname1 = request.form.get("tabname", "<missing tabame>")
    company1=  request.form.get("company", "<missing company>")
    doe1=request.form.get("doe","<missing doe>")
    doe2=datetime.strptime(doe1, '%Y-%m-%d').date()
    u = Addstock.query.get(int(id))
    u.tabname=tabname1
    u.company=company1
    u.doe=doe2
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/addbuyer", methods=['GET'])
def get_addbuyer():
    return render_template('addbuyer.html')

@app.route("/addbuyer", methods=['POST'])
def post_addbuyer():
    Name = request.form.get("name", "<missing name>")
    Amount= request.form.get("amount", "<missing tabame>")
    status1=request.form.get("status","<missing status")
    if status1=='on':
        status1=1
    else:
        status1=0

    date1=request.form.get("date","<missing date>")
    date2=datetime.strptime(date1, '%Y-%m-%d').date()
    u = Addbuyer(name=Name,amount=int(Amount),status=status1,date=date2)
    db.session.add(u)
    db.session.commit()
    return render_template('addbuyer.html',submitted='submitted')

@app.route("/dues")
def dues():
    tran1=Addbuyer.query.filter(Addbuyer.status==0)
    return render_template('dues.html',tran=tran1)












