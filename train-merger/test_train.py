# test_train.py

import unittest
from train import Train, TrainMerger, STATION_DISTANCES


class TrainMergerTests(unittest.TestCase):

    def test_valid_arrivals(self):
        train_a = Train("TRAIN_A", STATION_DISTANCES["TRAIN_A"])
        train_b = Train("TRAIN_B", STATION_DISTANCES["TRAIN_B"])

        train_a.set_bogies(["NDL", "NDL", "KRN", "GHY", "SLM", "NJP", "NGP", "BLR"])
        train_b.set_bogies(["NJP", "GHY", "AGA", "PNE", "MAO", "BPL", "PTA"])

        self.assertEqual(
            train_a.get_arrival_order(),
            "ARRIVAL TRAIN_A ENGINE NDL NDL GHY NJP NGP"
        )

        self.assertEqual(
            train_b.get_arrival_order(),
            "ARRIVAL TRAIN_B ENGINE NJP GHY AGA BPL PTA"
        )

        merger = TrainMerger(train_a, train_b)
        expected_departure = "DEPARTURE TRAIN_AB ENGINE ENGINE GHY GHY NJP NJP PTA NDL NDL AGA BPL NGP"
        self.assertEqual(merger.get_departure_order(), expected_departure)

    def test_journey_ended(self):
        train_a = Train("TRAIN_A", STATION_DISTANCES["TRAIN_A"])
        train_b = Train("TRAIN_B", STATION_DISTANCES["TRAIN_B"])

        train_a.set_bogies(["SLM", "BLR", "KRN"])  # all before HYB
        train_b.set_bogies(["TVC", "SRR", "MAQ", "MAO"])  # all before HYB

        self.assertIn("JOURNEY_ENDED", train_a.get_arrival_order())
        self.assertIn("JOURNEY_ENDED", train_b.get_arrival_order())

        merger = TrainMerger(train_a, train_b)
        self.assertIn("JOURNEY_ENDED", merger.get_departure_order())


if __name__ == '__main__':
    unittest.main()
