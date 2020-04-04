import xbmcgui
import sys
import os
import subprocess
import xbmc
import xbmcaddon
import requests
import random
import ftplib
import xbmcvfs
import gzip
import shutil
from time import sleep
from shutil import copyfile

addon = xbmcaddon.Addon()

addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
settings = xbmcaddon.Addon(id="script.rytec.epg.downloader")

speicherort = settings.getSetting("folder").decode('utf-8')
datei = settings.getSetting("outputname").decode('utf-8')
epgcompress = settings.getSetting("epgcompress")

if epgcompress == "false":
    dateiname = datei+'.xml'
else:
    dateiname = datei+'.xml.gz'

webgrabstatus = settings.getSetting("webgrabstatus")
webgrabexe = settings.getSetting("webgrablocation").decode('utf-8')
webgrabxml = settings.getSetting("webgrabfile").decode('utf-8')
webgrabcorrecttime = settings.getSetting("webgrabcorrecttime").decode('utf-8')

ftpstatus = settings.getSetting("ftpstatus")
ftpserver = settings.getSetting("ftpserver").decode('utf-8')
ftpuser = settings.getSetting("ftpuser").decode('utf-8')
ftppass = settings.getSetting("ftppass").decode('utf-8')
ftppath = settings.getSetting("ftppath").decode('utf-8')
ftpdelete = settings.getSetting("ftpdelete")

epgde = settings.getSetting("epgde")
epgat = settings.getSetting("epgat")
epgch = settings.getSetting("epgch")
epgbe = settings.getSetting("epgbe")
epgdk = settings.getSetting("epgdk")
epges = settings.getSetting("epges")
epgfr = settings.getSetting("epgfr")
epgit = settings.getSetting("epgit")
epgnl = settings.getSetting("epgnl")
epguk = settings.getSetting("epguk")
epgfi = settings.getSetting("epgfi")
epgno = settings.getSetting("epgno")
epgse = settings.getSetting("epgse")

script_file = os.path.realpath(__file__).decode('utf-8')
addondir = os.path.dirname(script_file).decode('utf-8')

server1 = 'http://www.xmltvepg.nl'
server2 = 'http://www.xmltvepg.nl'
server3 = 'http://www.xmltvepg.nl'

#server1 = 'http://rytecepg.ipservers.eu/epg_data'
#server2 = 'http://www.vuplus-community.net/rytec'
#server3 = 'http://www.xmltvepg.nl'
server_list = [server1, server2, server3]
rytecserver = (random.choice(server_list))

xml_path = 'special://home/addons/script.rytec.epg.downloader/resources/lib/download/'

time = 5000

nachricht1 = addon.getLocalizedString(30601)
nachricht2 = addon.getLocalizedString(30602)
nachricht3 = addon.getLocalizedString(30603)

errorline1 = addon.getLocalizedString(30604)
errorline2 = addon.getLocalizedString(30605)
errorline3 = addon.getLocalizedString(30606)
errorline4 = addon.getLocalizedString(30607)
errorline5 = addon.getLocalizedString(30608)
errorline6 = addon.getLocalizedString(30609)
errorline7 = addon.getLocalizedString(30610)
errorline8 = addon.getLocalizedString(30611)
errorline9 = addon.getLocalizedString(30612)

select1 = addon.getLocalizedString(30701)
select2 = addon.getLocalizedString(30702)
select3 = addon.getLocalizedString(30703)
select4 = addon.getLocalizedString(30704)
select5 = addon.getLocalizedString(30705)

if speicherort == "":
    addon.openSettings()
    sys.exit(0)
else:
    pass

if speicherort.startswith('smb'):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline6, time, icon))
    addon.openSettings()
    sys.exit(0)
else:
    pass

def rytec_clean():
    try:
        shutil.rmtree(addondir+'/resources/lib/download/', ignore_errors=True)
    except:
        pass
    try:
        os.makedirs(addondir+'/resources/lib/download/')
    except:
        pass

def rytec_clean_dl():
    try:
        shutil.rmtree(addondir+'/resources/lib/download/', ignore_errors=True)
    except:
        pass

def rytec_error():
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline1, time, icon))
    rytec_clean()
    rytec_menu()

def rytec_webgrabexe_error():
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline2, time, icon))
    rytec_clean()
    rytec_menu()

def rytec_webgrabxml_error():
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline3, time, icon))
    rytec_clean()
    rytec_menu()

def rytec_generator_error():
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline5, time, icon))
    rytec_menu()

def rytec_download():
    if epgde == "true":
        rytec_download_de()
    else:
        pass
    if epgat == "true":
        rytec_download_at()
    else:
        pass
    if epgch == "true":
        rytec_download_ch()
    else:
        pass
    if epgbe == "true":
        rytec_download_be()
    else:
        pass
    if epgdk == "true":
        rytec_download_dk()
    else:
        pass
    if epges == "true":
        rytec_download_es()
    else:
        pass
    if epgfr == "true":
        rytec_download_fr()
    else:
        pass
    if epgit == "true":
        rytec_download_it()
    else:
        pass
    if epgnl == "true":
        rytec_download_nl()
    else:
        pass
    if epguk == "true":
        rytec_download_uk()
    else:
        pass
    if epgfi == "true":
        rytec_download_fi()
    else:
        pass
    if epgno == "true":
        rytec_download_no()
    else:
        pass
    if epgse == "true":
        rytec_download_se()
    else:
        pass

