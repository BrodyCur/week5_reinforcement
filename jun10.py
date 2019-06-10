import random

reinforce_dictionary = { 'response': {
'status': "ok",
'userTier': "developer",
'total': 9772,
'startIndex': 1,
'pageSize': 10,
'currentPage': 1,
'pages': 978,
'orderBy': "relevance",
'results': [
{ 'id': "film/2017/jul/25/daniel-craig-judi-dench-and-idris-elba-toronto-film-festival",
'type': "article",
'sectionId': "film",
'sectionName': "Film",
'webPublicationDate': "2017-07-25T14:51:27Z",
'webTitle': "Daniel Craig, Judi Dench and Idris Elba lead British invasion of Toronto film festival",
'webUrl': "https://www.theguardian.com/film/2017/jul/25/daniel-craig-judi-dench-and-idris-elba-toronto-film-festival",
'apiUrl': "https://content.guardianapis.com/film/2017/jul/25/daniel-craig-judi-dench-and-idris-elba-toronto-film-festival",
'isHosted': False },
{ 'id': "us-news/2017/jun/27/trump-name-scrubbed-toronto-canada-hotel",
'type': "article",
'sectionId': "us-news",
'sectionName': "US news",
'webPublicationDate': "2017-06-27T22:49:50Z",
'webTitle': "Trump's name to be scrubbed from high-rise building in Toronto",
'webUrl': "https://www.theguardian.com/us-news/2017/jun/27/trump-name-scrubbed-toronto-canada-hotel",
'apiUrl': "https://content.guardianapis.com/us-news/2017/jun/27/trump-name-scrubbed-toronto-canada-hotel",
'isHosted': False },
{ 'id': "football/blog/2017/may/08/toronto-fc-mls-michael-bradley-seattle",
'type': "article",
'sectionId': "football",
'sectionName': "Football",
'webPublicationDate': "2017-05-08T13:06:11Z",
'webTitle': "Toronto FC's impressive win backs up Bradley's 'best team in MLS' claim | Matt Pentz",
'webUrl': "https://www.theguardian.com/football/blog/2017/may/08/toronto-fc-mls-michael-bradley-seattle",
'apiUrl': "https://content.guardianapis.com/football/blog/2017/may/08/toronto-fc-mls-michael-bradley-seattle",
'isHosted': False },
{ 'id': "world/2017/apr/20/toronto-foreign-tax-homes-housing-market-canada",
'type': "article",
'sectionId': "world",
'sectionName': "World news",
'webPublicationDate': "2017-04-20T19:17:57Z",
'webTitle': "Toronto to impose 15% tax on foreign home buyers to regulate housing costs",
'webUrl': "https://www.theguardian.com/world/2017/apr/20/toronto-foreign-tax-homes-housing-market-canada",
'apiUrl': "https://content.guardianapis.com/world/2017/apr/20/toronto-foreign-tax-homes-housing-market-canada",
'isHosted': False },
{ 'id': "discover-cool-canada/2016/sep/16/10-of-the-best-hotels-in-toronto",
'type': "article",
'sectionId': "discover-cool-canada",
'sectionName': "Discover cool Canada",
'webPublicationDate': "2016-09-16T12:00:22Z",
'webTitle': "10 of the best hotels in Toronto",
'webUrl': "https://www.theguardian.com/discover-cool-canada/2016/sep/16/10-of-the-best-hotels-in-toronto",
'apiUrl': "https://content.guardianapis.com/discover-cool-canada/2016/sep/16/10-of-the-best-hotels-in-toronto",
'isHosted': False },
 { 'id': "discover-cool-canada/2016/sep/16/10-toronto-restaurants-to-suit-every-budget",
'type': "article",
'sectionId': "discover-cool-canada",
'sectionName': "Discover cool Canada",
'webPublicationDate': "2016-09-16T11:59:53Z",
'webTitle': "10 Toronto restaurants to suit every budget",
'webUrl': "https://www.theguardian.com/discover-cool-canada/2016/sep/16/10-toronto-restaurants-to-suit-every-budget",
'apiUrl': "https://content.guardianapis.com/discover-cool-canada/2016/sep/16/10-toronto-restaurants-to-suit-every-budget",
'isHosted': False },
{ 'id': "discover-cool-canada/2016/sep/16/10-destinations-near-toronto-not-to-miss",
'type': "article",
'sectionId': "discover-cool-canada",
'sectionName': "Discover cool Canada",
'webPublicationDate': "2016-09-16T11:59:16Z",
'webTitle': "10 destinations near Toronto not to miss",
'webUrl': "https://www.theguardian.com/discover-cool-canada/2016/sep/16/10-destinations-near-toronto-not-to-miss",
'apiUrl': "https://content.guardianapis.com/discover-cool-canada/2016/sep/16/10-destinations-near-toronto-not-to-miss",
'isHosted': False },
{ 'id': "sport/blog/2017/feb/24/toronto-wolfpack-challenge-cup-debut-halifax-rugby-league",
'type': "article",
'sectionId': "sport",
'sectionName': "Sport",
'webPublicationDate': "2017-02-24T14:39:00Z",
'webTitle': "Toronto Wolfpack ready for ‘mystique’ of Challenge Cup debut in Halifax | Aaron Bower",
'webUrl': "https://www.theguardian.com/sport/blog/2017/feb/24/toronto-wolfpack-challenge-cup-debut-halifax-rugby-league",
'apiUrl': "https://content.guardianapis.com/sport/blog/2017/feb/24/toronto-wolfpack-challenge-cup-debut-halifax-rugby-league",
'isHosted': False } ,
{ 'id': "sport/2017/feb/25/toronto-wolfpack-challenge-cup-debut-siddal",
'type': "article",
'sectionId': "sport",
'sectionName': "Sport",
'webPublicationDate': "2017-02-25T17:59:47Z",
'webTitle': "Toronto Wolfpack take leap into the muddy unknown in rural Yorkshire | Aaron Bower",
'webUrl': "https://www.theguardian.com/sport/2017/feb/25/toronto-wolfpack-challenge-cup-debut-siddal",
'apiUrl': "https://content.guardianapis.com/sport/2017/feb/25/toronto-wolfpack-challenge-cup-debut-siddal",
'isHosted': False },
{ 'id': "tv-and-radio/2017/aug/29/margaret-atwood-you-have-been-warned-imagine-review",
'type': "article",
'sectionId': "tv-and-radio",
'sectionName': "Television &amp; radio",
'webPublicationDate': "2017-08-29T05:00:54Z",
'webTitle': "Margaret Atwood – You Have Been Warned! review: precious little of the woman herself",
'webUrl': "https://www.theguardian.com/tv-and-radio/2017/aug/29/margaret-atwood-you-have-been-warned-imagine-review",
'apiUrl': "https://content.guardianapis.com/tv-and-radio/2017/aug/29/margaret-atwood-you-have-been-warned-imagine-review",
'isHosted': False
}
]}
}

for result in reinforce_dictionary['response']['results']:
    result.update( {'views': 0 } )

def read_article():
    r = random.randint(0, len(reinforce_dictionary['response']['results'])-1)
    reinforce_dictionary['response']['results'][r]['views'] +=1

def display_views():
    for article in reinforce_dictionary['response']['results']:
        print(article['webTitle'])
        print(f"Read {article['views']}")

read_article()
read_article()
read_article()
read_article()
read_article()
display_views()