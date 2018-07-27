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

    print("Removing old versions...")
    mycursor.execute("DROP TABLE IF EXISTS keywords")
    mycursor.execute("DROP TABLE IF EXISTS production_companies")
    mycursor.execute("DROP TABLE IF EXISTS production_countries")
    mycursor.execute("DROP TABLE IF EXISTS original_language")
    mycursor.execute("DROP TABLE IF EXISTS movies")

    print("Generating table schema...")
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

    mycursor.execute("""CREATE TABLE IF NOT EXISTS keywords (
        id INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS production_companies (
        id INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS production_countries (
        iso_3166_1 INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS original_language (
        iso_639_1 INT PRIMARY KEY,
        movie_id INT,
        INDEX movie_ind (movie_id),
        FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        name VARCHAR(255)
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

def read_csv():
    tables = ["movies","keywords","production_companies","production_countries","original_language","genres"]
    print("Parsing CSV file...")
    with open('./tmdb_5000_movies.csv', 'r') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=',')
        header = next(spamreader)
        #print(header)
        rowCount = 0

        for row in spamreader:

            print('------------------------------------------')

            headerIndex = 0
            for attributeName in header:
                print(attributeName)
                for col in tables:
                    if col == attributeName:
                        print("\t ",col)
                        break
                    else:
                        print("\t movies")

                #print('\t' + row[headerIndex])
                headerIndex += 1

            print('------------------------------------------')

            #List of dictionaries
            #print('Parsed Line')
            #parsedLine = json.loads(row[1])
            #print(parsedLine)

            #print('------------------------------------------')

            #First dictionary
            #print('First Dictionary')
            #print(parsedLine[0])

            #print('------------------------------------------')

            #Key and values
            #print('Key and Values')
            #print()
            #for key in parsedLine[0]:
                #print('Key: ' + key)
                #print('Value: ' + str(parsedLine[0][key]))
                #print()

            #print('------------------------------------------')

            rowCount += 1
            break

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
    #sql_inserts()
    read_csv()

if __name__ == '__main__':
    main()
