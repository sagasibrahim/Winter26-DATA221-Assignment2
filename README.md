Question 1 
I wrote this script to read a text file and count how many times each word shows up. It cleans the data 
by making everything lowercase and stripping off punctuation from the ends of words. I also added a filter 
so it only counts words with at least two letters. In the end, it prints out a list of the top 10 most common words.

Question 2 
For this one, I used the same word-cleaning logic from Question 1 to look for bigrams (pairs of words that appear 
right next to each other). The program counts how often these pairs occur and then prints the top 5 most frequent 
ones it found.

Question 3 
This program looks for "near-duplicate" lines in a text file. To make sure the comparison is fair, it ignores things
like capitalization, spaces, and punctuation. If two lines look the same after being cleaned up, it groups them 
together. It prints the total number of duplicate groups found and shows a couple of examples with their original line
numbers.

Question 4 
In this script, I used the pandas library to look at a student dataset. I filtered the list for students who study at
least 3 hours, have internet at home, and have missed 5 or fewer classes. After filtering, it calculates the average
final grade for that specific group of students.

Question 5 
This program splits students into three categories—Low, Medium, and High—based on their final grades. For each of these 
groups, it calculates the average number of absences and what percentage of them have internet access. It then saves all
that summary data into a new CSV file.

Question 6 
I used this program to analyze a crime dataset. It checks the violent crime rate and labels each area as either 
"High Risk" or "Low Risk" (using 0.50 as the cutoff). Then, it compares the two groups to see what the average 
unemployment rate looks like for each risk level.

Question 7 
This is a web scraping script that goes to a Wikipedia page and pulls the page title. It also searches through the page
to find the first real paragraph of text. I set it to skip any paragraphs shorter than 50 characters so it doesn't just 
grab empty lines or short captions.

Question 8 
This script pulls all the main section headings (h2 tags) from a Wikipedia page. I made sure it cleans up the text (like
removing the "[edit]" links) and ignores the extra stuff at the bottom like "References" or "External links." It saves 
the final list of headings into a text file called headings.txt.

Question 9 
This program scrapes a table from Wikipedia. It looks for the first table that actually has enough data in it, then pulls
the headers and all the rows. It makes sure everything is lined up correctly and saves the whole thing as a CSV file called 
wiki_table.csv.

Question 10 
I created a search function for this one. You can give it any keyword and it will search through a text file for matches
without worrying about whether the letters are uppercase or lowercase. It prints out the line numbers and the text for every
match it finds, plus the total count at the end.
