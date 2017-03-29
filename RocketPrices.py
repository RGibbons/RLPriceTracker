
#requests deals with getting the HTML from the website and bs4 makes its easy to 
#traverse in python
import requests, bs4

#This is the dictionary where the information pulled down from the site will be stored
#while the program is running
RLItems = {}

#I got this from someone on reddit who stated that you have better luck accessing website
#with header info - essentially just giving the server an idea of what kind of request
#we are making
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/51.0.2704.103 Safari/537.36'}


website = "http://rocketprices.net/ps4";

#create a requests object that will hold all of the html we get back inside
res = requests.get(website, headers)

#This is incase the connection doesn't work, it will raise an exception and end the program
try:
	res.raise_for_status()
except Exception as e:
	print("Oops - there was a problem with your request: %s" % e)


#Here we turn our request object into a bs4 object, and simultaneously encode it so its
#friendly to shells like commandline, IDLE, etc. Not necessary unless there is printing
rocketHTML = bs4.BeautifulSoup(res.text.encode("ascii","xmlcharrefreplace"), "html.parser")

#Now we begin to traverse the elements on the page
#Quick Guide
#Items with a green background = ".imgWrappy"
#red background = ".imgWrap"
#purple/magenta background (I'm colorblind) = ".imgWrappgreen"
#yellow background = ".imgWrappyellow"
#Other than the yellow one there is not a lot of sense in the names of the classes but
#we won't question the wisdom of the site designer

#Isolate green items out of the whole bs4 object and store them in a list
greenItems = rocketHTML.select(".imgWrappy")

print(len(greenItems), " Green Items Present.")

#For each green item found on page:
for item in greenItems:

	name = item.select("p .js-name")[0].string #Get the name
	price = item.select("p .js-price")[0]		#Get the price
	#The below line is necessary because there is an <i> tag in price we must get rid of
	price.i.extract()							
	price = price.string
	#rarity has no specific CSS class, so give me the 3rd <p> tag and then give me the content
	#of that <p> tag. The content is actually a list which has [\n, rarity, \n] so we need to grab
	#the second item in the list
	rarity = item.select("p")[2].contents[1].string
	print(name)
	print(price)
	print(rarity)
	RLItems[name] = name #RLItems[name of item] =  name of item
	RLItems[name+"Price"] = price #RLItems[name of itemPrice] = price
	RLItems[name+"Rarity"] = rarity #RLItems[name of itemRarity] = rarity
	#RLItems[name+"Colors"] = {} #Nested dictionary to handle colors. We will cross that bridge
	#when we get there
	print(RLItems[name], ": ", RLItems[name+'Price'], "(", RLItems[name+"Rarity"], ")")
	print("...\n")


#everything below is just a repeat

redItems = rocketHTML.select(".imgWrap")

print(len(redItems), "Red Items Present.")

for item in redItems:

	name = item.select("p .js-name")[0].string
	price = item.select("p .js-price")[0]
	price.i.extract()
	price = price.string
	#This is annoying - they change it from <p> to div halfway through the page. I'm
	#going to hardcode it until I come up with a better solution
	rarity = "Import"
	#rarity = item.select("p")[2].contents[1].string
	print(name)
	print(price)
	print(rarity)
	RLItems[name] = name
	RLItems[name+"Price"] = price
	#RLItems[name+"Colors"] = {}
	print(RLItems[name], ": ", RLItems[name+'Price'])
	print("...\n")

purpleItems = rocketHTML.select(".imgWrappgreen")

print(len(purpleItems), " Purple Items Present.")

for item in purpleItems:

	name = item.select("p .js-name")[0].string
	price = item.select("p .js-price")[0]
	price.i.extract()
	price = price.string
	rarity = "Very Rare"
	#rarity = item.select("p")[2].contents[1].string
	print(name)
	print(price)
	print(rarity)
	RLItems[name] = name
	RLItems[name+"Price"] = price
	#RLItems[name+"Colors"] = {}
	print(RLItems[name], ": ", RLItems[name+'Price'])
	print("...\n")

yellowItems = rocketHTML.select(".imgWrappyellow")

print(len(yellowItems), " Yellow Items Present.")

for item in yellowItems:

	name = item.select("p .js-name")[0].string
	price = item.select("p .js-price")[0]
	price.i.extract()
	price = price.string
	rarity = "Exotic"
	#rarity = item.select("p")[2].contents[1].string
	print(name)
	print(price)
	print(rarity)
	RLItems[name] = name
	RLItems[name+"Price"] = price
	#RLItems[name+"Colors"] = {}
	print(RLItems[name], ": ", RLItems[name+'Price'])
	print("...\n")
