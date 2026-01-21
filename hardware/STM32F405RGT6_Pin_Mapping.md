# STM32F405RGT6 Pin Mapping

## Power Pins

| Pin | MCU Pin | Signal/Connection |
|-----|---------|-------------------|
| 1 | VBAT | 3.3V |
| 19 | VDD1 | 3.3V |
| 32 | VDD2 | 3.3V |
| 48 | VDD3 | 3.3V |
| 64 | VDD4 | 3.3V |
| 13 | VDDA | 3.3V |
| 31 | VCAP1 | 2.2µF to GND (C5) |
| 47 | VCAP2 | 2.2µF to GND (C6) |
| 18 | VSS1 | GND |
| 63 | VSS2 | GND |
| 12 | VSSA | GND |

## System Pins

| Pin | MCU Pin | Signal/Connection |
|-----|---------|-------------------|
| 7 | NRST | RESET |
| 60 | BOOT0 | BOOT0 |

## Crystal Oscillators

| Pin | MCU Pin | Signal/Connection |
|-----|---------|-------------------|
| 5 | PH0 | Y1 (12MHz HSE) + 22pF (C1) |
| 6 | PH1 | Y1 (12MHz HSE) + 22pF (C2) |
| 3 | PC14 | Y2 (32.768kHz LSE) + 15pF (C3) |
| 4 | PC15 | Y2 (32.768kHz LSE) + 15pF (C4) |

## Port A

| Pin | MCU Pin | Signal/Connection |
|-----|---------|-------------------|
| 14 | PA0 | G2 |
| 15 | PA1 | BATT_VIN |
| 16 | PA2/UART2_TX | TX1 |
| 17 | PA3/UART2_RX | RX1 |
| 20 | PA4/SPI1_NSS | AUD_LRCLK |
| 21 | PA5/SPI1_SCK | SCK |
| 22 | PA6/SPI1_MISO | CIPO |
| 23 | PA7/SPI1_MOSI | COPI |
| 41 | PA8 | G1 |
| 42 | PA9/UART1_TX | — |
| 43 | PA10/UART1_RX | — |
| 44 | PA11 | D- (via 22Ω R2) |
| 45 | PA12 | D+ (via 22Ω R3) |
| 46 | PA13/JTMS | SWDIO |
| 49 | PA14/JTCK | SWCLK |
| 50 | PA15/JTDI | STAT |

## Port B

| Pin | MCU Pin | Signal/Connection |
|-----|---------|-------------------|
| 26 | PB0 | A1 |
| 27 | PB1 | INT |
| 28 | PB2-BOOT1 | — |
| 55 | PB3/JTDO | AUD_BCLK |
| 56 | PB4/JTRST | AUD_OUT |
| 57 | PB5 | AUD_IN |
| 58 | PB6 | SCL1 |
| 59 | PB7 | SDA1 |
| 61 | PB8 | CAN_RX |
| 62 | PB9 | CAN_TX |
| 29 | PB10 | SCL |
| 30 | PB11 | SDA |
| 33 | PB12/I2S2_WS | HOST_ID |
| 34 | PB13/I2S2_CK | HOST_VBUS |
| 35 | PB14/I2S2_XD | HOST_D- |
| 36 | PB15/I2S2_SD | HOST_D+ |

## Port C

| Pin | MCU Pin | Signal/Connection |
|-----|---------|-------------------|
| 8 | PC0 | D0 |
| 9 | PC1 | D1 |
| 10 | PC2 | G6 |
| 11 | PC3 | FLASH_CS |
| 24 | PC4 | CS |
| 25 | PC5 | A0 |
| 37 | PC6/I2S2_MCK | PWM0 |
| 38 | PC7 | PWM1 |
| 39 | PC8/SDIO_D0 | G3 |
| 40 | PC9/SDIO_D1 | G4 |
| 51 | PC10/SDIO_D2 | FLASH_SCK |
| 52 | PC11/SDIO_D3 | FLASH_SDO |
| 53 | PC12/SDIO_CLK | FLASH_SDI |
| 2 | PC13 | G5 |

## Port D

| Pin | MCU Pin | Signal/Connection |
|-----|---------|-------------------|
| 54 | PD2/SDIO_CMD | G0 |

## Functional Summary

| Function | Pins/Signals |
|----------|--------------|
| **USB FS** | PA11 (D-), PA12 (D+) via 22Ω resistors |
| **USB Host** | HOST_ID, HOST_VBUS, HOST_D-, HOST_D+ |
| **SWD** | SWDIO (PA13), SWCLK (PA14) |
| **UART1** | PA9 (TX), PA10 (RX) |
| **UART2** | TX1 (PA2), RX1 (PA3) |
| **SPI1** | SCK (PA5), CIPO (PA6), COPI (PA7), AUD_LRCLK (PA4) |
| **I2C (Bus 0)** | SCL (PB10), SDA (PB11) |
| **I2C (Bus 1)** | SCL1 (PB6), SDA1 (PB7) |
| **CAN** | CAN_RX (PB8), CAN_TX (PB9) |
| **Audio/I2S** | AUD_BCLK, AUD_OUT, AUD_IN, AUD_LRCLK |
| **SPI Flash** | FLASH_CS, FLASH_SCK, FLASH_SDO, FLASH_SDI |
| **PWM** | PWM0 (PC6), PWM1 (PC7) |
| **GPIO** | G0-G6, A0, A1, D0, D1, INT, CS, STAT |

---

## MicroMod Connector (J1) - MICROMOD-2222

