from analyx.plugins import Plugin

class HitCounter(Plugin):
    def output(self):
        print("Hello! This is a test plugin!")

a = HitCounter()

a.output()