#!/usr/bin/env python3

import csrmesh as cm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', type=int, required=True, help='4 digit mesh PIN number')
    parser.add_argument('--dest', type=str, required=True, help='Destination address in aa:bb:cc:dd:ee:ff format')
    parser.add_argument('--level', type=int, default=255, help='Overall level (0-255)')
    parser.add_argument('--red', type=int, default=255, help='Red brightness (0-255)')
    parser.add_argument('--green', type=int, default=255, help='Green brightness (0-255)')
    parser.add_argument('--blue', type=int, default=255, help='Blue brightness (0-255)')
    args = parser.parse_args()
    
    p = cm.make_packet(cm.network_key(args.pin),cm.random_seq(),cm.light_set_cmd(args.level,args.red,args.green,args.blue))
    cm.send_packet(args.dest,p)
