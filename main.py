import argparse
from line_overlap import line_overlap

def main():
    parser = argparse.ArgumentParser(
        prog="Line Overlap",
        description="Checks if two lines (x1,x2) and (x3,x4) overlap.",
        )

    parser.add_argument('x', nargs='*', help="Coordinates of lines.")

    args = parser.parse_args()

    if len(args.x) == 0:
        x1 = float(input())
        x2 = float(input())
        x3 = float(input())
        x4 = float(input())
        
        ans = line_overlap(x1, x2, x3, x4)
        print(ans)
    else:
        if len(args.x) != 4:
            print("Wrong number of coordinates.")
            return
        x1 = float(args.x[0])
        x2 = float(args.x[1])
        x3 = float(args.x[2])
        x4 = float(args.x[3])
        
        ans = line_overlap(x1, x2, x3, x4)
        print(ans)

if __name__ == "__main__":
    main()