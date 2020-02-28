from main import *

print(f'Delay for {args.delay} seconds.')
print(f'Pls check make sure the date is 1 Jan and the cursor is at the right end.')
sleep(args.delay)
#send(ns.L3)

try:
    send(ns_B)
    sleep(1)
    # --- game close 
    send(ns_HOME)
    sleep(1.2)
    send(ns_X)
    sleep(0.5)
    send(ns_A)
    sleep(3.0)
    # --- game open
    send(ns_A)
    sleep(1.5)
    send(ns_A)
    sleep(17)
    send(ns_A)
    sleep(8)
    for nf in range(0,3):
        # --- check raid
        send(ns_A)
        sleep(0.5)
        send(ns_A)
        sleep(0.5)
        send(ns_A)
        sleep(1.0)
        send(ns_A)
        sleep(1.8)
        # --- frame skip
        send(ns_HOME)
        sleep(0.5)
        send(ns_DOWN)
        sleep(0.1)
        for i in range(0,4):
            send(ns_RIGHT,0.1)
            sleep(0.1)
        send(ns_A)
        sleep(0.4)
        send(ns_DOWN,1.5)
        send(ns_A)
        sleep(0.1)
        for i in range(0,4):
            send(ns_DOWN,0.1)
            sleep(0.1)
        send(ns_A)
        sleep(0.4)
        for i in range(0,2):
            send(ns_DOWN,0.1)
            sleep(0.1)
        send(ns_A)
        sleep(0.4)
        # --- change time
        for i in range(0,2):
            send(ns_RIGHT,0.1)
            sleep(0.1)
        send(ns_UP)
        sleep(0.1)
        for i in range(0,3):
            send(ns_RIGHT,0.1)
            sleep(0.1)
        send(ns_A)
        sleep(0.1)
        # --- back to game
        send(ns_HOME)
        sleep(1.0)
        send(ns_HOME)
        sleep(0.5)
        send(ns_B)
        sleep(0.5)
        send(ns_A)
        sleep(4.0)
    # --- check raid
    send(ns_A)
    sleep(0.5)
    send(ns_A)
    sleep(0.5)
    send(ns_A)
    sleep(3.0)

    # --- set time back
    send(ns_HOME)
    sleep(0.5)
    send(ns_DOWN)
    sleep(0.1)
    for i in range(0,4):
        send(ns_RIGHT,0.1)
        sleep(0.1)
    send(ns_A)
    sleep(0.4)
    send(ns_DOWN,1.5)
    send(ns_A)
    sleep(0.1)
    for i in range(0,4):
        send(ns_DOWN)
        sleep(0.1)
    send(ns_A)
    sleep(0.4)
    for i in range(0,2):
        send(ns_DOWN)
        sleep(0.1)
    send(ns_A)
    sleep(0.4)
    # --- change time
    for i in range(0,2):
        send(ns_RIGHT)
        sleep(0.1)
    for i in range(0,3):
        send(ns_DOWN)
        sleep(0.1)
    for i in range(0,3):
        send(ns_RIGHT)
        sleep(0.1)
    send(ns_A)
    sleep(0.1)
    # --- back to game
    send(ns_HOME)
    sleep(1.0)
    send(ns_HOME)
    sleep(0.5)

    send('RELEASE')
    ser.close()
    print('finished. 3 frames are skipped.')

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
