#Constants Variables and settings for onionSkinTool

"""
The default settings get corrupted easily when the tool crashes or bugs out.
These default settings will overwrite the corrupted settings.txt file
"""

default_settings = {
    "relativeFrameAmount": 8,
    "relativeStep": 1,
    "activeRelativeFrames": [-1, 1],
    "displayKeyframes": False,
    "autoClearBuffer": True,
    "tintType": 1,
    "tintSeed": 0,
    "onionType": 1,
    "maxBufferSize": 200,
    "aTint": [200, 200, 50],
    "drawBehind": True,
    "rFutureTint": [20, 255, 114],
    "outlineWidth": 3,
    "rPastTint": [255, 26, 75]
}
