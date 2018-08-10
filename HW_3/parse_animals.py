import csv
import json

def lexo_sort(list_name, output_name):
	entries_array = sorted(open(list_name).read().split('\n'))
	f = open(output_name, "w")
	for row in entries_array:
		if row != "":
			insert = row + "\n"
			f.write(insert)
			print(row)

def gen_bitmap(animal_file, bitmap_file):

	animal_list = {
		'cat':'1000',
		'dog':'0100',
		'turtle':'0010',
		'bird':'0001'
		}

	age_list = [
		'1000000000','0100000000','0010000000','0001000000','0000100000',
		'0000010000','0000001000','0000000100','0000000010','0000000001'
		]

	adopted_list = {
		'True':'10',
		'False':'01'
		}

	f = open(bitmap_file, "w")

	with open(animal_file, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			print(row, end=":     ")

			concat_entry = ""

			# Animal type
			concat_entry += str(animal_list[row[0]])

			# Age bracket
			age = int(row[1])
			if age >= 1 and age <= 10:
				concat_entry += str(age_list[0])
			elif age > 10 and age <= 20:
				concat_entry += str(age_list[1])
			elif age > 20 and age <= 30:
				concat_entry += str(age_list[2])
			elif age > 30 and age <= 40:
				concat_entry += str(age_list[3])
			elif age > 40 and age <= 50:
				concat_entry += str(age_list[4])
			elif age > 50 and age <= 60:
				concat_entry += str(age_list[5])
			elif age > 60 and age <= 70:
				concat_entry += str(age_list[6])
			elif age > 70 and age <= 80:
				concat_entry += str(age_list[7])
			elif age > 80 and age <= 90:
				concat_entry += str(age_list[8])
			elif age > 90 and age <= 100:
				concat_entry += str(age_list[9])

			# Adpoted bool
			concat_entry += str(adopted_list[row[2]])

			print(concat_entry)

			concat_entry += "\n"
			f.write(str(concat_entry))

def main():
	# Generate bitmap for unsorted list
	print("Generating unsorted bitmap...")
	gen_bitmap("data/animals_test.txt", "results/bitmap.txt")

	# Sort list, then generate another bitmap
	print("Sorting original list...")
	lexo_sort("data/animals_test.txt", "results/animals_sorted.txt")

	#print("Generating sorted bitmap...")
	gen_bitmap("results/animals_sorted.txt", "results/bitmap_sorted.txt")

if __name__ == '__main__':
	main()
