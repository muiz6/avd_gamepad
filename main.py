import subprocess

import hid


def trigger_adb_event(id):
    subprocess.run(f'adb shell input keyevent {id}', shell=True)


def trigger_adb_roll(x, y):
    subprocess.run(
        f'adb shell input joystick roll {x} {y}', shell=True)


def main():
    for device in hid.enumerate():
        print(
            f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

    gamepad = hid.device()
    gamepad.open(0x0810, 0x0001)
    gamepad.set_nonblocking(True)

    while True:
        report = gamepad.read(64)
        if report:
            if report[5] == 0:
                print('Up pressed')
                trigger_adb_event(19)

            if report[5] == 4:
                print('Down pressed')
                trigger_adb_event(20)

            if report[5] == 6:
                print("left pressed")
                trigger_adb_event(21)

            if report[5] == 2:
                print("right pressed")
                trigger_adb_event(22)

            if report[3] == 127 and report[4] == 127:
                trigger_adb_roll(0, 0)

            if report[5] == 31:
                print("y pressed")
                trigger_adb_event(100)

            if report[5] == 47:
                print("b pressed")
                trigger_adb_event(97)

            if report[5] == 79:
                print("a pressed")
                trigger_adb_event(96)

            if report[5] == 143:
                print("x pressed")
                trigger_adb_event(99)

            if report[6] == 2:
                print('l1 pressed')
                trigger_adb_event(103)

            if report[6] == 4:
                print('l2 pressed')
                trigger_adb_event(104)

            if report[6] == 1:
                print('r1 pressed')
                trigger_adb_event(102)

            if report[6] == 8:
                print('r2 pressed')
                trigger_adb_event(105)

            if report[6] == 32:
                print('start pressed')
                trigger_adb_event(108)

            if report[6] == 16:
                print('select pressed')
                trigger_adb_event(109)

            if report[6] == 64:
                print('thumbl pressed')

            if report[6] == 128:
                print('thumbr pressed')

            trigger_adb_roll((report[3] - 127) / 127, (report[4] - 127) / 127)

            print(report)


if __name__ == '__main__':
    main()
