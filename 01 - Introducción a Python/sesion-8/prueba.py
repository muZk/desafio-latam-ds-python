import json
import requests


def request(url, api_key):
    final_url = '{}&api_key={}'.format(url, api_key)
    response = requests.request('GET', final_url)
    return json.loads(response.text)


def build_web_page(data):
    start = '<html>\n<head>\n</head>\n<body>\n<ul>\n'
    body = ''
    for photo in data['photos']:
        body += "   <li><img src='{}'></li>\n".format(photo['img_src'])
    end = '</ul>\n</body>\n</html>'
    f = open('index.html', 'w')
    f.write(start + body + end)
    f.close()
    return start + body + end


def photos_count(data):
    count = {}
    for photo in data['photos']:
        camera_name = photo['camera']['name']
        if not camera_name in count:
            count[camera_name] = 0
        count[camera_name] += 1
    return count


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=10'
token = '9f1bex4j9PO0qmHmtVxj8jBCM56XurTMLbBuB9s6'
data = request(url, token)
build_web_page(data)
