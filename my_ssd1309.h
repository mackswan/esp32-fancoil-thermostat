#pragma once
#include "esphome/components/ssd1306_spi/ssd1306_spi.h"

// Access protected command() without subclassing the display object.
// The Hack struct is never instantiated — it just provides a legal call path
// to the protected method via reinterpret_cast. The actual SPISSD1306 object
// created by ESPHome is untouched; no vtable or constructor interference.

inline void ssd1309_send_cmd(esphome::ssd1306_spi::SPISSD1306* d, uint8_t cmd) {
  struct Hack : public esphome::ssd1306_spi::SPISSD1306 {
    void send(uint8_t c) { this->command(c); }
  };
  reinterpret_cast<Hack*>(d)->send(cmd);
}

inline void ssd1309_set_dim(esphome::ssd1306_spi::SPISSD1306* d, uint8_t level) {
  // Register encoding (per u8g2 issue #1504, confirmed on SSD1309 hardware):
  //   0xDB Vcom:      raw = v << 4,  v range 0-7  (0=darkest, main lever)
  //   0xD9 Precharge: raw = (p2 << 4) | p1,  p1/p2 range 1-15
  //                   higher p1 = darker, higher p2 = brighter
  //   0x81 Contrast:  0-255 (secondary lever, narrow range on SSD1309)
  switch (level) {
    case 0:  // Dimmest — dark room
      ssd1309_send_cmd(d, 0x81); ssd1309_send_cmd(d, 0x00);  // contrast=0
      ssd1309_send_cmd(d, 0xDB); ssd1309_send_cmd(d, 0x00);  // vcom v=1
      ssd1309_send_cmd(d, 0xD9); ssd1309_send_cmd(d, 0x11);  // p1=2, p2=2
      break;
    case 1:  // Dim — low ambient
      ssd1309_send_cmd(d, 0x81); ssd1309_send_cmd(d, 0x20);
      ssd1309_send_cmd(d, 0xDB); ssd1309_send_cmd(d, 0x20);  // vcom v=2
      ssd1309_send_cmd(d, 0xD9); ssd1309_send_cmd(d, 0x21);  // p1=1, p2=2
      break;
    case 2:  // Medium — normal indoor
      ssd1309_send_cmd(d, 0x81); ssd1309_send_cmd(d, 0x80);
      ssd1309_send_cmd(d, 0xDB); ssd1309_send_cmd(d, 0x30);  // vcom v=3
      ssd1309_send_cmd(d, 0xD9); ssd1309_send_cmd(d, 0x41);  // p1=1, p2=4
      break;
    case 3:  // Full brightness — bright room
      ssd1309_send_cmd(d, 0x81); ssd1309_send_cmd(d, 0xFF);
      ssd1309_send_cmd(d, 0xDB); ssd1309_send_cmd(d, 0x40);  // vcom v=4 (datasheet default)
      ssd1309_send_cmd(d, 0xD9); ssd1309_send_cmd(d, 0xF1);  // p1=1, p2=15
      break;
  }
}
