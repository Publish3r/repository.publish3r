#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin
import YDStreamUtils
import YDStreamExtractor
YDStreamExtractor.disableDASHVideo(True)

philizzmedia = xbmcaddon.Addon('plugin.video.philizz.media')

addon = xbmcaddon.Addon()

addonname = addon.getAddonInfo('name')
addonicon = addon.getAddonInfo('icon')

script_file = os.path.realpath(__file__).decode('utf-8')
addondir = os.path.dirname(script_file).decode('utf-8')

icon = 'special://home/addons/plugin.video.philizz.media/folder.png'

commands = []
commands.append(('[COLOR blue]Show Cover[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.philizz.media/cover.py)',))
commands.append(('[COLOR blue]Show Tracklist[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.philizz.media/tracklist.py)',))

def MENU():
    addDir('Latest','-',12,icon,'','Latest')
    addDir('Yearmixes','-',2,icon,'','Yearmixes')
    addDir('Videomixes','-',3,icon,'','Videomixes')
    addDir('Heroes Of The 00s','-',7,icon,'','Heroes Of The 00s')
    addDir('Back To The 90s','-',8,icon,'','Back To The 90s')
    addDir('I Covered The 80s','-',9,icon,'','I Covered The 80s')
    addDir('Specials','-',10,icon,'','Specials')
    addDir('Minimix Adventures','-',11,icon,'','Minimix Adventures')

