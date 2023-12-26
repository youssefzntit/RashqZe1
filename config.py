import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6594794857:AAE188AGJKjF--H17gyfGBmqjPd0KIrGpO8")

    APP_ID = int(os.environ.get("APP_ID", 19768714))

    API_HASH = os.environ.get("API_HASH", "ac680c77aa60dcc1436071a4ec2dac2a")
