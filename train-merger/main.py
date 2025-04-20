# main.py

from train import Train, TrainMerger, STATION_DISTANCES


def parse_input(line: str):
    parts = line.strip().split()
    return parts[0], parts[1:]  # TRAIN_A, [ENGINE, NDL, ...]


def main():
    input1 = input().strip()
    input2 = input().strip()

    train_a_name, bogies_a = parse_input(input1)
    train_b_name, bogies_b = parse_input(input2)

    train_a = Train("TRAIN_A", STATION_DISTANCES["TRAIN_A"])
    train_b = Train("TRAIN_B", STATION_DISTANCES["TRAIN_B"])

    train_a.set_bogies(bogies_a[1:])  # skip ENGINE
    train_b.set_bogies(bogies_b[1:])

    print(train_a.get_arrival_order())
    print(train_b.get_arrival_order())

    merger = TrainMerger(train_a, train_b)
    print(merger.get_departure_order())


if __name__ == "__main__":
    main()
