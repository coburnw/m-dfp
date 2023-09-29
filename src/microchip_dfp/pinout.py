import xml.etree.ElementTree as ET

class Pinouts():
    def __init__(self, pinouts):
        self.pinouts = pinouts
        return

    def __getitem__(self, name):
        for pinout in self.pinouts:
            pinout = Pinout(pinout)
            if pinout.name == name:
                break

        if pinout.name != name:
            print('pinout name "{}" not found in pinouts'.format(name))
            raise IndexError
        
        return pinout
    
class Pinout():
    def __init__(self, pinout):
        self.pinout = pinout
        self.pinmap = dict()
        for pin in pinout:
            pin = Pin(pin)
            self.pinmap[int(pin.position)-1] = pin
            
        return

    def __len__(self):
        return len(self.pinmap)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        try:
            pin = self.pinmap[self.index]
        except KeyError:
            raise StopIteration

        self.index += 1
        return pin

    @property
    def name(self):
        return self.pinout.get('name', '')

class Pin():
    def __init__(self, pin):
        self.pin = pin
        return

    @property
    def pad(self):
        return self.pin.attrib['pad']

    @property
    def position(self):
        return self.pin.attrib['position']
    
