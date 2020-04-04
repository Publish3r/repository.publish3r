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

c_rec = 'special://home/addons/plugin.video.ip.webcam.monitor/resources/tmp/Audio-' + c_ts + '.mp3'
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

url = c_url + 'audio.wav'

if not ':' in c_dauer:
    c_dauer = '00:15:00'

try:
    _ = requests.get(c_url, timeout=1)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33013), 5000, addon_icon))
    os.chdir(c_folder)
    subprocess.Popen('ffmpeg -i ' + url + ' -t ' +c_dauer+ ' ' + c_rec, shell=True)
except requests.ConnectionError:
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33014), 5000, addon_icon))
