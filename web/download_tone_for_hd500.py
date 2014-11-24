import urllib2
import urllib

url = "http://line6.com/customtone/tone/deliver/"

def downloadtone(ids):
    data = urllib2.urlopen(url + str(ids))
    d =  data.info().dict
    filename =  d['content-disposition'].split("=")[1][1:-1]
    if(filename[-3:] != "h5e"):
        return

    with open("tones/" + filename, "w") as f:
        print filename
        f.write(data.read())



for i in range(210000, 211000):
    downloadtone(i)

