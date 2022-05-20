"""Platform for sensor integration."""
import logging
from datetime import timedelta

import homeassistant.helpers.config_validation as cv
import requests
import voluptuous as vol
from bs4 import BeautifulSoup
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_FRIENDLY_NAME
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle


MIN_TIME_BETWEEN_UPDATES = timedelta(hours=1)

_LOGGER = logging.getLogger(__name__)
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Optional(CONF_FRIENDLY_NAME): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    username = config.get(CONF_USERNAME)
    password = config.get(CONF_PASSWORD)
    friendly_name = config.get(CONF_FRIENDLY_NAME)
    add_entities([Dinnerly(username, password, friendly_name)])


class Dinnerly(Entity):
    """Representation of a Sensor."""

    def __init__(self, username, password, friendly_name):
        """Initialize the sensor."""
        self._state = None
        self._username = username
        self._password = password
        self._friendly_name = friendly_name
        self._attributes = {}

    @property
    def entity_id(self):
        """Return the name of the sensor."""
        name = "sensor.dinnerly"
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
        return "mdi:food-turkey"

    @property
    def extra_state_attributes(self):
        """Return device specific state attributes."""
        return self._attributes

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        session = requests.Session()

        login_uri = "https://dinnerly.com/login"
        get_authenticity_token = session.get(login_uri)
        soup = BeautifulSoup(get_authenticity_token.text, "html.parser")

        def is_auth_token(tag):
            if tag.has_attr("name"):
                return tag.attrs["name"] == "authenticity_token"
            else:
                return False

        auth_token = soup.find_all(is_auth_token)[0].attrs["value"]

        login_body = {
            "utf8": "✓",
            "authenticity_token": auth_token,
            "spree_user[email]": self._username,
            "spree_user[password]": self._password,
            "spree_user[brand]": "dn",
            "button": "",
        }

        get_user_token = session.post(login_uri, data=login_body)

        # headers["Content-Type"] = "application/json"
        # headers["Authorization"] = "Bearer " + token.json()["access_token"]

        # account_result = requests.get(
        #     "https://api.prod.orca.connext.com/smw/1.0.0/transitAccounts",
        #     headers=headers,
        # )

        # first_transit_account = account_result.json()["data"][0]
        # card_balance = first_transit_account["balance"]

        # if card_balance is None:
        #     card_balance = 0

        self._state = get_user_token.headers["Set-Cookie"]
        # self._attributes["Card Number"] = self._cardnumber
        # self._attributes["Card Type"] = first_transit_account["cardTypeName"]
