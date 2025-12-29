from src.models.specialization import Specialization


class OperationManager:
    def __init__(self):
        self.specs=[]

    def options(self):
        print("RK Hospitals")
        choices=['1) Add a new Patient','2) Print all patients','3) Remove a patient','4) Get Next Patient,"5) Exit']
        print("\n".join(choices))
        choice=input("Enter your Choice")
        return int(choice)

    def run(self):
        choice=self.options()

        while True:
            if choice == 1:
                print("ADD NEW PATIENT")
                spec_name=str(input("Enter Specialization : ")).strip()
                patient_name=str(input("Enter Patient Name : ")).strip()
                patient_status=str(input("Enter Patient Status : ")).strip()
                spec_found=None
                spec_exist=False


                for specialization in self.specs:
                    if specialization.name==f"{spec_name} Specialization":
                        spec_found=specialization
                        spec_exist=True

                if spec_exist:
                    spec_found.add_new_patient(patient_name, int(patient_status))
                    print("Done")

                else:
                    new_spec = Specialization(spec_name)
                    new_spec.add_new_patient(patient_name, int(patient_status))
                    self.specs.append(new_spec)
                    print("Specialization Created and Patient Data Added")



            elif choice == 2:
                for specialization in self.specs:
                    print(f"Specialization : {specialization.name}")
                    specialization.print_patients()
                    print("----------------------------------------------------------------------------------")

            elif choice == 4:
                spec=str(input("Enter Specialization name :  "))
                found=False
                for specialization in self.specs:
                    if specialization.name == f"{spec} Specialization":
                        specialization.get_next_patient()
                        found=True
                        break
                if not found:
                    print("There is no such specialization")

            elif choice == 3:
                spec = str(input("Enter Specialization name :  "))
                found = False
                for specialization in self.specs:
                    if specialization.name == f"{spec} Specialization":
                        patient_name=str(input("Enter Patient Name")).strip()
                        ''' try:
                            specialization.remove_patient(patient_name)
                            print("Patient has been removed")
                        except:
                            print("No such specialization")'''
                        found = True
                        specialization.remove_patient(patient_name)
                        break
                if not found:
                    print("There is no such specialization")

            elif choice == 5:
                break

            else:
                print("Invalid option. Please select a valid one")

            choice=self.options()