def rytec_download_de():
    try:
        url = rytecserver+'/rytecDE_Common.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecDE_Common.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecDE_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecDE_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecDE_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecDE_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_at():
    try:
        url = rytecserver+'/rytecAT_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecAT_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_ch():
    try:
        url = rytecserver+'/rytecCH_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecCH_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_be():
    try:
        url = rytecserver+'/rytecBE_FR_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecBE_FR_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecBE_FR_Common.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecBE_FR_Common.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecBE_NL_Common.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecBE_NL_Common.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecBE_VL_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecBE_VL_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_dk():
    try:
        url = rytecserver+'/rytecDK_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecDK_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecDK_Misc.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecDK_Misc.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecDK_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecDK_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_es():
    try:
        url = rytecserver+'/rytecES_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecES_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecES_Misc.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecES_Misc.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecES_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecES_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_fr():
    try:
        url = rytecserver+'/rytecFR_Mixte.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecDE_Common.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecFR_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecFR_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_it():
    try:
        url = rytecserver+'/rytecIT_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecIT_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecIT_Sky.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecIT_Sky.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecIT_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecIT_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_nl():
    try:
        url = rytecserver+'/rytecNL_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecNL_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecNL_Extra.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecNL_Extra.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_uk():
    try:
        url = rytecserver+'/rytecUK_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecUK_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecUK_FTA.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecUK_FTA.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecUK_SkyDead.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecUK_SkyDead.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecUK_SkyLive.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecUK_SkyLive.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecUK_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecUK_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecUK_int.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecUK_int.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_fi():
    try:
        url = rytecserver+'/rytecFI_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecFI_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecFI_Misc.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecFI_Misc.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecFI_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecFI_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_no():
    try:
        url = rytecserver+'/rytecNO_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecNO_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecNO_Misc.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecNO_Misc.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecNO_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecNO_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_download_se():
    try:
        url = rytecserver+'/rytecSE_Basic.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecSE_Basic.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecSE_Misc.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecSE_Misc.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()
    try:
        url = rytecserver+'/rytecSE_SportMovies.xz'
        r = requests.get(url)
        with open(addondir+'/resources/lib/download/rytecSE_SportMovies.xz', 'wb') as f:
            f.write(r.content)
    except:
        rytec_error()

def rytec_extract():
    subprocess.Popen([addondir+'\\resources\\lib\\extract.bat'],shell=True).communicate()

def rytec_rename():
    for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
        for file in files:
            base_path, ext = os.path.splitext(os.path.join(root, file))

            if not ext:
                os.rename(base_path, base_path + ".xml")

def rytec_copy():
    if epgcompress == "false":
        rytec_copy_xml()
    else:
        rytec_copy_gz()

def rytec_copy_gz():
    if os.path.isfile(speicherort+''+dateiname):
        os.remove(speicherort+''+dateiname)
    else:
        pass
    if os.path.isfile(addondir+'/resources/lib/download/temp/merged_epg.xml.gz'):
        copyfile(addondir+'/resources/lib/download/temp/merged_epg.xml.gz', speicherort+''+dateiname)
    else:
        pass

def rytec_copy_xml():
    if os.path.isfile(speicherort+''+dateiname):
        os.remove(speicherort+''+dateiname)
    else:
        pass
    if os.path.isfile(addondir+'/resources/lib/merged_epg.xml.gz'):
        os.remove(addondir+'/resources/lib/merged_epg.xml.gz')
    else:
        pass
    if os.path.isfile(addondir+'/resources/lib/merged_epg.xml'):
        os.remove(addondir+'/resources/lib/merged_epg.xml')
    else:
        pass
    if os.path.isfile(addondir+'/resources/lib/download/temp/merged_epg.xml.gz'):
        copyfile(addondir+'/resources/lib/download/temp/merged_epg.xml.gz', addondir+'/resources/lib/merged_epg.xml.gz')
        subprocess.Popen([addondir+'\\resources\\lib\\decompress.bat'],shell=True).communicate()
        sleep(1)
        rytec_move_xml()    
    else:
        pass

def rytec_move_xml():
    if os.path.isfile(addondir+'/resources/lib/merged_epg.xml'):
        copyfile(addondir+'/resources/lib/merged_epg.xml', speicherort+''+dateiname)
    else:
        pass
    sleep(1)
    if os.path.isfile(addondir+'/resources/lib/merged_epg.xml.gz'):
        os.remove(addondir+'/resources/lib/merged_epg.xml.gz')
    else:
        pass
    if os.path.isfile(addondir+'/resources/lib/merged_epg.xml'):
        os.remove(addondir+'/resources/lib/merged_epg.xml')
    else:
        pass

