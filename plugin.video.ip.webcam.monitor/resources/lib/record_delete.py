import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import shutil

__settings__ = xbmcaddon.Addon(id="plugin.video.ip.webcam.monitor")

addon_icon = 'special://home/addons/plugin.video.ip.webcam.monitor/icon.png'

c_rec = 'special://home/addons/plugin.video.ip.webcam.monitor/resources/tmp'
c_rec = xbmc.translatePath(c_rec)

try:
    shutil.rmtree(c_rec)
    os.mkdir(c_rec)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33011), 5000, addon_icon))
except:
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33012), 5000, addon_icon))
