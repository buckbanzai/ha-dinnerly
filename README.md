# Marta Card (Breeze Card) Sensor

This custom components provides a sensor for each Marta/Breeze card you configure. It tracks the stored valued and number of trips remaining as well as any other items you purchased.

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE.md)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

### Installation

Copy the marta folder to `<config_dir>/custom_components/marta/`.

Required fields:
card_number
friendly_name

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  platform: marta
  friendly_name: <Card Name>
  card_number: <Card Number>
```

or add the following to your sensor.yaml file

```yaml
# Example sensor.yaml entry
- platform: marta
  friendly_name: <Card Name>
  card_number: <Card Number>
```

### Optional Sensor Values
The default state of the sensor is set to the number of trips remaining in the stored value section of the card. You can change the default state to be the stored value of the card by setting the state attribute in the configuration to value.

```yaml
# Example configuration.yaml entry
- platform: marta
  friendly_name: <Card Name>
  card_number: <Card Number>
  state: <trips or value>
```

In addition, if you have an additional item on your Marta / Breeze card that is not under the Stored Value line but you want to monitor, you can set the monitored_conditions field to be a list of those values. You just copy the text from the item on the breeze website and input it in. For example, see below.

```yaml
# Example configuration.yaml entry
- platform: marta
  friendly_name: <Card Name>
  card_number: <Card Number>
  monitored_conditions:
    - "<Special Line Item>"
```

---

Enjoy my card? Help me out for a couple of :beers: or a :coffee:!

[![coffee](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/Ryanmac8)


[commits]: https://github.com/ryanmac8/Home-Assistant-Marta/commits/master
[license-shield]: https://img.shields.io/github/license/ryanmac8/Home-Assistant-Marta.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/ryanmac8/Home-Assistant-Marta.svg?style=for-the-badge
[releases]: https://github.com/ryanmac8/Home-Assistant-Marta/releases
