import requests
#replace 57 with number of lectures
for i in range(1,57):
  #replace 106106131 with your course ID
  url='http://textofvideo.nptel.ac.in/106106131/lec'+str(i)+'.pdf'
  r = requests.get(url, stream=True)
  with open(str(i)+'.pdf', 'wb') as fd:
    for chunk in r.iter_content(200000):
        fd.write(chunk)
  print 'File '+str(i)+' downloaded'
