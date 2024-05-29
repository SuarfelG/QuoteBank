from flask import  Blueprint , render_template , request ,flash
from .models import Quotes

view = Blueprint("view",__name__)

@view.route("/view",methods=["POST","GET"])
def viewQuote():
        if request.method=="POST":
                id=request.form.get("id")
                Quote = Quotes.query.filter_by(id=id).first()
                if Quote:
                        return render_template('views.html', Quote=Quote)
                else:
                        flash("Quote Not Found" , category="error")
                        return render_template("base.html")
        return render_template("views.html")


@view.route("/")
def home():
    return render_template("base.html")
