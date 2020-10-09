import argparse
import lgc


def parse_args() -> []:
    parser = argparse.ArgumentParser(description="""""", usage='lcg [arguments] N')
    parser.add_argument('N', help='amount of number', type=int)
    parser.add_argument('-a', help='multiplier', type=float)
    parser.add_argument('-c', help='increment', type=float)
    parser.add_argument('-m', help='modules', type=float)
    parser.add_argument('-x', help='seed or start value', type=float)
    parser.add_argument('-s', help='save to file', dest='filename', type=str)
    parser.add_argument('-p', help='calculate period', action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    generator = lgc.LCG()

    if args.a:
        generator.a = args.a
    if args.c:
        generator.c = args.c
    if args.m:
        generator.m = args.m
    if args.x:
        generator.x = args.x

    numbers = generator.generate_n_numbers(args.N)
    for num in numbers:
        print(num)

    if args.p:
        period = generator.get_period()
        if period == -1:
            print('\033[91m' + 'list too small to calculate period!!!')
        else:
            print('\033[92m' + 'Period = ' + str(period))

    if args.filename:
        generator.save_to_file(args.filename)


if __name__ == '__main__':
    main()
