from src.models.specialization import Specialization

def populate_user_data(app_obj):
    import random
    for i in range(1,6):
        new_spec=Specialization(str(i))
        for j in range(6):
            patient_name=f"patient {j}"
            new_spec.add_new_patient(patient_name,random.randint(0,2))
        app_obj.specs.append(new_spec)