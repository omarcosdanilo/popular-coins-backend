from flask import Flask
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
cors = CORS(app)

connection = sqlite3.connect("popular_coins.db", check_same_thread=False)
connection.row_factory = lambda column, row: dict(
    zip([col[0] for col in column.description], row)
)
cursor = connection.cursor()


@app.route("/coins", methods=["GET"])
def get_coins():
    data = cursor.execute("SELECT * FROM coins").fetchall()

    return data


@app.route('/coins/<string:id>/<int:value>/update', methods=['PUT'])
def update_coin_score(id, value):
    sql = """
        UPDATE coins
        SET number_of_reviews = number_of_reviews + 1,
        total_score = total_score + ?
        WHERE id = ?;
"""
    try:
        data = cursor.execute(sql, (value, id)).fetchone()
        connection.commit()
        return 'Updated Succesfully'
    except sqlite3.Error as error:
        return str(error)

    return data


app.run(debug=True)
