from yeelight import Bulb
from yeelight import discover_bulbs
from yeelight import LightType, Flow, TemperatureTransition, RGBTransition, SleepTransition
import sys, getopt
from googlehomepush import GoogleHome



EntranceBulb = Bulb("mijiacolorbulb-6435.home")
bulb = Bulb("mijiacolorbulb-3ba3.home")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hdcos:a:b:e:")
    except getopt.GetoptError:
        print(getopt.error.msg)
        sys.exit(2)
    for opt, arg in opts:
        
        if opt == '-h' :
            print("\nOpen light by IP address:  \t-t <IP Address>\nClose light by IP address: \t-s <IP Address>\n")
            print("Show ip lights: \t\t-d\nClose all lights: \t\t-c\nOpen all lights: \t\t-o\n")
            print("Light temperature: \t\t-a <1700-6500>\nSet brightness lights: \t\t-b <1-100>\n")
            print("Light color: \t\t-e <0-255> <0-255> <0-255>\nSet brightness lights: \t\t-b <1-100>\n")
        elif opt == '-t':
            Bulb(arg).turn_on()
            print("arg")
        elif opt in ("-s"):
            Bulb(arg).turn_off()
            print(arg)
        elif opt == '-d':
            DiscoBulbs = discover_bulbs(timeout=5)
            #print(DiscoBulbs[0])
            for x in DiscoBulbs :
                print(x.get("ip"))
        elif opt == '-c':
            DiscoBulbs = discover_bulbs(timeout=5)
            for x in DiscoBulbs :
                Bulb(x.get("ip")).turn_off()
        elif opt == '-o':
            DiscoBulbs = discover_bulbs(timeout=5)
            for x in DiscoBulbs :
                Bulb(x.get("ip")).turn_on()
        elif opt == '-a':
            DiscoBulbs = discover_bulbs(timeout=5)
            for x in DiscoBulbs :
                Bulb(x.get("ip")).set_color_temp(int(arg))
        elif opt == '-b':
            DiscoBulbs = discover_bulbs(timeout=5)
            #print(arg)
            for x in DiscoBulbs :
                Bulb(x.get("ip")).set_brightness(int(arg))
            GoogleHome(host="192.168.1.29").say(text="The brightness ligths have been set to" + arg, lang='en-GB')
        elif opt == '-e':
            DiscoBulbs = discover_bulbs(timeout=5)
            #rint(args)
            for x in DiscoBulbs :
                Bulb(x.get("ip")).set_rgb(int(arg),int(args[len(args)-len(args)]),int(args[len(args)-(len(args)-1)]))
        else :
            print('heueeq<f')

if __name__ == "__main__":
    main()