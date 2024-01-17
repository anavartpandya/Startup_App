from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/modify_flashcard', methods=['POST'])
def modify_flashcard():
    data = request.json
    front_text = data['frontText'] + " got it"
    back_text = data['backText'] + " got it"
    return jsonify({'frontText': front_text, 'backText': back_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