def rytec_webgrab_check():
    if webgrabstatus == "true":
        rytec_webgrab()
    else:
        pass

def rytec_webgrab():
    if webgrabexe == "" and webgrabxml == "":
        pass
    else:
        try:
            subprocess.Popen([webgrabexe],shell=True).communicate()
        except:
            rytec_webgrabexe_error()

    if webgrabcorrecttime == "":
        pass
    else:
        try:
            subprocess.Popen([webgrabcorrecttime],shell=True).communicate()
        except:
            rytec_webgrabexe_error()

    if os.path.isfile(webgrabxml):
        try:
            copyfile(webgrabxml, addondir+'/resources/lib/download/webgrab.xml')
        except:
            rytec_webgrabxml_error()
    else:
        pass

def rytec_ftp_check():
    if ftpstatus == "true":
        rytec_ftp_upload()
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline7, time, icon))
        rytec_menu()

def rytec_ftp_upload():
    if ftpserver != "" and ftpuser != "" and ftppass != "":
        rytec_ftp_file_check()
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline8, time, icon))
        rytec_menu()

def rytec_ftp_file_check():
    if os.path.isfile(speicherort+''+dateiname):
        rytec_ftp_upload_start()
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline9, time, icon))
        rytec_menu()

def rytec_ftp_upload_start():
    try:
        session = ftplib.FTP(ftpserver,ftpuser,ftppass)
        file = open(speicherort+''+dateiname,'rb')
        session.cwd(ftppath)
        session.storbinary('STOR ' +dateiname, file)
        file.close()
        session.quit()
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, nachricht2, time, icon))
        rytec_ftp_upload_clean()
    except ftplib.all_errors, e:
        errorcode_string = str(e).split(None, 1)[0]
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, errorline4+' Code: '+errorcode_string, time, icon))
        rytec_menu()

def rytec_ftp_upload_clean():
    if ftpdelete == "true":
        try:
            os.remove(speicherort+''+dateiname)
        except:
            pass
    rytec_menu()        

def get_merged():
    merged = os.path.join(xml_path,'merged_epg.xml.gz')
    if xbmcvfs.exists(merged):
        xbmcvfs.delete(merged)
    return merged
    
def get_temp_merged():
    datapath = xbmc.translatePath('special://home/addons/script.rytec.epg.downloader/resources/lib/download/')
    temp = os.path.join(datapath,'temp')
    if not xbmcvfs.exists(temp):
        xbmcvfs.mkdir(temp)
    temp_merged = os.path.join(temp, 'merged_epg.xml.gz')
    return temp_merged

def copy_temp_merged():
    merged = get_merged()
    temp_merged = get_temp_merged()
    xbmcvfs.copy(temp_merged, merged)

def delete_temp_merged():
    temp_merged = get_temp_merged()
    if xbmcvfs.exists(temp_merged):
        xbmcvfs.delete(temp_merged)

def get_xml_file(name):
    xml_file = os.path.join(xml_path, name)
    return xml_file


def merge_epg():
    temp_merged = get_temp_merged()
    ltw = None
    
    dirs, files = xbmcvfs.listdir(xml_path)
    i=1
    total = len(files)
    for xmltv in files:
        if (xmltv.endswith('.gz') or xmltv.endswith('.xml')) and not xmltv.startswith('merged_epg.xml'):
            try:
                if xmltv.endswith('.gz'):
                    inF = gzip.GzipFile(fileobj=StringIO(xbmcvfs.File(os.path.join(xml_path,xmltv)).read()))
                else:
                    inF = xbmcvfs.File(os.path.join(xml_path,xmltv))
                b = inF.read()
                inF.close()
                b = b.replace('</tv>','')
                if i==1:
                    ltw = b.splitlines()
                else:
                    lines = b.splitlines()
                    li = 0
                    for line in lines:
                        if li == 0 or li == 1: 
                            pass
                        else: 
                            ltw.append(line)
                        li += 1
                i += 1
            except Exception as e:
                pass
    
    if ltw:
        f_in = '\n'.join(ltw)
        f_in = f_in+'</tv>'
        f_out = gzip.open(temp_merged, 'wb')
        f_out.write(f_in)
        f_out.close()

def rytec_start_download():
    rytec_clean()
    rytec_download()
    rytec_webgrab_check()
    rytec_extract()
    rytec_rename()
    sleep(1)
    merge_epg()
    sleep(1)
    rytec_copy()
    sleep(1)
    rytec_clean_dl()
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, nachricht1, time, icon))
    rytec_menu()

def rytec_menu():
    dialog = xbmcgui.Dialog()
    entries = [select1, select2, select4, select5]
    nr = dialog.select('RytecEPG Downloader', entries)
    if nr==0:
        rytec_start_download()
    if nr==1:
        rytec_ftp_check()
    if nr==2:
        addon.openSettings()
        sys.exit(0)
    if nr==3:
        xbmc.executebuiltin('xbmc.activatewindow(home)')
        sys.exit(0)

rytec_menu()
xbmc.executebuiltin('xbmc.activatewindow(home)')
sys.exit(0)
