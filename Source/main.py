__author__ = 'gwa2100'

import json
import urllib
import urllib.request
import urllib.parse
import urllib.response


def showsome(searchfor):
    query = urllib.parse.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode("utf8")
    results = json.loads(search_results)
    data = results['responseData']
    try:
        print('Total results: %s' % data['cursor']['estimatedResultCount'])
        hits = data['results']
        print('Top %d hits:' % len(hits))
        for h in hits:
            print(' ', h['url'])
            print('For more results, see %s' % data['cursor']['moreResultsUrl'])
        for i, line in enumerate(hits):
            print(line)
            if "Facebook" in line:
                for l in hits[i:i + 3]:
                    print(l), print("")
    except:
        print('no hits')


def getgoogleurl(search, siteurl=False):
    if siteurl == False:
        return 'http://www.google.com/search?q=' + urllib.parse.quote(search)
    else:
        return 'http://www.google.com/search?q=site:' + urllib.parse.quote(siteurl) + '%20' + urllib.parse.quote(search)


def pullgoogledata(search):
    headers = {'User-agent': 'Mozilla/11.0'}
    req = urllib.request.Request(getgoogleurl(search, False), None, headers)
    site = urllib.request.urlopen(req)
    gdata = site.read()
    site.close()
    return gdata


fstName = input('First name:')
lstName = input('Last name:')
searchTerm = fstName + " " + lstName
# searchString = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=" + fstName + "%20" \
#                + lstName
# html = request.urlopen(searchString).read()
# soup = BeautifulSoup(html, "html.parser")
# raw = soup.get_text()
# print ("RAW:" + raw)
# print (searchString)
# facebook = soup.find_all(text=re.compile("Facebook"))
# print(facebook)
# if "facebook" in raw:
#     print ("FACEBOOK DETECTED")

# showsome(fstName + " " + lstName)

data = pullgoogledata(searchTerm)
if b'facebook.com' in data:
    print("FACEBOOK HIT")
if b'twitter.com' in data:
    print("Twitter HIT")
if b'linkedIn.com' in data:
    print("LinkedIn HIT")
if b'myspace.com' in data:
    print("Myspace HIT")

print(data)
