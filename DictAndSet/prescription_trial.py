import prescription_data
from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

print(patients)
print()
# Remove warfarin and add edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Could not remove warfarin as Patient {patient} is not taking Warfarin."
              f"Please remove {patient} from the trial")
    print(patient, prescription)
