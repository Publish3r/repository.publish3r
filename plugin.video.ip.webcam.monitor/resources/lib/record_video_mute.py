import sys
import xbmcvfs
import time
import datetime
import xbmcgui
import xbmcplugin
import xbmcaddon
import subprocess
import os
import requests

__settings__ = xbmcaddon.Addon(id="plugin.video.ip.webcam.monitor")

addon_icon = 'special://home/addons/plugin.video.ip.webcam.monitor/icon.png'

ts = time.time()
c_ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

c_rec = 'special://home/addons/plugin.video.ip.webcam.monitor/resources/tmp/Video-' + c_ts + '.mkv'
c_rec = xbmc.translatePath(c_rec)

c_ip = __settings__.getSetting("ip")
c_port = __settings__.getSetting("port")
c_username = __settings__.getSetting("username").decode('utf-8')
c_password = __settings__.getSetting("password").decode('utf-8')
c_folder = __settings__.getSetting("folder")
c_audiomodus = __settings__.getSetting("audiomodus")
c_dauer = __settings__.getSetting("dauer").decode('utf-8')
c_folder = xbmc.translatePath(c_folder)

if c_username == "" or c_password == "":
    c_url = 'http://' + c_ip + ':' + c_port + '/'
else:
    c_url = 'http://' + c_username + ':' + c_password + '@' + c_ip + ':' + c_port + '/'

url_audio = c_url + 'audio.wav'
url_video = c_url + 'video'

if not ':' in c_dauer:
    c_dauer = '00:15:00'

try:
    _ = requests.get(c_url, timeout=1)
    os.chdir(c_folder)
    subprocess.Popen('ffmpeg -framerate 8 -f mjpeg -i ' + url_video + ' -c:v libx264 -r 25 -t ' +c_dauer+ ' ' + c_rec, shell=True)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33013), 5000, addon_icon))
except requests.ConnectionError:    
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33014), 5000, addon_icon))
