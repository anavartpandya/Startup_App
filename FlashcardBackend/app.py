from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/modify_flashcard', methods=['POST'])
def modify_flashcard():
    data = request.json
    front_text = data['frontText'] + " got its"
    back_text = data['backText'] + " got its"
    return jsonify({'frontText': front_text, 'backText': back_text})

@app.route('/health-check')
def health_check():
    print('ok')
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
