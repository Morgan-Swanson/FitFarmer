import sys
sys.path.append("../") #the folders below will not import unless I do this
from fitfarmer.data import get_patient_csv_data
from fitfarmer.diagnose import diagnose


def main():
    patients = get_patient_csv_data('../data/patient_mock_data.csv') #"../data" is necessary because data folder is one layer above
    diagnostics = [diagnose(p) for p in patients]
    for d in diagnostics:
        print(d)


if __name__ == "__main__":
    main()
