#--------# --------# --------# --------# --------# --------# --------# --------#

# NOTE: For the most port, I have stopped passing down the name of the video to
# the name of the file. Most of the videos in the last few sections have either
# been something to reference when needed, or very little code. As we work our
# way back into some heavy code, I will just continue naming files with what
# makes sense at the time. Thanks :)
import requests
url = "https://api.yelp.com/v3/businesses/search"
API_KEY = "1CUNlPOfRTOhLwI5LyOWRtjVAkn4Kom2rkisVAZzfKwH5QcbJ0SgmOlnit3IYiyzkvs66t_HbI2JUttPuMpKAesr5K5xuAVLJ_N_H4h46CJwCa2t8VzB1qCl0HLqYHYx"
header = {
    "Authorization":
    'Bearer' + API_KEY
}
params = {
    "location": "NYC"
}
response = requests.get(url=url, headers=header, params=params)
print(response.text)
