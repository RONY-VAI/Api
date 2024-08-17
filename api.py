from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SMS_GATEWAY_URL = 'https://api.yoursmsgateway.com/send'
API_KEY = 'your_api_key_here'

@app.route('/send_sms', methods=['POST'])
def send_sms():
    phone_number = request.json.get('phone_number')
    message = request.json.get('message')

    if not phone_number or not message:
        return jsonify({'error': 'Phone number and message are required'}), 400

    response = requests.post(
        SMS_GATEWAY_URL,
        data={
            'api_key': API_KEY,
            'to': phone_number,
            'message': message
        }
    )

    if response.status_code == 200:
        return jsonify({'success': 'SMS sent successfully'}), 200
    else:
        return jsonify({'error': 'Failed to send SMS'}), 500

if __name__ == '__main__':
    app.run(debug=True)