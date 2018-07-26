# Imports
import os
import sys
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

    # Make tables
    mycursor.execute(sql =
        "CREATE TABLE movies (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            budget INT,
            homepage VARCHAR(255),
            original_language VARCHAR(255),
            original_title VARCHAR(255),
            title VARCHAR(255),
            overview TEXT,
            popularity FLOAT,
            release_date DATE,
            revenue INT,
            runtime INT,
            status VARCHAR(50),
            tagline TEXT,
            vote_avg FLOAT,
            vote_count INT
            )"
        )
    mycursor.execute(sql =
        "CREATE TABLE genres (
            id INT PRIMARY KEY, movie_id INT FOREIGN KEY, name VARCHAR(255))"
        )
    mycursor.execute(sql =
        "CREATE TABLE keywords (
            id INT  PRIMARY KEY, movie_id INT FOREIGN KEY, name VARCHAR(255))"
        )
    mycursor.execute(sql =
        "CREATE TABLE companies (
            id INT  PRIMARY KEY, movie_id INT FOREIGN KEY, name VARCHAR(255))"
        )
    mycursor.execute(sql =
        "CREATE TABLE countries (
            iso_3166_1 INT PRIMARY KEY, movie_id INT FOREIGN KEY, name VARCHAR(255))"
        )
    mycursor.execute(sql =
        "CREATE TABLE languages (
            iso_639_1 INT PRIMARY KEY, movie_id INT FOREIGN KEY, name VARCHAR(255))"
        )



def main():
    sql_init()

if __name__ == '__main__':
    main()
