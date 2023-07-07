import urllib.request
import re

keywords="This is a linear equation with one variable. It can be solved by isolating the variable x on one side of the equation:"
searchPhrase = keywords.replace(' ', '+')

html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchPhrase)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
#("https://www.youtube.com/watch?v=" + video_ids[0])

buffer = video_ids[0]
j = 0

for i in range(0, len(video_ids)):
    if j > 2:
        break
    if buffer != video_ids[i]:
        j += 1
        print("https://www.youtube.com/watch?v=" + buffer)
        buffer = video_ids[i]

        