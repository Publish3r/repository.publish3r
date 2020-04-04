import xbmc
cover = xbmc.getInfoLabel('ListItem.Icon')
xbmc.executebuiltin('ShowPicture('+cover+')')
