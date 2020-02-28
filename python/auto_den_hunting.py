from main import *

print(f'Delay for {args.delay} seconds.')
print(f'Pls make sure the den has no watts inside!')
sleep(args.delay)
#send(ns.L3)

def num_dist(a, b):
    cols   = [1, 2, 3,
              1, 2, 3,
              1, 2, 3]
    rows   = [1, 1, 1,
              2, 2, 2,
              3, 3, 3]
    ny = rows[b-1]-rows[a-1]
    nx = cols[b-1]-cols[a-1]
    return nx, ny

def set_password(psw):
    if len(str(psw))!=4:
        raise Exception('Wrong raid password, pls give a 4-digit password.')
    else:
        a =  psw//1000
        b = (psw-a*1000)//100
        c = (psw-a*1000-b*100)//10
        d =  psw-a*1000-b*100-c*10
        print('Current raid password is: {:}{:}{:}{:}'.format(a,b,c,d))
        send(ns_START)
        sleep(1)
        codes = [1,a,b,c,d]
        for num in range(0,4):
            nx,ny = num_dist(codes[num],codes[num+1])
            if nx>0:
                for i in range(0,nx):
                    send(ns_RIGHT)
                    sleep(0.1)
            elif nx<0:
                for i in range(0,-nx):
                    send(ns_LEFT)
                    sleep(0.1)
            if ny>0:
                for i in range(0,ny):
                    send(ns_DOWN)
                    sleep(0.1)
            elif ny<0:
                for i in range(0,-ny):
                    send(ns_UP)
                    sleep(0.1)
            send(ns_A)
            sleep(0.1)
        send(ns_START)
        sleep(1.0)
        send(ns_A)
        sleep(0.5)

def set_flight_mode():
    send(ns_HOME,2)
    for i in range(0,4):
        send(ns_DOWN)
        sleep(0.1)
    send(ns_A)
    send(0.2)
    send(ns_A)
    send(0.2)
    send(ns_B)
    send(0.2)
    send(ns_A)
    sleep(30)

def game_reload():
    # --- game close 
    send(ns_HOME)
    sleep(1.5)
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

def exit_raid(exit_mode):
    if exit_mode == 'flight':
        set_flight_mode()
    elif exit_mode == 'reload':
        game_reload()

def connect_internet():
    send(ns_Y)
    sleep(1)
    send(ns_START)
    sleep(args.connection_time)
    send(ns_A)
    sleep(0.2)
    send(ns_B)
    sleep(2)

def raid():
    connect_internet()
    send(ns_A)
    sleep(4)
    set_password(args.raid_password)
    send(ns_A)
    start_recruit = time.time()
    print('------ recruiting ...')
    while time.time()-start_recruit < args.recruit_duration:
        sleep(1)
    send(ns_UP)
    sleep(0.2)
    send(ns_A)
    sleep(0.5)
    send(ns_A)
    sleep(2)
    start_raid = time.time()
    print('------ raid begin!')
    while time.time()-start_raid < args.battle_duration:
        send(ns_A)
        sleep(0.5)

try:
    if args.exit_mode not in ['flight', 'reload']:
        raise Exception('Wrong exit_mode.')
        send('RELEASE')
        ser.close()
    else:
        raid_counter = 1
        print('Current exit mode: {:} mode.'.format(args.exit_mode))
        while raid_counter >=0:
            now = time.strftime("%H:%M:%S",time.localtime())
            print('[ {:} ] Raid {:} is ready.'.format(now, raid_counter))
            raid()
            exit_raid(args.exit_mode)
            raid_counter += 1
            
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
