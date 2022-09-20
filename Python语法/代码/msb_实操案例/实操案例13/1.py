"""任务1：编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器从而发出不同的声音。可
以弹奏的乐器包括二胡、钢琴和琵琶"""
class Instrument(object):
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print("二胡在演奏")

class Piano(Instrument):
    def make_sound(self):
        print("钢琴在演奏")

class Violin(Instrument):
    def make_sound(self):
        print("小提琴在演奏")

def play(instrument):
    instrument.make_sound()

if __name__ == '__main__':
    play(Erhu())
    play(Violin())
    play(Piano())
