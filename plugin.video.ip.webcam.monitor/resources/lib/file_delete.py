import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
import os

__settings__ = xbmcaddon.Addon(id="plugin.video.ip.webcam.monitor")

addon_icon = 'special://home/addons/plugin.video.ip.webcam.monitor/icon.png'

datei = xbmc.getInfoLabel('ListItem.FileNameAndPath')

try:
    os.remove(datei)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33009), 5000, addon_icon))
except:
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('IP Webcam Monitor', __settings__.getLocalizedString(33010), 5000, addon_icon))

xbmc.executebuiltin('Container.Refresh')
