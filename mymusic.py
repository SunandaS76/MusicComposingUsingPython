#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(120)

fitMedia(COMMON_LOVE_DRUMBEAT_1, 1, 1, 16)
setEffect(1, VOLUME, GAIN, -60, 1, 12)
setEffect(1, VOLUME, GAIN, 5, 12, -60, 16)
fitMedia(HIPHOP_BASSSUB_003, 2, 1, 12)
setEffect(2, DELAY, DELAY_TIME, 500)
fitMedia(HOUSE_MAIN_BEAT_003, 3, 1, 8)
setEffect(3, REVERB, REVERB_TIME, 200)

 
finish()
