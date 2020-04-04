#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import xbmcaddon
import os
import requests
import xbmc
import xbmcgui
import urllib
import urllib2
import re
import xbmcplugin

rar = xbmcaddon.Addon('plugin.video.rockamring')

addon = xbmcaddon.Addon()

addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')

script_file = os.path.realpath(__file__).decode('utf-8')
addondir = os.path.dirname(script_file).decode('utf-8')

path = xbmc.translatePath('special://home/addons/plugin.video.rockamring/resources/').decode('utf-8')

def CATEGORIES():
   addDir1('[B]Rock am Ring [COLOR blue]07.-09.06.2019[/COLOR][/B]','','1',path+'info.png')
   addDir2('Streams [COLOR blue](2019)[/COLOR]','https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/streams.txt',3,path+'play.png')
   addDir2('Replays [COLOR blue](2019)[/COLOR]','https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/replays.txt',7,path+'replays.png')
   addDir2('Line-up [COLOR blue](2019)[/COLOR]','https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/lineup.txt',2,path+'lineup.png')
   addDir2('Programm von Freitag [COLOR blue](07.06.2019)[/COLOR]','https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/freitag.txt',4,path+'programm.png')
   addDir2('Programm von Samstag [COLOR blue](08.06.2019)[/COLOR]','https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/samstag.txt',5,path+'programm.png')
   addDir2('Programm von Sonntag [COLOR blue](09.06.2019)[/COLOR]','https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/sonntag.txt',6,path+'programm.png')

def lineup():
   r = requests.get('https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/lineup.txt')
   match = re.compile('name= (.+?) logo= "(.+?)"').findall(r.content)
   for name,logo in match:
     name = name.decode('utf-8')
     addLink(name,logo,'','')

def livestreams():
   r = requests.get('https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/streams.txt')
   match = re.compile('name= (.+?) url= "(.+?)"').findall(r.content)
   for name,url in match:
     addLink_livestreams(name,url,path+'live.png','','')

def replays():
   r = requests.get('https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/replays.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,url,logo in match:
     name = name.decode('utf-8')
     addLink_replays(name,url,logo,'','')

def freitag():
   r = requests.get('https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/freitag.txt')
   match = re.compile('stage= (.+?) zeit= "(.+?)" name= "(.+?)" image= "(.+?)"').findall(r.content)
   for stage,zeit,name,image in match:
     addLink_programm(stage,zeit,name,image,'','')

def samstag():
   r = requests.get('https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/samstag.txt')
   match = re.compile('stage= (.+?) zeit= "(.+?)" name= "(.+?)" image= "(.+?)"').findall(r.content)
   for stage,zeit,name,image in match:
     addLink_programm(stage,zeit,name,image,'','')

def sonntag():
   r = requests.get('https://raw.githubusercontent.com/Publish3r/repository.publish3r/master/plugin.video.rockamring/resources/sonntag.txt')
   match = re.compile('stage= (.+?) zeit= "(.+?)" name= "(.+?)" image= "(.+?)"').findall(r.content)
   for stage,zeit,name,image in match:
     addLink_programm(stage,zeit,name,image,'','')

def addLink(name,image,urlType,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": name } )
        liz.setProperty('IsPlayable','false')
	liz.setArt({'poster': image, 'fanart': rar.getAddonInfo('fanart')})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url='',listitem=liz)

def addLink_livestreams(name,url,image,urlType,fanart):
        request = requests.get(url, timeout=2)
        if request.status_code == 200:
            titel = 'Rock am Ring [COLOR blue]('+name+')[/COLOR]'
            name = name+' [COLOR blue](online)[/COLOR]'
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
            liz.setInfo( type="Video", infoLabels={ "Title": titel, "plot": name } )
            liz.setProperty('IsPlayable','true')
	    liz.setArt({'poster': image, 'fanart': rar.getAddonInfo('fanart')})
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        else:
            name = name+' [COLOR blue](offline)[/COLOR]'
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
            liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": name } )
            liz.setProperty('IsPlayable','false')
	    liz.setArt({'poster': image, 'fanart': rar.getAddonInfo('fanart')})
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)

def addLink_replays(name,url,image,urlType,fanart):
        titel = 'Rock am Ring '+name
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": titel, "plot": name } )
        liz.setProperty('IsPlayable','true')
	liz.setArt({'poster': image, 'fanart': rar.getAddonInfo('fanart')})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)

def addLink_programm(stage,zeit,name,image,urlType,fanart):
        name = stage+' [COLOR blue]'+zeit+'[/COLOR] '+name
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": name } )
        liz.setProperty('IsPlayable','false')
	liz.setArt({'poster': image, 'fanart': rar.getAddonInfo('fanart')})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url='',listitem=liz)

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
      

def addDir1(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": name } )
        liz.setArt({'fanart': rar.getAddonInfo('fanart')})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok 

def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": name } )
        liz.setArt({'fanart': rar.getAddonInfo('fanart')})
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
        CATEGORIES()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
       
elif mode==1:
        OPEN_URL(url)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==2:
        lineup()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==3:
        livestreams()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==4:
        freitag()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==5:
        samstag()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==6:
        sonntag()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==7:
        replays()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
