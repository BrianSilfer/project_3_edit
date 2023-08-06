from flask import Flask, jsonify
import sqlite3
from dateutil.parser import parse
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/movies')
def display_movies():
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * FROM netflix_titles"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

@app.route('/movies/released/<int:year>')
def display_movies_by_year(year):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from netflix_titles where release_year = ?"
        df = pd.read_sql_query(query, conn, params=(year,))

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

@app.route('/movies/released/start=<int:start_year>')
def display_movies_by_start_year(start_year):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from netflix_titles where release_year >= ?"
        df = pd.read_sql_query(query, conn, params=(start_year,))

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

@app.route('/movies/released/start=<int:start_year>/stop=<int:stop_year>', methods=['GET'])
def display_movies_by_year_range(start_year, stop_year):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'netflix_titles' table
        query = "SELECT * from netflix_titles where release_year BETWEEN ? AND ?"
        df = pd.read_sql_query(query, conn, params=(start_year, stop_year,))

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the movies dictionary as JSON
        return jsonify(movies_dict)

# not working
@app.route('/movies/added/<year>', methods=['GET'])
def display_movies_added_by_year(year):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'netflix_titles' table
        query = "SELECT * from netflix_titles"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert 'date_added' to datetime and filter rows between start_date and end_date
        df['date_added'] = df['date_added'].apply(lambda x: parse(x.strip()) if pd.notnull(x) else None)
        df = df.loc[(df['date_added'] == parse(year))]

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the movies dictionary as JSON
        return jsonify(movies_dict)

@app.route('/movies/added/start=<start_date>/stop=<end_date>', methods=['GET'])
def display_movies_added_by_date_range(start_date, end_date):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'netflix_titles' table
        query = "SELECT * from netflix_titles"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert 'date_added' to datetime and filter rows between start_date and end_date
        df['date_added'] = df['date_added'].apply(lambda x: parse(x.strip()) if pd.notnull(x) else None)
        df = df.loc[(df['date_added'] >= parse(start_date)) & (df['date_added'] <= parse(end_date))]

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the movies dictionary as JSON
        return jsonify(movies_dict)

@app.route('/movies/added/start=<start_date>', methods=['GET'])
def display_movies_added_by_start_year(start_date):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'netflix_titles' table
        query = "SELECT * from netflix_titles"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert 'date_added' to datetime and filter rows between start_date and end_date
        df['date_added'] = df['date_added'].apply(lambda x: parse(x.strip()) if pd.notnull(x) else None)
        df = df.loc[(df['date_added'] >= parse(start_date))]

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the movies dictionary as JSON
        return jsonify(movies_dict)

@app.route('/stocks/')
def display_stocks():
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from nflx"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

# not working
@app.route('/stocks/date/<year>')
def display_stocks_by_year(year):
# Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'netflix_titles' table
        query = "SELECT * from nflx"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert 'date_added' to datetime and filter rows between start_date and end_date
        df['Date'] = df['Date'].apply(lambda x: parse(x.strip()) if pd.notnull(x) else None)
        df = df.loc[(df['Date'] == parse(year))]

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the movies dictionary as JSON
        return jsonify(movies_dict)

@app.route('/stocks/date/start=<start_year>')
def display_stocks_by_start_year(start_year):
# Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'netflix_titles' table
        query = "SELECT * from nflx"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert 'date_added' to datetime and filter rows between start_date and end_date
        df['Date'] = df['Date'].apply(lambda x: parse(x.strip()) if pd.notnull(x) else None)
        df = df.loc[(df['Date'] >= parse(start_year))]

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the movies dictionary as JSON
        return jsonify(movies_dict)

@app.route('/stocks/date/start=<start_date>/stop=<end_date>', methods=['GET'])
def display_stocks_by_date_range(start_date, end_date):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'netflix_titles' table
        query = "SELECT * from nflx"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert 'date_added' to datetime and filter rows between start_date and end_date
        df['Date'] = df['Date'].apply(lambda x: parse(x.strip()) if pd.notnull(x) else None)
        df = df.loc[(df['Date'] >= parse(start_date)) & (df['Date'] <= parse(end_date))]

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the movies dictionary as JSON
        return jsonify(movies_dict)

if __name__ == "__main__":
        app.run(debug=True)