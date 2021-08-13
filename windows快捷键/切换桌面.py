from pykeyboard import PyKeyboard
import time
k = PyKeyboard()
k.press_key(k.windows_r_key)
k.press_key(k.control_l_key)
k.tap_key('d')
k.release_key(k.windows_r_key)
k.release_key(k.control_l_key)

