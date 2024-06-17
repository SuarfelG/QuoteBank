from flask import  Blueprint , render_template , request ,flash ,redirect,url_for
from .models import Quotes,Authentication
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required , login_user ,logout_user


view = Blueprint("view",__name__)
@view.route("/")
def Home():
       logout_user()
       return render_template("auth.html")



@view.route("/searchkey",methods=["POST","GET"])
@login_required
def SearchQuoteByKeyWord():
       if request.method=="POST":
              keyword=request.form.get("Keyword")
              quot=Quotes.query.all()  
              for x in quot:
                 if keyword.lower() in (x.Quote).lower():
                        return render_template('base.html', Quote=x)
              flash("Quote Not Found" , category="error")
              return render_template("base.html")           

       return render_template("searchkey.html")


@view.route("/searchid",methods=["POST","GET"])
@login_required
def SearchQuoteById():
        if request.method=="POST":
                id=request.form.get("id")
                Quote = Quotes.query.filter_by(id=id).first()
                if Quote:
                        return render_template('base.html', Quote=Quote)
                else:
                        flash("Quote Not Found" , category="error")
                        return render_template("base.html")
        return render_template("searchId.html")


@view.route("/SeeAll")
@login_required
def SearchAll():
        quote=Quotes.query.all()
        return quote



@view.route("/login", methods=["POST","GET"])
def login():
        if request.method=="POST":
                Email=request.form.get("Email")
                Password=request.form.get("Password")
                EmailExist=Authentication.query.filter_by(Email=Email).first()
                if EmailExist:
                       if check_password_hash (EmailExist.password,Password):
                              flash("Logged In Successfuly", category="success")
                              login_user(EmailExist)
                              return redirect (url_for("view.SearchQuoteByKeyWord"))
                       else:
                              flash("Passwords Don't Match", category="error")
                              return render_template("login.html")

        return render_template("login.html")

@view.route("/signup", methods=["POST","GET"])
def signup():
    if request.method=="POST":
        Name=request.form.get("Name")
        Father_Name=request.form.get("Father")
        Email=request.form.get("Email")
        Password=request.form.get("Password")
        
        EmailExist=Authentication.query.filter_by(Email=Email).first()

        if(EmailExist):
                flash("Email Exist" , category="error")
        elif (len(Name)<4):
                flash("Name is too short" , category="error")
        elif (len(Father_Name)<4):
                flash("Father_Name is too short" , category="error")
        elif(len(Email)<4):
                flash("Email is too short" , category="error")
        elif(len(Password)<4):
                flash("Password is too short" , category="error")
        else:
                NewUser=Authentication(First_name=Name,Last_name=Father_Name,Email=Email,password=generate_password_hash(Password))
                db.session.add(NewUser)
                db.session.commit()
                flash("Signed in Successfuly" , category="success")
                login_user(NewUser)

                return redirect (url_for("view.SearchQuoteById"))
        
        
    return render_template("signup.html")
