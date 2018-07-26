import csv
import json

def main():
	with open('../tmdb_5000_movies.csv', 'r') as csvfile:
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
			if rowCount > 10:
				break
			rowCount += 1

if __name__ == '__main__':
	main()