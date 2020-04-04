import xbmc
import xbmcgui
title = xbmc.getInfoLabel('ListItem.Title')
if '[COLOR blue]' in title:
 title = title[33:]
tracklist = xbmc.getInfoLabel('ListItem.Plot')
dialog = xbmcgui.Dialog()
dialog.textviewer(title, tracklist)
