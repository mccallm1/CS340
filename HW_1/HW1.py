# Imports
import os
import sys
import csv
import json
import datetime
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
    mycursor.execute("DROP TABLE IF EXISTS movies_genres")
    mycursor.execute("DROP TABLE IF EXISTS movies_keywords")
    mycursor.execute("DROP TABLE IF EXISTS movies_companies")
    mycursor.execute("DROP TABLE IF EXISTS movies_countries")
    mycursor.execute("DROP TABLE IF EXISTS movies_languages")

    mycursor.execute("DROP TABLE IF EXISTS genres")
    mycursor.execute("DROP TABLE IF EXISTS keywords")
    mycursor.execute("DROP TABLE IF EXISTS production_companies")
    mycursor.execute("DROP TABLE IF EXISTS production_countries")
    mycursor.execute("DROP TABLE IF EXISTS original_language")
    mycursor.execute("DROP TABLE IF EXISTS movies")

    print("Generating table schema...")
    # Main Tables
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
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS keywords (
        id INT PRIMARY KEY,
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS production_companies (
        id INT PRIMARY KEY,
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS production_countries (
        iso_3166_1 INT PRIMARY KEY,
        name VARCHAR(255)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS languages (
        iso_639_1 INT PRIMARY KEY,
        name VARCHAR(255)
        )"""
    )

    # Relation Tables

    mycursor.execute("""CREATE TABLE IF NOT EXISTS movies_genres (
        movie_id INT,
        genre_id INT,
        PRIMARY KEY (movie_id,genre_id),
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (genre_id) REFERENCES genres(id)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS movies_keywords (
        movie_id INT,
        keyword_id INT,
        PRIMARY KEY (movie_id,keyword_id),
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (keyword_id) REFERENCES keywords(id)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS movies_companies (
        movie_id INT,
        company_id INT,
        PRIMARY KEY (movie_id,company_id),
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (company_id) REFERENCES production_companies(id)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS movies_countries (
        movie_id INT,
        country_id INT,
        PRIMARY KEY (movie_id,country_id),
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (country_id) REFERENCES production_countries(iso_3166_1)
        )"""
    )

    mycursor.execute("""CREATE TABLE IF NOT EXISTS movies_languages (
        movie_id INT,
        language_id INT,
        PRIMARY KEY (movie_id,language_id),
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (language_id) REFERENCES languages(iso_639_1)
        )"""
    )

def read_csv():
    #budget,genres,homepage,id,keywords,original_language,original_title,overview,popularity,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,vote_average,vote_count
    print("Parsing CSV file...")
    with open('./tmdb_5000_movies.csv', 'r') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=',')
        header = next(spamreader)
        #print(header)
        rowCount = 0

        final_row = {}

        for row in spamreader:

            print('------------------------------------------')

            final_row["budget"] = int(row[0])
            print("budget: ",str(budget))

            #print('------------------------------------------')

            genres = []
            genres_csv = json.loads(row[1])
            for entry in genres_csv:
                genres += [entry['id'],entry['name']]
            print("genres: ",str(genres))

            #print('------------------------------------------')


            final_row["homepage"] = str(row[2])
            print("homepage: ",str(homepage))

            #print('------------------------------------------')

            final_row["id"] = int(row[3])
            print("id: ",str(id))

            #print('------------------------------------------')

            keywords = []
            keywords_csv = json.loads(row[4])
            for entry in keywords_csv:
                keywords += [entry['id'],entry['name']]
            print("keywords: ",str(keywords))

            #print('------------------------------------------')

            final_row["original_language"] = str(row[5])
            print("original language: ",str(original_language))

            #print('------------------------------------------')

            final_row["original_title"] = str(row[6])
            print("original title: ",str(original_title))

            #print('------------------------------------------')

            final_row["overview"] = str(row[7])
            print("overview: ",str(overview))

            #print('------------------------------------------')

            final_row["popularity"] = float(row[8])
            print("popularity: ",str(popularity))

            #print('------------------------------------------')

            companies = []
            companies_csv = json.loads(row[9])
            for entry in companies_csv:
                companies += [entry['id'],entry['name']]
            print("companies: ",str(companies))

            #print('------------------------------------------')

            countries = []
            countries_csv = json.loads(row[10])
            for entry in countries_csv:
                countries += [entry['iso_3166_1'],entry['name']]
            print("countries: ",str(countries))

            #print('------------------------------------------')

            if row[11]:
                final_row["release_date"] = datetime.datetime.strptime(row[11], '%m/%d/%y').date()
                print("release date: ",str(release_date))

            #print('------------------------------------------')

            final_row["revenue"] = int(row[12])
            print("revenue: ",str(revenue))

            #print('------------------------------------------')

            if row[13]:
                final_row["runtime"] = int(row[13])
                print("revenue: ",str(runtime))

            #print('------------------------------------------')

            languages = []
            languages_csv = json.loads(row[14])
            for entry in languages_csv:
                languages += [entry['iso_639_1'],entry['name']]
            print("languages: ",str(languages))

            #print('------------------------------------------')

            final_row["status"] = str(row[15])
            print("revenue: ",str(status))

            #print('------------------------------------------')

            final_row["tagline"] = str(row[16])
            print("tagline: ",str(tagline))

            #print('------------------------------------------')

            final_row["title"] = str(row[17])
            print("title: ",str(title))

            #print('------------------------------------------')

            final_row["vote_avg"] = float(row[18])
            print("vote avg: ",str(vote_avg))

            #print('------------------------------------------')

            vote_count = int(row[19])
            print("vote count: ",str(vote_count))

            #print('------------------------------------------')

            final_row =

            # SQL Insert
            query = """INSERT INTO movies (
                id,
                title,
                budget,
                homepage,
                original_language,
                original_title,
                overview,
                popularity,
                release_date,
                revenue,
                runtime,
                status,
                tagline,
                vote_avg,
                vote_count)"""

            test_str = """INSERT INTO movies (
                id,
                title,
                budget,
                homepage,
                original_language,
                original_title,
                overview,
                popularity,
                release_date,
                revenue,
                runtime,
                status,
                tagline,
                vote_avg,
                vote_count)
                VALUES (
                    %s, %s)
                {0[name]}"""

            .format(dict(name='Fred'))



            vals = ("John", "Highway 21")
            mycursor.execute(sql, val)

mydb.commit()

            # End of row
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

    '''INSERT INTO `hw1`.`movies`
()
VALUES
(<{id: }>,
<{title: }>,
<{budget: }>,
<{homepage: }>,
<{original_language: }>,
<{original_title: }>,
<{overview: }>,
<{popularity: }>,
<{release_date: }>,
<{revenue: }>,
<{runtime: }>,
<{status: }>,
<{tagline: }>,
<{vote_avg: }>,
<{vote_count: }>);'''

def main():
    sql_init()
    #sql_inserts()
    #read_csv()

if __name__ == '__main__':
    main()
