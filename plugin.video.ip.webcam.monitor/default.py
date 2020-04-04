import sys
import urllib
import urlparse
import requests
import time
import datetime
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
addon = xbmcaddon.Addon()

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

ipwebcammonitor = xbmcaddon.Addon('plugin.video.ip.webcam.monitor')

__settings__ = xbmcaddon.Addon(id="plugin.video.ip.webcam.monitor")

addon_icon = 'special://home/addons/plugin.video.ip.webcam.monitor/icon.png'

ts = time.time()
c_ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

c_ip = __settings__.getSetting("ip")
c_port = __settings__.getSetting("port")
c_username = __settings__.getSetting("username").decode('utf-8')
c_password = __settings__.getSetting("password").decode('utf-8')
c_folder = __settings__.getSetting("folder").decode('utf-8')
c_audiomodus = __settings__.getSetting("audiomodus")

if c_username == "" or c_password == "":
    c_url = 'http://' + c_ip + ':' + c_port + '/'
else:
    c_url = 'http://' + c_username + ':' + c_password + '@' + c_ip + ':' + c_port + '/'

errorline1 = __settings__.getLocalizedString(33001)
errorline2 = __settings__.getLocalizedString(33002)

c_rec = 'special://home/addons/plugin.video.ip.webcam.monitor/resources/tmp/'
c_rec = xbmc.translatePath(c_rec).decode('utf-8')

def c_fanart(url=c_url, timeout=1):
    try:
        _ = requests.get(url, timeout=timeout)
        li.setArt({'fanart': c_url + 'shot.jpg?timestamp=' + c_ts})
        return True
    except requests.ConnectionError:
        li.setArt({'fanart': ipwebcammonitor.getAddonInfo('fanart')})
    return False

def c_videostream(url=c_url, timeout=1):
    try:
        _ = requests.get(url, timeout=timeout)
        info = {
            'genre': 'Livestream',
            'title': 'IP Webcam Monitor - Videostream',
        }
        listitem = xbmcgui.ListItem('IP Webcam Monitor - Videostream', iconImage=addon_icon, thumbnailImage=addon_icon)
        listitem.setInfo('video', info)
        xbmc.Player().play(c_url + 'video', listitem)
        return True
    except requests.ConnectionError:
        xbmcgui.Dialog().ok(errorline1, errorline2)
    return False

def c_aufnahme(url=c_url, timeout=1):
    listitem = xbmcgui.ListItem('IP Webcam Monitor - Videostream', iconImage=addon_icon, thumbnailImage=addon_icon)
    xbmc.Player().play(c_url + 'video', listitem)
     
def c_audiostream(url=c_url, timeout=1):
    try:
        _ = requests.get(url, timeout=timeout)
        info = {
            'genre': 'Livestream',
            'title': 'IP Webcam Monitor - Audiostream',
        }
        listitem = xbmcgui.ListItem('IP Webcam Monitor - Audiostream', iconImage=addon_icon, thumbnailImage=addon_icon)
        listitem.setInfo('music', info)
        xbmc.Player().play(c_url + 'audio.wav', listitem)
        return True
    except requests.ConnectionError:
        xbmcgui.Dialog().ok(errorline1, errorline2)
    return False

def c_snapshot(url=c_url, timeout=1):
    try:
        _ = requests.get(url, timeout=timeout)
        snap = c_url + 'shot.jpg?timestamp=' + c_ts
        xbmc.executebuiltin('ShowPicture('+snap+')') 
    except requests.ConnectionError:
        xbmcgui.Dialog().ok(errorline1, errorline2)
    return False

def c_aufnahmen():
    for match in os.listdir(c_rec):
        li = xbmcgui.ListItem(match, iconImage=addon_icon, thumbnailImage=addon_icon)
        li.addContextMenuItems([('[COLOR blue]'+__settings__.getLocalizedString(33003)+'[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.ip.webcam.monitor/resources/lib/file_delete.py)',),]) 
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=c_rec+match, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)

