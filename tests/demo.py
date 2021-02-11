import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FitFarmerFolder = os.path.dirname(dir_path)
sys.path.insert(1, FitFarmerFolder)

from fitfarmer.data import get_patient_csv_data
from fitfarmer.diagnose import diagnose
import data


def main():
    patients = get_patient_csv_data(FitFarmerFolder + '/data/patient_mock_data.csv')
    diagnostics = [diagnose(p) for p in patients]
    for d in diagnostics:
        print(d)


if __name__ == "__main__":
    main()
