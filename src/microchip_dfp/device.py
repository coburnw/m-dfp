import xml.etree.ElementTree as ET

import microchip_dfp.peripheral as Peripheral

class Devices():
    def __init__(self, devices):
        self.devices = devices
        return

    def __getitem__(self, key):
        if isinstance(key, int):
            return Device(self.devices[key])

        for dev in self.devices:
            device = Device(dev)
            if device.name == key:
                break

        if device.name != key:
            print('device name "{}" not found in devices'.format(key))
            raise IndexError
        
        return device

    def __len__(self):
        return len(self.devices)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        try:
            device = self.__getitem__(self.index)
        except IndexError:
            raise StopIteration

        self.index += 1
        return device

class Device():
    def __init__(self, device):
        self.device = device
        
        self.address_spaces = None
        self.peripherals = Peripheral.Peripherals(self.device.find('peripherals'))
        self.interrupts = None
        self.interfaces = None
        self.property_groups = None
        return

    @property
    def architecture(self):
        return self.device.attrib['architecture']

    @property
    def family(self):
        return self.device.attrib['family']

    @property
    def name(self):
        return self.device.attrib['name']    