mode = args.get('mode', None)

if mode is None:
    
    url = build_url({'mode': 'snapshot', 'foldername': 'Snapshot'})
    li = xbmcgui.ListItem('Snapshot', iconImage=addon_icon, thumbnailImage=addon_icon)
    li.setInfo(type='video', infoLabels={'plot': 'Snapshot'})
    c_fanart()
    li.addContextMenuItems([('[COLOR blue]Overlay[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.ip.webcam.monitor/resources/lib/overlay.py)',),]) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    if c_audiomodus == "true":
        url = build_url({'mode': 'videostream', 'foldername': 'Videostream'})
        li = xbmcgui.ListItem('Videostream', iconImage=addon_icon, thumbnailImage=addon_icon)
        li.setInfo(type='video', infoLabels={'title': 'IP Webcam Monitor - Videostream', 'plot': 'Videostream'})
        li.setArt({'fanart': ipwebcammonitor.getAddonInfo('fanart')}) 
        li.addContextMenuItems([('[COLOR blue]'+__settings__.getLocalizedString(33004)+'[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.ip.webcam.monitor/resources/lib/record_video.py)',),])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)
    else:
        url = build_url({'mode': 'videostream', 'foldername': 'Videostream'})
        li = xbmcgui.ListItem('Videostream', iconImage=addon_icon, thumbnailImage=addon_icon)
        li.setInfo(type='video', infoLabels={'title': 'IP Webcam Monitor - Videostream', 'plot': 'Videostream'})
        li.setArt({'fanart': ipwebcammonitor.getAddonInfo('fanart')}) 
        li.addContextMenuItems([('[COLOR blue]'+__settings__.getLocalizedString(33004)+'[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.ip.webcam.monitor/resources/lib/record_video_mute.py)',),])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    if c_audiomodus == "true":
        url = build_url({'mode': 'audiostream', 'foldername': 'Audiostream'})
        li = xbmcgui.ListItem('Audiostream', iconImage=addon_icon, thumbnailImage=addon_icon)
        li.setInfo(type='video', infoLabels={'title': 'IP Webcam Monitor - Audiostream', 'plot': 'Audiostream'})
        li.setArt({'fanart': ipwebcammonitor.getAddonInfo('fanart')}) 
        li.addContextMenuItems([('[COLOR blue]'+__settings__.getLocalizedString(33005)+'[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.ip.webcam.monitor/resources/lib/record_audio.py)',),]) 
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    url = build_url({'mode': 'aufnahmen', 'foldername': __settings__.getLocalizedString(33006)})
    li = xbmcgui.ListItem(__settings__.getLocalizedString(33006), iconImage=addon_icon, thumbnailImage=addon_icon)
    li.setInfo(type='video',infoLabels={'title': __settings__.getLocalizedString(33006), 'plot': __settings__.getLocalizedString(33006)})
    li.setArt({'fanart': ipwebcammonitor.getAddonInfo('fanart')}) 
    li.addContextMenuItems([('[COLOR blue]'+__settings__.getLocalizedString(33007)+'[/COLOR]', 'XBMC.RunScript(special://home/addons/plugin.video.ip.webcam.monitor/resources/lib/record_delete.py)',),]) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)    

    url = build_url({'mode': 'settings', 'foldername': __settings__.getLocalizedString(33008)})
    li = xbmcgui.ListItem(__settings__.getLocalizedString(33008), iconImage=addon_icon, thumbnailImage=addon_icon)
    li.setInfo(type='video', infoLabels={'plot': __settings__.getLocalizedString(33008)})
    li.setArt({'fanart': ipwebcammonitor.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'videostream':
    c_videostream()

elif mode[0] == 'audiostream':
    c_audiostream()

elif mode[0] == 'snapshot':
    c_snapshot()

elif mode[0] == 'aufnahmen':
    c_aufnahmen()

elif mode[0] == 'settings':
    addon.openSettings()
    xbmc.executebuiltin('Container.Refresh')

