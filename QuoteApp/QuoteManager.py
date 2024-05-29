from flask import  render_template , redirect , request , url_for , Blueprint ,flash
from . import db
from .models import Quotes
quote=Blueprint('quote',__name__)

@quote.route('/AddQuote' , methods=["POST","GET"])
def AddQuotes():
    if request.method=="POST":
            Quote=request.form.get("Quote")
            Author=request.form.get("author")
            newquote=Quotes( Author=Author,Quote=Quote)
            db.session.add(newquote)
            db.session.commit()
            flash("Quote Added Successfuly" ,category="success")
            return redirect (url_for("view.viewQuote"))
        
           
    return render_template ('AddQuotes.html')
@quote.route('/delete' , methods=["POST","GET"])
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