from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Programi i Stokut</h1>
    <p>Kjo është një faqe e thjeshtë që do të shfaqë stoqet më vonë.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
