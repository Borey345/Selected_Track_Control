# this file stores some constants regarding MIDI-handling, etc.
# for settings which MIDI-notes trigger what functionality see settings.py

import Live


STATUS_MASK = 0xF0
CHAN_MASK =  0x0F

CC_STATUS =  0xb0
NOTEON_STATUS = 0x90
NOTEOFF_STATUS = 0x80

STATUS_ON =  0x7f
STATUS_OFF = 0x00
STATUS_OFF2 = 0x40

# possible CC modes (always 7bit); RELATIVE: <increment> / <decrement>
ABSOLUTE = Live.MidiMap.MapMode.absolute # 0 - 127
RELATIVE_BINARY_OFFSET = Live.MidiMap.MapMode.relative_binary_offset # 065 - 127 / 063 - 001
RELATIVE_SIGNED_BIT = Live.MidiMap.MapMode.relative_signed_bit # 001 - 064 / 065 - 127
RELATIVE_SIGNED_BIT2 = Live.MidiMap.MapMode.relative_signed_bit2 # 065 - 127 / 001 - 064
RELATIVE_TWO_COMPLIMENT = Live.MidiMap.MapMode.relative_two_compliment # 001 - 064 / 127 - 65


relative_to_signed_int = {
	RELATIVE_BINARY_OFFSET: relativebinary_offset_to_signed_int,
	RELATIVE_SIGNED_BIT: relative_signed_bit_to_signed_int
	RELATIVE_SIGNED_BIT2: relative_signed_bit2_to_signed_int
	RELATIVE_TWO_COMPLIMENT: relative_two_complement_to_signed_int
}

def relativebinary_offset_to_signed_int(value):
	return value-64
def relative_signed_bit_to_signed_int(value):
	if value > 64:
		return -value+64
	return value
def relative_signed_bit2_to_signed_int(value):
	if value > 64:
		return value-64
	return -value
def relative_two_complement_to_signed_int(value):
	if value > 64:
		return value-128
	return value



class MIDICommand:
	def __init__(self, key, mode = ABSOLUTE, status = NOTEON_STATUS, channel = 0):
		self.key = key
		self.mode = mode
		self.status = status
		self.channel = channel
class Note (MIDICommand):
	def __init__(self, note, channel = 0):
		super(note, ABSOLUTE, NOTEON_STATUS, channel)
class CC (MIDICommand):
	def __init__(self, cc, mode = RELATIVE_TWO_COMPLIMENT, channel = 0):
		super(cc, mode, CC_STATUS, channel)