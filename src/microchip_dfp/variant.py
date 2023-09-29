import xml.etree.ElementTree as ET

class Variants():
    def __init__(self, variants):
        self.variants = variants
        return

    def __getitem__(self, ordercode):
        return Variant(self.variants[ordercode])

class Variant():
    def __init__(self, variant):
        self.variant = variant
        return

    @property
    def ordercode(self):
        return self.variant.get('ordercode', '')
        
    @property
    def package(self):
        return self.variant.get('package', '')
    
    @property
    def pinout(self):
        return self.variant.get('pinout', '')

    @property
    def speedmax(self):
        return self.variant.get('speedmax', 0)
    
    @property
    def tempmax(self):
        return self.variant.get('tempmax', 0)
    
    @property
    def tempmin(self):
        return self.variant.get('tempmin', 0)
    
    @property
    def vccmax(self):
        return self.variant.get('vccmax', 0)
    
    @property
    def vccmin(self):
        return self.variant.get('vccmin', 0)
    
