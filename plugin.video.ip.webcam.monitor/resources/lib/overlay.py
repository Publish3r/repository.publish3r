import os, time, urllib2, xbmc, xbmcaddon, xbmcgui, xbmcvfs, requests

ACTION_PREVIOUS_MENU = 10
ACTION_BACKSPACE = 110
ACTION_NAV_BACK = 92
ADD_ON_ID = 'plugin.video.ip.webcam.monitor'

addon = xbmcaddon.Addon('plugin.video.ip.webcam.monitor')

__icon__     = xbmc.translatePath('special://home/addons/plugin.video.ip.webcam.monitor/resources/lib/preview.png').decode("utf-8")
__snapshot_dir__ = xbmc.translatePath('special://home/addons/plugin.video.ip.webcam.monitor/resources/snapshots/').decode("utf-8")

c_ip = addon.getSetting("ip")
c_port = addon.getSetting("port")
c_username = addon.getSetting("username")
c_password = addon.getSetting("password")

if c_username == "" or c_password == "":
    url = 'http://' + c_ip + ':' + c_port + '/shot.jpg'
else:
    url = 'http://' + c_username + ':' + c_password + '@' + c_ip + ':' + c_port + '/shot.jpg'

width     = int(float(addon.getSetting('width')))
height    = int(float(addon.getSetting('height')))
interval  = int(float(addon.getSetting('interval')))
autoClose = (addon.getSetting('autoClose') == 'true')
duration  = int(float(addon.getSetting('duration')) * 1000)

class CamPreviewDialog(xbmcgui.WindowDialog):
    def __init__(self):
        COORD_GRID_WIDTH = 1280
        COORD_GRID_HEIGHT = 720
        scaledWidth = int(float(COORD_GRID_WIDTH) / self.getWidth() * width)
        scaledHeight = int(float(COORD_GRID_HEIGHT) / self.getHeight() * height)
        self.image = xbmcgui.ControlImage(COORD_GRID_WIDTH - scaledWidth, COORD_GRID_HEIGHT - scaledHeight, scaledWidth, scaledHeight, __icon__)
        self.addControl(self.image)
        self.image.setAnimations([('WindowOpen', 'effect=slide start=%d time=1000 tween=cubic easing=in'%(scaledWidth),), ('WindowClose', 'effect=slide end=%d time=1000 tween=cubic easing=in'%(scaledWidth),)])

    def start(self, autoClose, duration, interval, url, destination):
        self.isRunning = bool(1)
        snapshot = ''
        startTime = time.time()
        while(not autoClose or (time.time() - startTime) * 1000 <= duration):
            if xbmcvfs.exists(snapshot):
                os.remove(snapshot)

            snapshot = self.downloadSnapshot(url, destination)

            if snapshot != '':
                self.update(snapshot)

            xbmc.sleep(interval)
            if not self.isRunning:
                break
        self.close()

    def downloadSnapshot(self, url, destination):
        try:
            imgData = requests.get(url).content
            filename = snapshot = xbmc.translatePath( os.path.join( destination, 'snapshot' + str(time.time()) + '.jpg' ).encode("utf-8") ).decode("utf-8")
            with open(filename, 'wb') as handler:
                handler.write(imgData)
                return filename       
        except:
            return ''

    def onAction(self, action):
        if action in (ACTION_PREVIOUS_MENU, ACTION_BACKSPACE, ACTION_NAV_BACK):
            self.isRunning = bool(0)
            self.close()

    def update(self, image):
        self.image.setImage(image, bool(0))

argCount = len(sys.argv)
for i in xrange(1, argCount):
    search = '{%d}'%(i - 1)
    replace = sys.argv[i]
    url = url.replace(search, replace)

xbmcvfs.mkdir(__snapshot_dir__)

camPreview = CamPreviewDialog()
camPreview.show()
camPreview.start(autoClose, duration, interval, url, __snapshot_dir__)
del camPreview

dirs, files = xbmcvfs.listdir(__snapshot_dir__)
for file in files:
    xbmcvfs.delete(os.path.join(__snapshot_dir__, file))
