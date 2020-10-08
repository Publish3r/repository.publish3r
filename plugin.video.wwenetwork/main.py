from resources.lib.wwenetwork import *

params = get_params()
mode = None
content_id = None
content_name = None
path = None
year = None
sub_filter = None
season_id = None
start_point = None

if 'name' in params:
    name = urllib.unquote_plus(params["name"])

if 'mode' in params:
    mode = int(params["mode"])

if 'content_id' in params:
    content_id = urllib.unquote_plus(params["content_id"])

if 'content_name' in params:
    content_name = urllib.unquote_plus(params["content_name"])

if 'path' in params:
    path = urllib.unquote_plus(params["path"])

if 'year' in params:
    year = urllib.unquote_plus(params["year"])

if 'sub_filter' in params:
    sub_filter = urllib.unquote_plus(params["sub_filter"])

if 'season_id' in params:
    season_id = urllib.unquote_plus(params["season_id"])

if 'start_point' in params:
    start_point = urllib.unquote_plus(params["start_point"])

if mode is None or mode == 0:
    account = Account()
    if(account.login_token == ''):
        account.login()
    categories()

elif mode == 100:
    list_page(content_id)

elif mode == 101:
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_DATE)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_DURATION)
    xbmcplugin.setContent(addon_handle, 'episodes')
    fetch_list(content_id)

elif mode == 103:
    play_event(content_id, content_name)

elif mode == 104:
    play_vod(content_id, content_name, start_point)

elif mode == 105:
    list_filters(path,sub_filter)

elif mode == 106:
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_DATE)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_DURATION)
    xbmcplugin.setContent(addon_handle, 'episodes')
    fetch_episodes(content_id, year, season_id)

elif mode == 107:
    list_seasons(content_id, path)

elif mode == 108:
    list_decider(content_id,path)

elif mode == 109:
    search_term = xbmcgui.Dialog().input('Search')
    if search_term:
        search(search_term)

elif mode == 110:
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_DATE)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_DURATION)
    list_search_results(content_id, path)

elif mode == 400:
    account = Account()
    account.logout()
    dialog = xbmcgui.Dialog()
    title = "Logout Successful"
    dialog.notification(title, 'Logout completed successfully', ICON, 5000, False)
    sys.exit()

elif mode == 500:
    xbmcaddon.Addon('inputstream.adaptive').openSettings()

elif mode == 999:
    sys.exit()

if mode == 200:
    xbmcplugin.endOfDirectory(addon_handle, cacheToDisc=False)
elif mode == 201:
    xbmcplugin.endOfDirectory(addon_handle, cacheToDisc=False, updateListing=True)
else:
    xbmcplugin.endOfDirectory(addon_handle)
