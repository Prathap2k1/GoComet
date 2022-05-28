from bs4 import BeautifulSoup
import requests
File = open("output.csv","a")
HEADERS = ({'User-Agent':
		'Mozilla/5.0 (X11; Linux x86_64)
				AppleWebKit/537.36 (KHTML, like Gecko)
					Chrome/44.0.2403.157 Safari/537.36',
						'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

try:
		title = soup.find("span",
						attrs={"id": 'productTitle'})
	title_value = title.string

		title_string = title_value
					.strip().replace(',', '')
		
except AttributeError:

		title_string = "NA"

		print("product Title = ", title_string)

File.write(f"{title_string},")

File.write(f"{available},\n")

File.close()

if __name__ == '__main__':
# opening our url file to access URLs
	file = open("url.txt", "r")

	# iterating over the urls
	for links in file.readlines():
		main(links)