### Power & System

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 2*2 | 3.3V | 3.3V |
| 1*10 | GND | GND |
| 4 | 3.3V_EN | — |
| 72 | RTC_3V | — |
| 9 | USB_VIN | — |
| 49 | BATT_VIN/3 | BATT_VIN |

### Reset & Boot

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 6 | RESET | RESET |
| 11 | BOOT | BOOT |

### USB (Device)

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 5 | USB_D- | D- |
| 3 | USB_D+ | D+ |

### USB Host

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 37 | USBHOST_D- | HOST_D- |
| 35 | USBHOST_D+ | HOST_D+ |
| 63 | G10/ADC_D+/CAM_VSYNC | HOST_VBUS |
| 8 | G11 | HOST_ID |

### SWD (Debug)

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 23 | SWDIO | SWDIO |
| 21 | SWDCK | SWCLK |

### CAN Bus

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 43 | CAN-TX | CAN_TX |
| 41 | CAN-RX | CAN_RX |

### SPI (Primary)

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 57 | SPI_SCK | SCK |
| 59 | SPI_SDO | COPI |
| 61 | SPI_SDI | CIPO |
| 55 | SPI_CS | CS |

### SPI1 / SDIO

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 60 | SPI_SCK1/SDIO_CLK | — |
| 62 | SPI_SDO1/SDIO_CMD | — |
| 64 | SPI_SDI1/SDIO_DATA0 | — |
| 66 | SDIO_DATA1 | — |
| 68 | SDIO_DATA2 | — |
| 70 | SPI_CS1/SDIO_DATA3 | — |

### I2C (Primary)

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 14 | I2C_SCL | SCL |
| 12 | I2C_SDA | SDA |
| 16 | I2C_INT | INT |

### I2C (Secondary)

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 53 | I2C_SCL1 | SCL1 |
| 51 | I2C_SDA1 | SDA1 |

### Audio / I2S / Camera

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 58 | AUD_MCLK | — |
| 56 | AUD_OUT/CAM_MCLK | AUD_OUT |
| 54 | AUD_IN/CAM_PCLK | AUD_IN |
| 52 | AUD_LRCLK | AUD_LRCLK |
| 50 | AUD_BCLK | AUD_BCLK |

### UART1

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 17 | TX1 | TX1 |
| 19 | RX1 | RX1 |
| 13 | RTS1 | — |
| 15 | CTS1 | — |

### UART2

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 22 | TX2 | — |
| 20 | RX2 | — |

### Analog

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 34 | A0 | A0 |
| 38 | A1 | A1 |

### PWM

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 32 | PWM0 | PWM0 |
| 47 | PWM1 | PWM1 |

### Digital I/O

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 10 | D0 | D0 |
| 18 | D1/CAM_TRIG | D1 |

### GPIO / BUS

| Pin | MicroMod Signal | Board Connection |
|-----|-----------------|------------------|
| 40 | G0/BUS0 | G0 |
| 42 | G1/BUS1 | G1 |
| 44 | G2/BUS2 | G2 |
| 46 | G3/BUS3 | G3 |
| 48 | G4/BUS4 | G4 |
| 73 | G5/BUS5 | G5 |
| 71 | G6/BUS6 | G6 |
| 69 | G7/BUS7 | — |
| 67 | G8 | — |
| 65 | G9/ADC_D-/CAM_HSYNC | — |

---

## Cross-Reference: MicroMod ↔ STM32F405

| MicroMod Pin | MicroMod Signal | STM32 Pin | STM32 GPIO |
|--------------|-----------------|-----------|------------|
| 6 | RESET | 7 | NRST |
| 11 | BOOT | 60 | BOOT0 |
| 5 | USB_D- | 44 | PA11 |
| 3 | USB_D+ | 45 | PA12 |
| 37 | USBHOST_D- | 35 | PB14 |
| 35 | USBHOST_D+ | 36 | PB15 |
| 63 | HOST_VBUS | 34 | PB13 |
| 8 | HOST_ID | 33 | PB12 |
| 23 | SWDIO | 46 | PA13 |
| 21 | SWDCK | 49 | PA14 |
| 43 | CAN-TX | 62 | PB9 |
| 41 | CAN-RX | 61 | PB8 |
| 57 | SPI_SCK | 21 | PA5 |
| 59 | SPI_SDO | 23 | PA7 |
| 61 | SPI_SDI | 22 | PA6 |
| 55 | SPI_CS | 24 | PC4 |
| 14 | I2C_SCL | 29 | PB10 |
| 12 | I2C_SDA | 30 | PB11 |
| 16 | I2C_INT | 27 | PB1 |
| 53 | I2C_SCL1 | 58 | PB6 |
| 51 | I2C_SDA1 | 59 | PB7 |
| 56 | AUD_OUT | 56 | PB4 |
| 54 | AUD_IN | 57 | PB5 |
| 52 | AUD_LRCLK | 20 | PA4 |
| 50 | AUD_BCLK | 55 | PB3 |
| 17 | TX1 | 16 | PA2 |
| 19 | RX1 | 17 | PA3 |
| 34 | A0 | 25 | PC5 |
| 38 | A1 | 26 | PB0 |
| 32 | PWM0 | 37 | PC6 |
| 47 | PWM1 | 38 | PC7 |
| 10 | D0 | 8 | PC0 |
| 18 | D1 | 9 | PC1 |
| 40 | G0 | 54 | PD2 |
| 42 | G1 | 41 | PA8 |
| 44 | G2 | 14 | PA0 |
| 46 | G3 | 39 | PC8 |
| 48 | G4 | 40 | PC9 |
| 73 | G5 | 2 | PC13 |
| 71 | G6 | 10 | PC2 |
| 49 | BATT_VIN | 15 | PA1 |
