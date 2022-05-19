# ORCA Card Sensor

This custom components provides a sensor for each [ORCA card](https://en.wikipedia.org/wiki/ORCA_card) you configure, which shows the current balance on the card.

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE.md)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

### Installation

Copy the orca folder to `<config_dir>/custom_components/orca/`.

Required fields:
card_number
security_code

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  platform: orca
  friendly_name: <Card Name>
  card_number: <Card Number>
  security_code: <Security Code>
```

[license-shield]: https://img.shields.io/github/license/buckbanzai/ha-orca.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/buckbanzai/ha-orca.svg?style=for-the-badge
[releases]: https://github.com/buckbanzai/ha-orca/releases
