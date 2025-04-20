# train.py

from typing import List, Dict

STATION_DISTANCES = {
    "TRAIN_A": {
        "CHN": 0, "SLM": 350, "BLR": 550, "KRN": 900,
        "HYB": 1200, "NGP": 1600, "ITJ": 1900,
        "BPL": 2000, "AGA": 2500, "NDL": 2700
    },
    "TRAIN_B": {
        "TVC": 0, "SRR": 300, "MAQ": 600, "MAO": 1000,
        "PNE": 1400, "HYB": 2000, "NGP": 2400,
        "ITJ": 2700, "BPL": 2800, "PTA": 3800,
        "NJP": 4200, "GHY": 4700, "AGA": 2500
    }
}

HYB_DISTANCE = {
    "TRAIN_A": 1200,
    "TRAIN_B": 2000
}


class Train:
    def __init__(self, name: str, route_map: Dict[str, int]):
        self.name = name
        self.route_map = route_map
        self.bogies: List[str] = []

    def set_bogies(self, bogie_list: List[str]):
        self.bogies = [bogie for bogie in bogie_list if bogie in self.route_map]

    def get_bogies_after_hyderabad(self) -> List[str]:
        hyb_distance = HYB_DISTANCE[self.name]
        return [bogie for bogie in self.bogies if self.route_map[bogie] > hyb_distance]

    def get_arrival_order(self) -> str:
        valid_bogies = self.get_bogies_after_hyderabad()
        if valid_bogies:
            return f"ARRIVAL {self.name} ENGINE " + " ".join(valid_bogies)
        return f"ARRIVAL {self.name} ENGINE JOURNEY_ENDED"


class TrainMerger:
    def __init__(self, train_a: Train, train_b: Train):
        self.train_a = train_a
        self.train_b = train_b

    def get_departure_order(self) -> str:
        bogies_a = self.train_a.get_bogies_after_hyderabad()
        bogies_b = self.train_b.get_bogies_after_hyderabad()

        combined = bogies_a + bogies_b
        distance_map = {**STATION_DISTANCES["TRAIN_A"], **STATION_DISTANCES["TRAIN_B"]}

        sorted_bogies = sorted(
            combined,
            key=lambda station: distance_map[station],
            reverse=True
        )

        if sorted_bogies:
            return "DEPARTURE TRAIN_AB ENGINE ENGINE " + " ".join(sorted_bogies)
        return "DEPARTURE TRAIN_AB ENGINE ENGINE JOURNEY_ENDED"
