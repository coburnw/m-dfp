import xml.etree.ElementTree as ET


class Peripherals():
    def __init__(self, peripherals):
        self.peripherals = peripherals
        self.index = 0
        return
    
        # self.modules = dict()
        # for module in peripherals:
        #     m = Module(module)
        #     self.modules[m.name] = m

        # return

    def __len__(self):
        if self.peripherals is None:
            return 0
        
        return len(self.peripherals)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        try:
            module = Module(self.peripherals[self.index])
        except IndexError:
            raise StopIteration

        self.index += 1
        return module
        
class Module(): #Peripheral?
    def __init__(self, module):
        self.module = module
        self.instances = dict()
        
        for inst in module:
            instance = ModuleInstance(self.name, inst)
            self.instances[instance.number] = instance

        return

    @property
    def name(self):
        return self.module.attrib['name']
        
    @property
    def has_signals(self):
        return False

class ModuleInstance():
    def __init__(self, name, instance):
        self.instance = instance
        self.number = self.name.removeprefix(name)

        self.address_space = None
        self.address_offset = 0
        if self.instance.find('register-group') is not None:
            self.address_space = self.instance.find('register-group').attrib['address-space']
            self.address_offset = self.instance.find('register-group').attrib['offset']
            
        self.signals = Signals(self.instance.find('signals'))
        return

    @property
    def name(self):
        return self.instance.attrib['name']

class Signals():
    def __init__(self, signals):
        self.signals = signals
        self.index = 0
        return

    def __len__(self):
        if self.signals is None:
            return 0
        
        return len(self.signals)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        try:
            signal = Signal(self.signals[self.index])
        except IndexError:
            raise StopIteration

        self.index += 1
        return signal

class Signal():
    def __init__(self, signal):
        self.signal = signal
        
        if signal.tag != 'signal':
            print('Signal({}) is not a signal'.format(signal.tag))
            raise
        
        return

    @property
    def field(self):
        return self.signal.get('field', '')
    
    @property
    def function(self):
        return self.signal.attrib['function']

    @property
    def group(self):
        return self.signal.attrib['group']

    @property
    def index(self):
        return self.signal.get('index', '')

    @property
    def pad(self):
        return self.signal.attrib['pad']
