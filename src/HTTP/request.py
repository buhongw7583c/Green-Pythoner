import requests
import json

## Use requests.get(url).json to decode the text from URL
text_url = 'https://api.github.com'
text_response = requests.get(text_url)
#print (text_response.json())
#print (json.loads(text_response.text))

gif_url = 'http://www.baidu.com/img/baidu_jgylogo3.gif'
gif_response = requests.get(gif_url)
print (gif_response.content)



def my_add(a: int, b: int) -> int:
    return a + b

print(my_add(5.4, 5))