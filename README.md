# Dinnerly Sensor

This custom components provides a sensor for the upcoming Dinnerly meals

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE.md)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

### Installation

Copy the dinnerly folder to `<config_dir>/custom_components/dinnerly/`.

Required fields:
username
password

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  platform: dinnerly
  friendly_name: <Week Name>
  username: <Username>
  password: <Password>
```

[license-shield]: https://img.shields.io/github/license/buckbanzai/ha-dinnerly.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/buckbanzai/ha-dinnerly.svg?style=for-the-badge
[releases]: https://github.com/buckbanzai/ha-dinnerly/releases
