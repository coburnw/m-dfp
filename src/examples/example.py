import os

from microchip_dfp import Atdf

if __name__ == '__main__':
    fpath = os.path.expanduser('~/dev/svg/avr-atpack/Microchip.AVR-Dx_DFP.2.3.272/atdf/AVR128DA28.atdf')
    target = Atdf(fpath)

    for device in target.devices:
        print(device.name, device.architecture)

    for variant in target.variants:
        print(variant.ordercode, variant.package)
    
    device = target.devices[0]

    for module in device.peripherals:
        print(module.name)
        for name, instance in module.instances.items():
            print('  {}: {}'.format(instance.name, len(instance.signals)))
            if instance.signals:
                for signal in instance.signals:
                    print('    {}: {}_{}{}'.format(signal.pad, signal.function, signal.group, signal.index))

    print()

    variant = target.variants[0]
    pinout = target.pinouts[variant.package]
    print(pinout.name)
    for pin in pinout:
        print('  {}: {}'.format(pin.position, pin.pad))
