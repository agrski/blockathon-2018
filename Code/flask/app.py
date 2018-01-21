from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import pandas as pd

app = Flask(__name__)
land_id = [1, 2, 3]
add = 'PG, PNG, 598'
d = {'Land ID': pd.Series([add, add, add], index=land_id),
     'Address': pd.Series([add, add, add], index=land_id),
     }
data = pd.DataFrame(d)
# data.iloc[[2]]

@app.route("/")
def show_tables():
    return render_template('index.html',tables=[data.to_html(classes='table table-bordered')], #table table-bordered so that bootstrap css can style it
    titles = ['na', 'blockchain'])



# # Index
# @app.route('/')
# def index():
#     return render_template('index_orig.html')




if __name__ == '__main__':

    app.run(debug=True)