def LATEST():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<article class="item" data-permalink="(.*?)">').findall(r.content)
    for match in matches:
     content = requests.get(match)
     published = re.compile('<time datetime="(.*?)" pubdate>').findall(content.content)[0]
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     name = '[COLOR blue]('+published+')[/COLOR] '+name
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<h2>Tracklist:</h2>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '</p>' , '' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def YEARMIXES():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/yearmix-(.*?)" class="level1">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/yearmix-'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<h2>Tracklist:</h2>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<p><strong>Tracklist:</strong></p>(.*?)ay</p>', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( 'Sigma – St' , 'Sigma – Stay' )
      desc = desc . replace ( '<p>Shawn' , 'Shawn' )
      desc = desc . replace ( '<p>Part 1:</p>' , '<p>Part 1:[CR]' )
      desc = desc . replace ( '<p><br />Part 2:</p>' , '[CR]Part 2:' )
      desc = desc . replace ( '<p>Zayn' , '[CR]Zayn' )
     except:
      pass
     try:
      desc = re.compile('<p><strong>Tracklist:</strong></p>(.*?)lo</p>', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( 'Adele - Hel' , 'Adele - Hello' )
     except:
      pass
     try:
      desc = re.compile('<p><span style="text-decoration: underline;"><strong>Tracklist:</strong></span></p>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<p>Intro with DJ Moradzo (.*?)Sento</p>', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( 'Vocals Alesha Dixon' , '<p>Intro with DJ Moradzo Vocals Alesha Dixon' )
      desc = desc . replace ( 'Weinst Du Scooter – Ti ' , 'Weinst Du Scooter – Ti Sento' )
     except:
      pass
     try:
      desc = re.compile('<p>Intro – Gu(.*?)l Stay ', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( 'ru Josh' , '<p>Intro – Guru Josh' )
      desc = desc . replace ( '– Say You’l' , '– Say You’ll Stay' )
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '</p>' , '' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def VIDEOMIXESDIR():
    addDir('Videomixes 2013','-',4,icon,'','Videomixes 2013')
    addDir('Videomixes 2012','-',5,icon,'','Videomixes 2012')
    addDir('Videomixes 2011','-',6,icon,'','Videomixes 2011')

def VIDEOMIXES2013():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/videomix-2013/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/videomix-2013/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<p><span style="text-decoration: underline;"><strong>Tracklist:</strong></span></p>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def VIDEOMIXES2012():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/videomix-2012/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/videomix-2012/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<h2>Tracklist Volume 1</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist Volume 2</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<p>Tracklist(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( ': <br />' , '<p>' )
     except:
      pass
     try:
      desc = re.compile('<strong>Tracklist:</strong></span></p>(.*?)</p>', re.DOTALL).findall(content.content)[0] 
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def VIDEOMIXES2011():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/videomix-2011/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/videomix-2011/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<h2>Tracklist Volume 1</h2>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist Volume 2</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist Volume 3</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist Volume 4</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist Volume 5</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def ZEROS():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/heroes-of-the-00s/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/heroes-of-the-00s/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<h2>Tracklist:</h2>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def NINETIES():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/back-to-the-90s/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/back-to-the-90s/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<h2>Tracklist:</h2>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def EIGHTIES():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/i-covered-the-80s/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/i-covered-the-80s/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     url = re.compile('http(.*?)mp4').findall(content.content)[0]
     url = 'http'+url+'mp4'
     if ' ' in url:
      url = url.replace(" ", "%20")
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<p><strong>Tracklist:<br /></strong></p>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def SPECIALS():
    r = requests.get('http://philizz.nl/tropical-summer-2016')
    desc = re.compile('<p>Twenty One Pilots - Stress(.*?)</p>', re.DOTALL).findall(r.content)[0]
    desc = desc . replace ( 'ed Out' , '[B]Tracklist:[/B][CR]Twenty One Pilots - Stressed Out' )
    desc = desc . replace ( '<br />' , '[CR]' )
    addLink('Tropical Summer 2016','http://philizz.nl/videos/tropical.mp4','http://philizz.nl/images/philizz/thumbnails/Philizz_-_Tropical_Summer_2016.jpg',desc,'','')
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/specials/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/specials/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     try:
      url = re.compile('http(.*?)mp4').findall(content.content)[0]
      url = 'http'+url+'mp4'
      if ' ' in url:
       url = url.replace(" ", "%20")
     except:
      urlpart = re.compile('com\/video\/(.*?)\?').findall(content.content)[0]
      url = 'https://vimeo.com/'+urlpart
     try:
      image = re.compile('href="/images/(.*?)"').findall(content.content)[0]
      image = 'http://philizz.nl/images/'+image
      if ' ' in image:
       image = image.replace(" ", "%20")
     except:
      image = addonicon
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('<h2>Tracklist:</h2>(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist:</h2>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('server=" target="_blank">Click here</a><br /></span></p>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<p>Tracklist:<br />(.*?)<br /><br />', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( '<br />Oli' , "<p>Oli" )
     except:
      pass
     try:
      desc = re.compile('<h2>Tracklist</h2>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<p><strong>Tracklist</strong>:(.*?)</p>', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( '<br />1.' , "<p>1." )
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def MINIMIXES():
    r = requests.get('http://philizz.nl')
    matches = re.compile('<a href="/philizz-ft-dj-ic/(.*?)" class="level2">').findall(r.content)
    for match in matches:
     link = 'http://philizz.nl/philizz-ft-dj-ic/'+match
     content = requests.get(link)
     name = re.compile('<h1 class="title">(.*?)<').findall(content.content)[0]
     try:
      url = re.compile('http(.*?)mp4').findall(content.content)[0]
      url = 'http'+url+'mp4'
      if ' ' in url:
       url = url.replace(" ", "%20")
     except:
      urlpart = re.compile('com\/video\/(.*?)\?').findall(content.content)[0]
      url = 'https://vimeo.com/'+urlpart
     image = 'http://philizz.nl/images/philizz/djic-philizz.jpg'
     desc = 'Tracklist not found.'
     try:
      desc = re.compile('Tracklist</span>:</strong></p>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     try:
      desc = re.compile('<p><strong>Tracklist:<br />(.*?)</p>', re.DOTALL).findall(content.content)[0]
      desc = desc . replace ( '</strong>' , "<p>" )
     except:
      pass
     try:
      desc = re.compile('<p><strong>Tracklist:<br /></strong></p>(.*?)</p>', re.DOTALL).findall(content.content)[0]
     except:
      pass
     desc = desc . replace ( '<p>' , '[B]Tracklist:[/B][CR]' )
     desc = desc . replace ( '<br /> ' , '<br />' )
     desc = desc . replace ( '<br />' , '[CR]' )
     desc = desc . replace ( '&quot;' , '"' )
     desc = desc . replace ( '&rsquo;' , "'" )
     desc = desc . replace ( '&amp;' , "&" )
     addLink(name,url,image,desc,'','')

def addLink(name,url,image,desc,urlType,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        if not 'mp4' in url:
         url = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=13&name="+name+"&description="+desc+"&iconimage="+image
         liz.setProperty('IsPlayable','false')
        else:
         url = url
         liz.setProperty('IsPlayable','true')
        liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": desc } )
	liz.setArt({'poster': image, 'fanart': philizzmedia.getAddonInfo('fanart')})
        liz.addContextMenuItems(commands)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param               

def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setArt({'fanart': philizzmedia.getAddonInfo('fanart')})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
            
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        MENU()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1:
        OPEN_URL(url)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==2:
        print ""
        YEARMIXES()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==3:
        print ""
        VIDEOMIXESDIR()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==4:
        print ""
        VIDEOMIXES2013()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==5:
        print ""
        VIDEOMIXES2012()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==6:
        print ""
        VIDEOMIXES2011()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==7:
        print ""
        ZEROS()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==8:
        print ""
        NINETIES()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==9:
        print ""
        EIGHTIES()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==10:
        print ""
        SPECIALS()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==11:
        print ""
        MINIMIXES()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==12:
        print ""
        LATEST()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==13:
        url = str(url)
        title = str(name)
        plot = str(description)
        pic = str(iconimage)
        try:
         vid = YDStreamExtractor.getVideoInfo(url,quality=1)
         url = vid.streamURL()
         listitem=xbmcgui.ListItem(title, iconImage=pic, thumbnailImage=pic)
         listitem.setInfo( type="Video", infoLabels={ "Title": title, "plot": plot } )
         xbmc.Player().play(url, listitem)
        except:
         xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('[B]Error[/B]', 'Video not found.', 5000, addonicon))
