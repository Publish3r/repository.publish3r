import sys
import urllib
import urlparse
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

tplink = xbmcaddon.Addon('plugin.tplink.hs100')

__settings__ = xbmcaddon.Addon(id="plugin.tplink.hs100")

poweron_icon = 'special://home/addons/plugin.tplink.hs100/resources/lib/power-on.png'
poweroff_icon = 'special://home/addons/plugin.tplink.hs100/resources/lib/power-off.png'
ledon_icon = 'special://home/addons/plugin.tplink.hs100/resources/lib/led-on.png'
ledoff_icon = 'special://home/addons/plugin.tplink.hs100/resources/lib/led-off.png'
reboot_icon = 'special://home/addons/plugin.tplink.hs100/resources/lib/reboot.png'
reset_icon = 'special://home/addons/plugin.tplink.hs100/resources/lib/reset.png'

ip = __settings__.getSetting("ip")
port = __settings__.getSetting("port")

mode = args.get('mode', None)

if mode is None:
    
    url = build_url({'mode': 'poweron', 'foldername': "POWER: ON"})
    li = xbmcgui.ListItem("POWER: ON", iconImage=poweron_icon, thumbnailImage=poweron_icon)
    li.setInfo(type='video', infoLabels={'plot': "POWER: ON"})
    li.setArt({'fanart': tplink.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    url = build_url({'mode': 'poweroff', 'foldername': "POWER: OFF"})
    li = xbmcgui.ListItem("POWER: OFF", iconImage=poweroff_icon, thumbnailImage=poweroff_icon)
    li.setInfo(type='video', infoLabels={'plot': "POWER: OFF"})
    li.setArt({'fanart': tplink.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)     

    url = build_url({'mode': 'ledon', 'foldername': "LED: ON"})
    li = xbmcgui.ListItem("LED: ON", iconImage=ledon_icon, thumbnailImage=ledon_icon)
    li.setInfo(type='video', infoLabels={'plot': "LED: ON"})
    li.setArt({'fanart': tplink.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    url = build_url({'mode': 'ledoff', 'foldername': "LED: OFF"})
    li = xbmcgui.ListItem("LED: OFF", iconImage=ledoff_icon, thumbnailImage=ledoff_icon)
    li.setInfo(type='video', infoLabels={'plot': "LED: OFF"})
    li.setArt({'fanart': tplink.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    url = build_url({'mode': 'reboot', 'foldername': "REBOOT"})
    li = xbmcgui.ListItem("REBOOT", iconImage=reboot_icon, thumbnailImage=reboot_icon)
    li.setInfo(type='video', infoLabels={'plot': "REBOOT"})
    li.setArt({'fanart': tplink.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    url = build_url({'mode': 'reset', 'foldername': "RESET"})
    li = xbmcgui.ListItem("RESET", iconImage=reset_icon, thumbnailImage=reset_icon)
    li.setInfo(type='video', infoLabels={'plot': "RESET"})
    li.setArt({'fanart': tplink.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'poweron':
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.tplink.hs100/resources/lib/tplink_smartplug.py", "-t", '+ip+', "-p", '+port+', "-c", "on")')
    xbmc.executebuiltin('Container.Refresh')

elif mode[0] == 'poweroff':
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.tplink.hs100/resources/lib/tplink_smartplug.py", "-t", '+ip+', "-p", '+port+', "-c", "off")')
    xbmc.executebuiltin('Container.Refresh')

elif mode[0] == 'ledon':
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.tplink.hs100/resources/lib/tplink_smartplug.py", "-t", '+ip+', "-p", '+port+', "-c", "ledon")')
    xbmc.executebuiltin('Container.Refresh')

elif mode[0] == 'ledoff':
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.tplink.hs100/resources/lib/tplink_smartplug.py", "-t", '+ip+', "-p", '+port+', "-c", "ledoff")')
    xbmc.executebuiltin('Container.Refresh')

elif mode[0] == 'reboot':
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.tplink.hs100/resources/lib/tplink_smartplug.py", "-t", '+ip+', "-p", '+port+', "-c", "reboot")')
    xbmc.executebuiltin('Container.Refresh')

elif mode[0] == 'reset':
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.tplink.hs100/resources/lib/tplink_smartplug.py", "-t", '+ip+', "-p", '+port+', "-c", "reset")')
    xbmc.executebuiltin('Container.Refresh')