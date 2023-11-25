# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC74e582057d402ebdfed6384d8bca2348'
        auth_token = '8885a4c3becf0e8a44019ac85e288a68'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('IS6ad08a4fe808d61787f9d9243194068a') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'AC74e582057d402ebdfed6384d8bca2348'
    auth_token = '8885a4c3becf0e8a44019ac85e288a6'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('IS6ad08a4fe808d61787f9d9243194068a') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_verify.html')    # Write code here
    else:
        return redirect("http://localhost:5001/")


if __name__ == "__main__":
    app.run()

