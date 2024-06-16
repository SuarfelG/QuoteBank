from flask import  render_template , redirect , request , url_for , Blueprint ,flash
from flask_login import login_required
from . import db
from .models import Quotes
QuoteManager=Blueprint('quote',__name__)


@QuoteManager.route('/AddQuote' , methods=["POST","GET"])
@login_required
def AddQuotes():
    if request.method=="POST":
            Quote=request.form.get("Quote")
            Author=request.form.get("author")
            check= Quotes.query.all()
            for x in check:
                  print(x.Quote)
                  if Quote == x.Quote:
                        flash("Quote Already Exists" , category="error")
                        return redirect (url_for("view.SearchQuoteById"))
                  
            newquote=Quotes( Author=Author,Quote=Quote)
            db.session.add(newquote)
            db.session.commit()
            flash("Quote Added Successfuly" ,category="success")
            return redirect (url_for("view.SearchQuoteById"))
        
    return render_template ('AddQuotes.html')

@QuoteManager.route('/delete' , methods=["POST","GET"])
@login_required
def DeleteQuote():
      if request.method=="POST":

            id= request.form.get('id')
            quote=Quotes.query.filter_by(id=id).first()
            if quote:
                  db.session.delete(quote)
                  db.session.commit()
                  flash("Quote Successfully Deleted",category="success")  
            else:
                  flash("Quote doesn't exist" , category="error")
            return render_template ("delete.html")
      return render_template ("delete.html")