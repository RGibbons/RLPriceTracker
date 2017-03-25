import praw;

PS4posts = 0;

r = praw.Reddit("bot1");

RLExchange = r.subreddit("RocketLeagueExchange");

for post in RLExchange.hot(limit=1000):
	workingTitle = post.title.lower();
	if("ps4" in workingTitle):
		PS4posts +=1;
		if(workingTitle.find("[h]")>-1 and workingTitle.find("[w]")>-1 and workingTitle.find("[discussion]") == -1):
			haveIndex = post.title.find("[H]");
			wantIndex = post.title.find("[W]");
			haveItem = post.title[haveIndex:wantIndex].encode("ascii","replace");
			wantItem = post.title[wantIndex:].encode("ascii", "replace");
			print("Post ID: " + post.fullname[3:]);
			print( haveItem.decode("ascii", "replace") + " || " + wantItem.decode("ascii","replace"));
			print("\n");
			if(post.fullname[3:]=="61cd8k"):
				input("........................................................")


print("There were " + str(PS4posts) + " posts for the PS4");
input("Press Enter to end this program");
