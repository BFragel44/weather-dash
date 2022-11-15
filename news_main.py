import requests
import config

def get_news():
	url = "https://bing-news-search1.p.rapidapi.com/news"

	querystring = {"textFormat":"Raw","safeSearch":"Off"}
	headers = {
		"X-BingApis-SDK": "true",
		"X-RapidAPI-Key": config.rapi,
		"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	# dict
	news_json = response.json()

	news_package = []

	for value in news_json.get("value"):
		headline = value["name"]
		story_url = value["url"]
		news_package.append((headline, story_url))
	
	return news_package



# if news.get("_type") == "TrendingTopics":

# {'_type': 'NewsArticle', 
# 'name': '9 people shot outside bar in Philadelphia: Police', 
# 'url': 'https://www.msn.com/en-us/news/crime/9-people-shot-outside-bar-in-philadelphia-police/ar-AA13NFIW', 
# 'image': {
# 	'_type': 'ImageObject', 
# 	'thumbnail': {
# 		'_type': 'ImageObject', 
# 		'contentUrl': 'https://www.bing.com/th?id=ORMS.5ceb82616c964f25e145900de6c3069f&pid=Wdp', 
# 		'width': 1024, 
# 		'height': 576}, 
# 		'isLicensed': True}, 
# 'description': "PHILADELPHIA (CBS) -- Nine people were shot outside a bar in Philadelphia's Kensington section on Saturday night, police say. The shooting happened in the area of Kensington and Allegheny Avenues", 
# 'provider': [
# 	{'_type': 'Organization', 
# 	'name': 'CBS New York', 
# 	'image': {
# 		'_type': 'ImageObject', 
# 		'thumbnail': {
# 			'_type': 'ImageObject', 
# 			'contentUrl': 'https://www.bing.com/th?id=ODF.lisIXhXb-iy9Ku1HbFcCEw&pid=news'
# 			}}}], 
# 'datePublished': '2022-11-06T18:58:00.0000000Z'}



# Add to the regular expression used in the extract_pid function, to 
# return the uppercase message in parenthesis, after the process id.
