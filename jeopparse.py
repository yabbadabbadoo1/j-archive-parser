# Python script to parse j-archive.org

from bs4 import BeautifulSoup
import urllib2
import os
import time

for i in range (1, 4512):
	print "Game " + str(i)
	url = "http://www.j-archive.com/showgame.php?game_id=" + str(i)
	html = urllib2.urlopen(url) #source is in html
	source = html.read()
	html.close()


	#use beautifulsoup to parse

	soup = BeautifulSoup(source)

	#get category names

	categories = soup.findAll("td", class_="category_name")

	
	category_file_name = "category_" + str(i)
	category_file = open(category_file_name, 'w')
	for c in categories:
		category_file.write(c.text.encode('ascii', 'ignore') + '\n')
	category_file.close()

	#get category comments and append
	
	category_comments = soup.findAll("td", class_="category_comments")

	category_comments_file_name = "categorycomments_" + str(i)
	category_comments_file = open(category_comments_file_name, 'w')
	for c in category_comments:
		category_comments_file.write(c.text.encode('ascii', 'ignore') + '\n')
	category_comments_file.close()

	#get clues

	clue_id_template = "clue_J_"
	clue_id_template_doubleJ = "clue_DJ_"

	# first jeopardy round

	clues_file_name = "clues_" + str(i)
	clues_file = open(clues_file_name, 'w')
	for category_number in range(1, 7):
		for clue_number in range(1, 6):
			clue_id = clue_id_template + str(category_number) + "_" + str(clue_number)
			clue1 = soup.find("td", id=clue_id)
			if clue1 is None:
				clues_file.write("NO CLUE\n")
			else:
				clues_file.write(clue1.text.encode('ascii', 'ignore') + "\n")


	#double jeopardy round
	for category_number in range(1, 7):
		for clue_number in range(1, 6):
			clue_id_doubleJ = clue_id_template_doubleJ + str(category_number) + "_" + str(clue_number)
			clue2 = soup.find("td", id=clue_id_doubleJ)
			if clue2 is None:
				clues_file.write("NO CLUE\n")
			else:
				clues_file.write(clue2.text.encode('ascii', 'ignore') + "\n")
	clues_file.close()

	#final jeopardy round
	final_jeop_clue_name = "final_" + str(i)
	final_jeop_clue_file = open(final_jeop_clue_name, 'w')
	final_jeop_clue = soup.find ("td", id="clue_FJ")
	if final_jeop_clue is None:
		final_jeop_clue_file.write("\n")
	else:
		final_jeop_clue_file.write(final_jeop_clue.text.encode('ascii', 'ignore') + "\n")
	final_jeop_clue_file.close()
	time.sleep(.5)