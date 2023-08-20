from flask import Flask, request
from src.networking import request_api



app = Flask(__name__)


@app.route('/my-ip-geolocation', methods=['GET'])
def home() :
    remote_ip = request.remote_addr
    status, data = request_api(remote_ip)
    
    if status == 200 :
        return f"<p>{data}</p>"
    else : 
        return "<p>Fail :(</p>"






if __name__ == '__main__':
    app.run(debug=True)