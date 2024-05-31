from flask import  Blueprint , render_template , request ,flash ,redirect,url_for
from .models import Quotes

view = Blueprint("view",__name__)

@view.route("/searchkey",methods=["POST","GET"])
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


@view.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        Name=request.form.get("Name")
        Father_Name=request.form.get("Father")
        Email=request.form.get("Email")
        Password=request.form.get("Password")
        

        if (len(Name)<4):
                flash("Name is too short" , category="error")
        elif (len(Father_Name)<4):
                flash("Father_Name is too short" , category="error")
        elif(len(Email)<4):
                flash("Email is too short" , category="error")
        elif(len(Password)<4):
                flash("Password is too short" , category="error")
        else:
                flash("Signed in Successfuly" , category="success")
                return redirect (url_for("view.SearchQuoteById"))
        
        
    return render_template("signup.html")
