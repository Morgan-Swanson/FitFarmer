from fitfarmer import get_patients, diagnose, recommend

def main():
    patients = get_data_from_csv('../data/')
    diagnostics = [diganose(p) for patient in data]
    for d in diagnostics:
        print(recommend(d))


if __name__ == "__main__":
    main()
