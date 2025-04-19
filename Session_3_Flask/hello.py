from flask import Flask, request
import joblib

encode_dict={
    "fuel_type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
     "transmission_type": {"Manual": 1, "Automatic": 2},
	 "seller_type": {"Dealer": 1, "Individual": 2, "Trustmark Dealer": 3}
}

pancakes = Flask(__name__)
@pancakes.route('/')
def main():
    return '''
    <!doctype html>
    <html>
        <head>
            <title>Login Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                form {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    animation: fadeIn 1s ease-in-out;
                }
                label {
                    display: block;
                    margin-bottom: 5px;
                    font-weight: bold;
                }
                input[type="text"], input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 15px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="submit"] {
                    background: #ff6f61;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background 0.3s ease;
                }
                input[type="submit"]:hover {
                    background: #e55b50;
                }
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                        transform: translateY(-20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
            </style>
        </head>
        <body>
            <form action="/login" method="post">
                <h1>Login</h1>
                <label for="username">Username:</label>
                <input type="text" id="username" name="username">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password">
                <input type="submit" value="Login">
            </form>
        </body>
    </html>
    '''

@pancakes.route('/login', methods=['GET'])
def hello():
    return '''
    <!doctype html>
    <html>
        <head>
            <title>Instagram Homepage</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    width: 300px;
                }
                h1 {
                    color: #333;
                    margin-bottom: 20px;
                }
                .profile-pic {
                    width: 100px;
                    height: 100px;
                    border-radius: 50%;
                    margin-bottom: 15px;
                    background: #ddd;
                }
                .post {
                    background: #f9f9f9;
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="profile-pic"></div>
                <h1>Welcome to Instagram</h1>
                <div class="post">Post 1: This is a sample post.</div>
                <div class="post">Post 2: Another example post.</div>
                <div class="post">Post 3: Yet another post!</div>
            </div>
        </body>
    </html>
    '''


model = joblib.load('/Users/kavithiyagu/Documents/Projects/Mlops/cars24-car-price-model.joblib')
scaler = joblib.load('/Users/kavithiyagu/Documents/Projects/Mlops/Session_2_Streamlit/scaler.pkl')

@pancakes.route('/predict', methods = ['POST'])
def predict():
    load = request.get_json()

    fuel_type = encode_dict['fuel_type'][load['fuel_type']]
    transmission_type = encode_dict['transmission_type'][load['transmission_type']]
    seller_type = encode_dict['seller_type'][load['seller_type']]
    year = load['year']
    km_driven = load['km_driven']
    millege = load['millege']
    engine = load['engine']
    max_power = load['max_power']
    seats = load['seats']

    print('year:', year)
    print('fuel_type:', fuel_type)

    data = [[
		float(year),
		seller_type,
		float(km_driven),
		fuel_type,
		transmission_type,
		float(millege),
		float(engine),
		float(max_power),
		float(seats)
	]]

    data = scaler.transform(data)
    prediction = model.predict(data)


    return {
        'prediction' : list(prediction)
    }


