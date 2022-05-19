"""Platform for sensor integration."""
import logging
import voluptuous as vol
import uuid
import requests
from datetime import timedelta

from homeassistant.const import (CONF_FRIENDLY_NAME, CONF_STATE)
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.util import Throttle
import homeassistant.helpers.config_validation as cv


MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)

_LOGGER = logging.getLogger(__name__)
CONF_CARDNUMBER = 'card_number'
CONF_SECURITY_CODE = 'security_code'

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_CARDNUMBER): cv.string,
    vol.Required(CONF_SECURITY_CODE): cv.string,
    vol.Optional(CONF_FRIENDLY_NAME): cv.string
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    cardnumber = config.get(CONF_CARDNUMBER)
    security_code = config.get(CONF_SECURITY_CODE)
    friendly_name = config.get(CONF_FRIENDLY_NAME)
    add_entities([OrcaCard(cardnumber, security_code, friendly_name)])


class OrcaCard(Entity):
    """Representation of a Sensor."""

    def __init__(self, cardnumber, security_code, friendly_name):
        """Initialize the sensor."""
        self._state = None
        self._cardnumber = cardnumber
        self._security_code = security_code
        self._friendly_name = friendly_name
        self._attributes = {}

    @property
    def entity_id(self):
        """Return the name of the sensor."""
        name = "sensor.orca_card_"+self._cardnumber
        return name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def name(self):
        """Return the fname of the sensor."""
        return self._friendly_name

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        measurement = ""
        return measurement

    @property
    def icon(self):
        """Return the icon."""
        return "mdi:subway-variant"

    @property
    def extra_state_attributes(self):
        """Return device specific state attributes."""
        return self._attributes

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        headers = {
            'User-Agent': 'myORCA/1 CFNetwork/1333.0.4 Darwin/21.5.0',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        uppercase_uuid = str(uuid.uuid4()).upper()
        token_body = {'grant_type': 'mobilevario_guest',
                      'username': self._cardnumber,
                      'password': self._security_code,
                      'balance_protection_code': '',
                      'client_id': 'us0hrpbDc0AIOKmqCytWODwWkq4a',
                      'scope': 'device_'+uppercase_uuid
                      }
        token_result = requests.post(
            'https://api.prod.orca.connext.com/token', data=token_body, headers=headers)

        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer ' + \
            token_result.json()['access_token']

        account_result = requests.get(
            'https://api.prod.orca.connext.com/smw/1.0.0/transitAccounts', headers=headers)

        first_transit_account = account_result.json()['data'][0]

        self._state = first_transit_account['balance']
        self._attributes["Card Number"] = self._cardnumber
        self._attributes["Card Type"] = first_transit_account['cardTypeName']
