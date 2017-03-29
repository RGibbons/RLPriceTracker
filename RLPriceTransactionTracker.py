import praw

PS4posts = 0	#Counts number of posts with [PS4] tag

r = praw.Reddit("bot1") #creates praw object. bot1 is a specific set of authorizations that
						# that is found in a file called praw.ini. This isn't in the github
						#because it contains sensitive information

RLExchange = r.subreddit("RocketLeagueExchange")	#We point our praw object to the subreddit we want

for post in RLExchange.hot(limit=1000):	#For each of the first 1000 posts designated as hot
	workingTitle = post.title.lower()	#lower the case of the string to make checking easier
	if("ps4" in workingTitle):			#if ps4 is in title
		PS4posts +=1
		#If there is an [H] and [W] tag and no discussion tag
			if(workingTitle.find("[h]")>-1 and workingTitle.find("[w]")>-1 and workingTitle.find("[discussion]") == -1):
			haveIndex = post.title.find("[H]")	#index of [H] tag
			wantIndex = post.title.find("[W]")	#index of [W] tag
			haveItem = post.title[haveIndex:wantIndex].encode("ascii","replace")
			wantItem = post.title[wantIndex:].encode("ascii", "replace")
			#This is mostly for debugging. Reddit post titles are not for humans and
			#look like this: t3_23HG92. This cuts off the first 3 chars which aren't needed
			print("Post ID: " + post.fullname[3:])  
			print( haveItem.decode("ascii", "replace") + " || " + wantItem.decode("ascii","replace")) #print out the post title.
			print("\n")


print("There were " + str(PS4posts) + " posts for the PS4")
input("Press Enter to end this program")
