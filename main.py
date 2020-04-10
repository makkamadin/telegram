from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from utils import *
import config
import time


def main():
    previous_time = ''
    timegm = time.gmtime()
    with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        while True:
            if not previous_time == "{}:{}".format(timegm.tm_hour+3, timegm.tm_min):
                timegm = time.gmtime()
                current_time = "{}:{}".format(timegm.tm_hour+3, timegm.tm_min)
                previous_time = current_time
                generate_image(current_time)
                image = client.upload_file('time.jpg')
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(image))


if __name__ == '__main__':
    main()
