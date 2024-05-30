from flask import  Blueprint , render_template , request ,flash
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


@view.route("/")
def home():
    return render_template("base.html")
