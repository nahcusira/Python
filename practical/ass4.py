import argparse, math


parser = argparse.ArgumentParser()
parser.add_argument('--x','--x', type=float, metavar='', required=True, help='value x')
parser.add_argument('--y','--y', type=float, metavar='', required=True, help='value y')
parser.add_argument('-add', '--add', action='store_true', help='add')
parser.add_argument('-sub', '--subtract', action='store_true', help='subtract')
parser.add_argument('-mul', '--multiply', action='store_true', help='multiply')
parser.add_argument('-div', '--divide', action='store_true', help='divide')
parser.add_argument('-root', '--root', action='store_true', help='root')
parser.add_argument('-log', '--logarithm', action='store_true', help='logarithm')
args = parser.parse_args()

if args.add:
    print('{:.3f}'.format(args.x + args.y))
if args.subtract:
    print('{:.3f}'.format(args.x - args.y))
if args.divide:
    if args.y < 0:
        print('can divide by 0')
    print('{:.3f}'.format(args.x / args.y))
if args.multiply:
    print('{:.3f}'.format(args.x * args.y))
if args.root:
    print('{:.3f}'.format(math.pow(args.x, args.y)))
if args.logarithm:
    print('{:.3f}'.format(math.log(args.x, args.y)))