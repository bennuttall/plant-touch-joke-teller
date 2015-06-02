# Plant Touch Joke Teller

## Components

- [Adafruit Capacative Touch HAT](http://www.adafruit.com/product/2340)

## Requirements

- Python SMBus
- [Adafruit_Python_MPR121](https://github.com/adafruit/Adafruit_Python_MPR121)

```bash
sudo apt-get install build-essential python-dev python-smbus python-pip
git clone git://github.com/adafruit/Adafruit_Python_MPR121
cd Adafruit_Python_MPR121
sudo python setup.py install
cd ..
rm -rf Adafruit_Python_MPR121
```

- Add `i2c-dev` to `/etc/modules`
- Enable SPI & I2C in `raspi-config`
- Reboot

