from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    loads homepage
    """

    return render_template('main.html')

''' left this here for an example
@app.route("/data")
def datatest():

    data = datapuller()
    csadata = data[0]
    abusedata = data[1]
    spamhausdata = data[2]

    # pass the data do the template
    return render_template('chart.html', csadata=csadata, abusedata=abusedata, spamhausdata=spamhausdata)

if __name__ == '__main__':
    app.run()
'''