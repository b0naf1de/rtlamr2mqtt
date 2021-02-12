# List of the Meter IDs to watch
# Use empty brackets to read all meters - []
# List may contain only one entry - [12345678]
# or multiple entries - [12345678, 98765432, 12340123]
#WATCHED_METERS = [8675309, 123456789]
WATCHED_METERS = []

# List of protocols to watch
# r900 and idm supported
# List may contain only one protocol - ['r900']
# or multiple protocols - ['r900', 'idm']
MSGTYPE = ['r900']

# 
# Mode for running rtlamr
#   True  : Run in single mode and exit after each reading
#   False : Run continously
RTLAMR_SINGLE_MODE = True

# Period of meter transmissions and value updates are independent
# So, we only need to read the meter as frequently as it updates its
# values. 
# Period meter updates its parameters (Seconds) 
METER_UPDATE_PERIOD=900

# RTLAMR_LOW_CPU: Run in low cpu mode
#   Single Mode = True
#   center_freq = 912000000
#   symbol_length = 8
RTLAMR_LOW_CPU = False 

# multiplier to get reading to Gallons (gal)
GALLONS_MULTIPLIER = 0.10

# multiplier to get reading to Watt Hours (Wh)
# examples:
#   for meter providing readings in kWh
#      MULTIPLIER = 1000
#   for meter providing readings in kWh
#   with 2 extra digits of precision
#      MULTIPLIER = 10
# MULTIPLIER needs to be a number
WH_MULTIPLIER = 1000

# number of IDM intervals per hour reported by the meter
# examples:
#   for meter providing readings every 5 minutes
#   or 12 times every hour
#     READINGS_PER_HOUR = 12
#   for meter providing readings every 15 minutes
#   or 12 times every hour
#     READINGS_PER_HOUR = 4
READINGS_PER_HOUR = 12
 
# MQTT Server settings
# MQTT_HOST needs to be a string
# MQTT_PORT needs to be an int
# MQTT_USER needs to be a string
# MQTT_PASSWORD needs to be a string
# If no authentication, leave MQTT_USER and MQTT_PASSWORD empty
MQTT_HOST = '127.0.0.1'
MQTT_PORT = 1883
MQTT_USER = ''
MQTT_PASSWORD = ''

# path to rtlamr
RTLAMR = '/usr/local/bin/rtlamr'

# path to rtl_tcp
#RTL_TCP = '/usr/local/bin/rtl_tcp'
RTL_TCP = '/usr/bin/rtl_tcp'
