#		python code
#		script_name: demo
#
#		author: Sunanda Somwase
#		description: Cometition practice
#
#   Set up
from earsketch import *

init()
setTempo(120)
#   Music
chord = RD_RNB_KEYSRHODES_1
secondaryBeat = YG_ALT_POP_MELODY_1
mainBeat = COMMON_LOVE_THEME_PIANO_2
fitMedia(chord, 1, 1, 16)
#   Add effect between measures 1 and 16
setEffect(1, VOLUME, GAIN, -60, 1, 12)
setEffect(1, VOLUME, GAIN, 5 ,12, -60, 16)


fitMedia(secondaryBeat, 2, 1, 12)
#   Add effect
setEffect(2, DELAY, DELAY_TIME, 500)
fitMedia(mainBeat, 3, 1, 8)
#   Add effect
setEffect(3, REVERB, REVERB_TIME, 200)
#   Finish
finish()
