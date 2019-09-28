# MiniProject1for601
Repository for project to create summaries from twitter accounts from posted pictures and text

user stories brainstormed with Pei on 9/9/19:
1) I, a company, want to know what my customers think of my products/services.
2) I, a busy person, want to keep up with my friends (the accounts I follow) but do not have the time to look at everything.
3) I, a student, want to know what my favorite celebrities are up to.
4) I, a student, want to know where to find the best clubs/restaurants/etc in my college's town or city.
5) I, a visitor, wnat to know what the best tourist attractions/accommodations/services/etc are for me in the town/city I am visiting.
5a) I, a town/city, want to track where visitors go, so that no attraction gets overcrowded/overwhelmed.
5b) I, an attraction/accommodation/services company in a town/city, want to know what my visitors think of my company.

Will probably start with user story 5, as it allows for expansion to 5a and 5b quite readily

Our final user story is a visitor that wants to evaluate a particular attraction OR an attraction that wants to assess visitors' responses.

Architecture:
Our app architecture hardcodes the target twitter feed's user name and feeds this into the twitter apis to get ten tweets. (Since our user story is about current evaluation, we do not go further back into the feed's history, though this is possible.) From there, the text of the tweets is fed into the Google Natural Language api and the average sentiment is returned. In addition, the app tells the users whether the greater number of tweets were positive or negative (or the numbers were equal), which can account for outliers unduly affecting the mean sentiment score we return (one super positve score might more than offset nine slightly negative scores in the mean). 
