# Bill of Materials (BOM)

## Core Electronics

| Category | Part | Qty Used | Approx Cost* | Notes |
|---|---:|---:|---:|---|
| MCU | Waveshare ESP32-S3 Zero | 1 | $12.49 | Main controller |
| Sensor | SHTC3 I2C Temperature/Humidity Module | 1 | $3.20 | From 5-pack |
| Display | 2.42" SSD1309 128x64 SPI OLED | 1 | $15.99 | Main UI |
| Relay | 5V Opto-Isolated 1-Channel Relay | 1 | $5.97 | 120V fan switching |
| Input | KY-040 Rotary Encoder | 1 | $3.50 | From 2-pack |
| Knob | Aluminum Encoder Knob (40mm) | 1 | $5.29 | Larger user knob |
| Sensor | KY-018 Photoresistor Module | 1 | $1.20 | From 5-pack |
| Audio | 20mm Piezo Disc | 1 | $0.40 | From 20-pack |
| IR RX | 38kHz IR Receiver Module | 1 | Included | IR receive |
| IR TX | Vishay TSAL6100 IR LED | 1 | $0.86 | From 10-pack |
| Power | 5V AC-DC Supply Module (5W) | 1 | TBD | Internal power supply |

\*Pack pricing amortized where applicable.

---

## Mechanical / Enclosure

| Part | Qty | Cost | Notes |
|---|---:|---:|---|
| Legrand Wiremold NMW3 Deep Box | 1 | $9.99 | Main enclosure |
| Enerlites Screwless Blank Wall Plate | 1 | $11.99 | Modified front panel |
| Black Matte Foil Tape | 1 | $9.59 | Display masking / light blocking |

---

## Support Materials / Consumables

Not fully costed:

- Dupont / JST connectors and housings  
- Hookup wire  
- Heat shrink  
- Solder and flux  
- Fasteners / standoffs  
- IR driver resistors  
- Quick disconnects / terminal hardware  

---

## Approx Project Cost

Estimated build cost:

**~$85–95 USD**

(Depends how you allocate multi-packs and consumables.)

---

## Components Evaluated / Revisions

### Revisions made during development

- Moved from DHT22-style sensors to **SHTC3**
- Final display choice became **SSD1309 128x64 SPI**
- Upgraded IR emitter to **TSAL6100**
- Replaced stock encoder knob with larger aluminum knob

---

## Primary Functional Blocks

### Control
- ESP32-S3 Zero  
- Relay Module  
- Rotary Encoder  

### Sensing
- SHTC3  
- Photoresistor  
- IR Receiver  

### User Interface
- OLED Display  
- Piezo  
- Encoder Knob  

### Infrared
- TSAL6100 IR LED  
- IR Receiver Module  

### Mechanical
- Wiremold enclosure  
- Modified Decora blank plate  

---

## Safety Note

This project interfaces with mains voltage.

Use proper isolation and only attempt if you are comfortable working safely with line voltage.
