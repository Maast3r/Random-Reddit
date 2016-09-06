import os
from faker import name
from faker import lorem
import random
import csv
import sys
import time

bools = [True, False]
maxInt = 2147483648
length = 1000000

def main():
	headers = ['archived', 'author', 'author_flair_css_class', 'author_flair_text', 'body', 'controversiality',
		'created_utc', 'distinguished', 'downs', 'edited', 'gilded', 'id', 'link_id', 'name',
		'parent_id', 'retrieved', 'score', 'score_hidden', 'subreddit', 'subreddit_id', 'ups', 'positive']

	start_time = time.time()
	with open("test_data/test.csv", 'w', newline='', encoding='utf-8') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow(headers)

		for i in range(0, length):
			row = [random.choice(bools), name.find_name(), '', '', lorem.bias_sentence(False, True), random.randint(-maxInt, maxInt), random.randint(-maxInt, maxInt), '', random.randint(-maxInt, maxInt),
				random.choice(bools), random.randint(-maxInt, maxInt), name.find_name()+str(random.randint(-maxInt, maxInt)), name.first_name()+str(random.randint(-maxInt, maxInt)), name.find_name(),
				name.last_name()+str(random.randint(-maxInt, maxInt)), random.randint(-maxInt, maxInt), random.randint(-maxInt, maxInt), random.choice(bools), '/r'+name.find_name(),
				name.find_name()+str(random.randint(-maxInt, maxInt)), random.randint(-maxInt, maxInt), True]
			writer.writerow(row)

		for i in range(0, length):
			row = [random.choice(bools), name.find_name(), '', '', lorem.bias_sentence(False, False), random.randint(-maxInt, maxInt), random.randint(-maxInt, maxInt), '', random.randint(-maxInt, maxInt),
				random.choice(bools), random.randint(-maxInt, maxInt), name.find_name()+str(random.randint(-maxInt, maxInt)), name.first_name()+str(random.randint(-maxInt, maxInt)), name.find_name(),
				name.last_name()+str(random.randint(-maxInt, maxInt)), random.randint(-maxInt, maxInt), random.randint(-maxInt, maxInt), random.choice(bools), '/r'+name.find_name(),
				name.find_name()+str(random.randint(-maxInt, maxInt)), random.randint(-maxInt, maxInt), False]
			writer.writerow(row)


	print ("Took " + str(time.time()-start_time) + " seconds.")

if __name__ == "__main__":
	main()
