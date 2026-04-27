# Custom ESP32-S3 Fan Coil Thermostat

A DIY wall-mounted thermostat built around an ESP32-S3 for controlling a 120V fan coil system, designed with local-first control, physical UI, and Home Assistant integration.

## Documentation

- [Bill of Materials](./BOM.md)
- [ESPHome reference configuration](./thermostat_reference.yaml)
- [Custom SSD1309 helper](./my_ssd1309.h)

## Features

- Local thermostat control loop (not cloud dependent)
- 120V fan coil relay switching
- OLED UI (temperature, setpoint, humidity, outdoor weather)
- Rotary encoder control
- SHTC3 temperature / humidity sensing
- IR transmit/receive support
- Photo sensor-driven display/button dimming
- Home Assistant integration (setpoint + weather)
- Standalone operation if HA is unavailable

## Hardware

- Waveshare ESP32-S3 Zero
- SSD1309 OLED (SPI)
- SHTC3 sensor
- Rotary encoder with push switch
- Isolated relay module
- KY-018 light sensor
- Piezo buzzer
- IR TX/RX
- 5V AC-DC power module

## Why I Built It

I have a seasonal 2-pipe 120V fan coil system and wanted something smarter than a conventional thermostat, while keeping control local and hackable.

## Project Photos

### Finished Installed Thermostat
![Installed thermostat](thermostat-installed-front.jpg)

### Main Runtime Display
![Display UI](thermostat-display.jpg)

### Mode Selection Interface
![Mode UI](thermostat-installed-mode_set.jpg)

### Internal Assembly with Wiring Layout
![Bench Layout](thermostat-internal-esp32_unmounted.JPG)

## Internal Component Layout
![Internal layout](thermostat-premounting_layout.jpg)
(Esp32 and the mounting extender were rotated left 90° in final layout)
## Display Features

- Custom OLED UI
- Ambient dimming
- Multi-screen rotary menu
- Hand-crafted pixel weather sprites

## Architecture

Room temp → control loop → relay output
             ↓
       OLED + local UI
             ↓
 Home Assistant (weather + optional setpoint)

## Future Ideas

- PID mode experimentation
- Matter variant?
- Expanded HVAC modes
- More polished enclosure revisions

## Disclaimer

This project interfaces with mains voltage.
Use proper isolation and only attempt if you're comfortable working safely with line voltage.
