import argparse
import time

parser = argparse.ArgumentParser(description="CLI Joemodoro Timer")
parser.add_argument('--work', type=int, default=90, help='Duration of work time (90 x 3 is ideal)')
parser.add_argument('--break-time', type=int, default=30, help='Duration of break')
parser.add_argument('--cycles', type=int, default=3, help='Number of Pomodoro cycles')

args = parser.parse_args()

for cycle in range(1, args.cycles + 1):
    print(f"Session {cycle}: Work for {args.work} minutes.")
    print("---------------------------------------------")
    num_seconds = args.work * 60
    for i in range(num_seconds, 0, -1):
        min_left = i // 60
        sec_left = i % 60
        print(f"{min_left}:{sec_left} left (dial in).", end='\r')
        time.sleep(1)

    print("\a Take a break! ☕️\a")
    for i in range(args.break_time, 0, -1):
        print(f"{i} minutes left of break...", end='\r')
        time.sleep(60)

print("\nGood job doing your Joemodoro sessions!\a")

