import win32api
import pystray
from PIL import Image, ImageDraw, ImageFont


def get_refresh_rate():
    devices = win32api.EnumDisplayDevices()
    settings = win32api.EnumDisplaySettings(devices.DeviceName, -1)
    return settings.DisplayFrequency


def toggle_refresh_rate(icon):
    devices = win32api.EnumDisplayDevices()
    settings = win32api.EnumDisplaySettings(devices.DeviceName, -1)
    if settings.DisplayFrequency == 144:
        settings.DisplayFrequency = 60
    else:
        settings.DisplayFrequency = 144
    win32api.ChangeDisplaySettingsEx(devices.DeviceName, settings)
    update_icon(icon)


def exit_app(icon):
    icon.stop()


def update_icon(icon):
    current_rate = get_refresh_rate()
    image = Image.new('RGB', (16, 16), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 10)
    draw.text((2, 1), str(current_rate), (0, 0, 0), font=font)
    icon.icon = image


def main():
    image = Image.new('RGB', (16, 16), (255, 255, 255))
    icon = pystray.Icon("Refresh Rate Toggler", image)
    icon.menu = (
        pystray.MenuItem('Toggle Refresh Rate', toggle_refresh_rate),
        pystray.MenuItem('Exit', exit_app),
    )
    update_icon(icon)
    icon.run()


if __name__ == '__main__':
    main()
