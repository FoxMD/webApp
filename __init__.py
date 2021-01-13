from flask import Flask, render_template
import os
# from OpenSSL import SSL

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_certificate('/home/embedded-fox.crt')
# context.use_privatekey('/home/embedded-fox.key')

app = Flask(__name__)


@app.route("/")
def hello():
    return "Under construction"

@app.route("/Test")
def test():
    return render_template("under_construction.html")

if __name__ == "__main__":
    context = ('/home/embedded-fox.crt', '/home/embedded-fox.key')
    app.run(debug=False, ssl_context=context)
#    app.run()
