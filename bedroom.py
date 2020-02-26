import pychromecast

device_friendly_name = "Bedroom TV"

chromecasts = pychromecast.get_chromecasts()

# select Chromecast device
cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_friendly_name)

cast.wait()

print(cast)

# get media controller 
mc = cast.media_controller
# set online video url

mc.play_media('http://192.168.2.24:8000/test.avi', 'video/mpeg')

#mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')

# blocks device
mc.block_until_active()
print(mc.status)

# plays the video
mc.play()

