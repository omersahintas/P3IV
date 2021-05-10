import pickle
from p3iv_types.vehicle import Vehicle


class GroundTruth(dict):
    """
    Ground truth data container for vehicles.py
    """

    def __init__(self):
        super(GroundTruth, self).__init__()

    def append(self, vehicle):
        assert isinstance(vehicle, Vehicle)
        assert vehicle.id not in self.keys()
        self[vehicle.id] = vehicle

    def update(self, vehicle):
        assert isinstance(vehicle, Vehicle)
        assert vehicle.id in self.keys()
        self[vehicle.id] = vehicle

    def vehicles(self):
        return self.values()

    def get_vehicle(self, vehicle_id):
        assert vehicle_id in self.keys()
        return self[vehicle_id]

    def dump(self, pickle_filename):
        for v in self.vehicles():
            delattr(v, "modules")
        outfile = open(pickle_filename, "wb")
        pickle.dump(self, outfile, -1)
        outfile.close()

    # todo: cover other types of participants!
