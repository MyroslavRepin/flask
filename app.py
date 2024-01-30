from flask import Flask, render_template, request, send_file
import filecmp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_text = None
    if request.method == 'POST':
        user_text = request.form.get('text')
    
    with open('users_text.txt', 'w') as file:
            file.write(user_text)
    return render_template('index.html', user_text=user_text)

@app.route('/download')
def download():
     return send_file('users_text.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
