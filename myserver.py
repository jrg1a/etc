from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    key = request.form.get('key')
    
    # You may want to add some validation here to ensure 'key' is the correct format
    with open('log.txt', 'a') as f:
        f.write('{}\n'.format(key))
    
    return '', 204  # Return 204 No Content to indicate success

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
