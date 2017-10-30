from flask import Flask,request, render_template,url_for
import redirect
import stripe

app = Flask(__name__)

public_key = '########'         #API Key is hidden for security purpose
test_secret_key = '######'      #API Key is hidden for security purpose

stripe.api_key = test_secret_key

@app.route('/')
def index():
    return render_template('home.html', public_key=public_key)

@app.route('/thanku')
def thanku():
    return render_template('thanku.html')

@app.route('/paynow', methods=['POST'])
def paynow():
    
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1000,
        currency='usd',
        description='Selected Product name'
    )

    return redirect(url_for('thanku'))

if __name__ == '__main__':
    app.run(debug=True)