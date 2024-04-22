Password handler application made with kivy(python) and built with buildozer in ubuntu linux(virtualbox-windowOS) for android.

Download buildozer according to buildozer offical document's 'installation' step.
# Just refer to offical doc's installation' step

Do 'buildozer init'
modify buildozer.spec
# refering to my buildozer's spec can be a good way.

Do 'buildozer android debug'
# This step gonna spend long time if you build your app first time.
# From second, use informations(files) already installed, so spend much less time.

Enjoy your app!

# I used adb for debugging.
# used codes like adb devices, adb logcat -s "python"
