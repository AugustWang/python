#encoding:utf-8
# Create your views here.
from django.http import HttpResponse
import urllib
from BeautifulSoup import BeautifulSoup

def one_article(request):
    url = urllib.urlopen("http://hanhan.qq.com/hanhan/one/one221m.htm#page1").read()
    soup = BeautifulSoup(url)
    tit = soup.findAll('h1',{'class':'tit','id':'onebd'})
    pic = soup.findAll('div',{'class':'neirong','id':'picIdbd'})
    return HttpResponse('<html><body>%s,%s</body></html>' % (tit,pic))

def one_img(request):
    img_url = urllib.urlopen("http://hanhan.qq.com/hanhan/one/one221m.htm#page0").read()
    img_soup = BeautifulSoup(img_url)
    img_html = img_soup.findAll('img',{'id':'mypicOne'})
    img_addr = urllib.urlopen(img_html[0]['src']).read()
    return HttpResponse(img_addr,mimetype="image/png")