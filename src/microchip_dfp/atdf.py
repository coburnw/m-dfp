import xml.etree.ElementTree as ET

import microchip_dfp.device as Device
import microchip_dfp.pinout as Pinout
import microchip_dfp.variant as Variant

class Atdf():
    def __init__(self, filename):
        self.filename = filename
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

        self.variants = Variant.Variants(self.root.find('variants'))
        self.devices = Device.Devices(self.root.find('devices'))
        self.modules = None
        self.pinouts = Pinout.Pinouts(self.root.find('pinouts'))
        return
    
