# Imports
import os
import sys
import csv
import json
import mysql.connector

#Functions
def sql_init():
    # MySQL Connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Atiradeon1",
        database="hw1"
        )
    print(mydb)
    mycursor = mydb.cursor()

    # Remove old versions
    mycursor.execute("DROP TABLE IF EXISTS keywords")
    mycursor.execute("DROP TABLE IF EXISTS companies")
    mycursor.execute("DROP TABLE IF EXISTS countries")
    mycursor.execute("DROP TABLE IF EXISTS languages")
    mycursor.execute("DROP TABLE IF EXISTS movies")

    # Make tables
    mycursor.execute("""CREATE TABLE IF NOT EXISTS movies (
        id INT PRIMARY KEY,
        title VARCHAR(255),
        budget INT,
        homepage VARCHAR(255),
        original_language VARCHAR(255),
        original_title VARCHAR(255),
        overview TEXT,
        popularity FLOAT,
        release_date DATE,
        revenue INT,
        runtime INT,
        status VARCHAR(50),
        tagline TEXT,
        vote_avg FLOAT,
        vote_count INT
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS genres (
        id INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS keywords (
        id INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS companies (
        id INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS countries (
        iso_3166_1 INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS languages (
        iso_639_1 INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

def read_csv():
    with open('./tmdb_5000_movies.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        header = next(spamreader)
        print(header)
        rowCount = 0

        for row in spamreader:
            print('------------------------------------------')
            headerIndex = 0

            #This is one way to iterate through all of the attribute columns with their corresponding headers
            for attributeName in header:
                print(attributeName)
                print('\t' + row[headerIndex])
                headerIndex += 1
                print()
            print('------------------------------------------')
            #This is one way to parse the dictionaries in the CSV file
            #List of dictionaries
            print('Parsed Line')
            parsedLine = json.loads(row[1])
            print(parsedLine)
            print('------------------------------------------')

            #First dictionary
            print('First Dictionary')
            print(parsedLine[0])
            print('------------------------------------------')

            #Key and values
            print('Key and Values')
            print()
            for key in parsedLine[0]:
                print('Key: ' + key)
                print('Value: ' + str(parsedLine[0][key]))
                print()
            print('------------------------------------------')
            if rowCount > 1:
                break
            rowCount += 1

def sql_inserts():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Atiradeon1",
        database="hw1"
        )
    print(mydb)
    mycursor = mydb.cursor()

def main():
    sql_init()
    sql_inserts()
    read_csv()

if __name__ == '__main__':
    main()
