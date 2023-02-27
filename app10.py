from flask import Flask, render_template, request, send_file
import os
import table

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/submitfile', methods=['POST'])
def submitfile():
    global file
    file = request.files["filename"]

    if os.path.splitext(file.filename)[1] != ".csv":
        return render_template("home.html", message = "Sorry that is not a CSV file.")

    if request.method=='POST':
        new_table = table.geocode(file)
        if new_table[0] == False:
            return render_template("home.html", message = "Sorry there is no column labeled 'address'.")
        return render_template("home.html", chart=new_table[1].to_html(), btn="download.html")

@app.route('/download/')
def download():
    return send_file('uploaded/geocoded_'+file.filename, as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)