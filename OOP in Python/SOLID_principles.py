## SOLID Principles
# S : Single Responsibility Principle
# O : Open and Closed Principle
# L : Liskov Substitution Principle
# I : Interface Segregation Principle
# D : Dependency Inversion Principle

""""
📌 Real-Life Problem: Building a Hospital Management System (HMS)
Scenario

You’re building a backend for a Hospital Management System that manages:
	•	Patient registrations 🧑‍⚕️
	•	Doctor schedules 👩‍⚕️
	•	Billing 💳
	•	Notifications (SMS/Email/Push) 📩
"""
import sys
from typing import Iterable

PATIENTS = []

from abc import ABC, abstractmethod
import json

class Patient:
    def __init__(self, name, address, phone, email, age):
        self.name = name
        self.address = address
        self.phone = phone
        self.age = age
        self.email = email


class RegisterPatient(ABC):
    @abstractmethod
    def supports(self, patient):
        pass

    @abstractmethod
    def register(self, patient):
        pass


class SeniorCitizenPatientRegistration(RegisterPatient):
    def supports(self, patient):
        return patient.age >= 60

    def register(self, patient):
        patient_dict = patient.__dict__
        patient_dict['senior_citizen'] = True
        PATIENTS.append(patient_dict)
        print("Senior Citizen Patient Registered !")


class GeneralPatientRegistration(RegisterPatient):
    def supports(self, patient):
        return patient.age < 60

    def register(self, patient):
        patient_dict = patient.__dict__
        patient_dict['senior_citizen'] = False
        PATIENTS.append(patient_dict)
        print("General Patient Registered !")


# Application Service or logic
class RegistrationService:
    @staticmethod
    def register(patient: Patient):
        RegistrationService.register_patient(
            patient=patient,
            register_strategies=[
                SeniorCitizenPatientRegistration(),
                GeneralPatientRegistration()
            ]
        )

    @staticmethod
    def register_patient(patient: Patient, register_strategies: Iterable[RegisterPatient]):
        for strategy in register_strategies:
            if strategy.supports(patient):
                strategy.register(patient)


class DisplayDataService:
    @classmethod
    def show_patients(cls):
        print("Total Patients Registered : ", len(PATIENTS))
        print("Patient Details: ", json.dumps(PATIENTS, indent=4))


# Client or User
class Client:
    @staticmethod
    def get_patient_details():
        try:
            name = input("Enter the Name of the Patient : ")
            if str.lower(name) == "exit":
                DisplayDataService.show_patients()
                sys.exit()
            address = input("Enter the Address of the Patient : ")
            phone = input("Enter the phone number of the Patient : ")
            age = int(input("Enter the AGE of the patient : "))
            email = input("Enter the email id of the patient : ")
            return Patient(name, address, phone, email, age)
        except ValueError as e:
            DisplayDataService.show_patients()
            print("Invalid inputs passed...")
            sys.exit()

    @staticmethod
    def register_patient(patient: Patient):
        RegistrationService.register(patient=patient)


def main():
    # Only call the registration process
    while True:
        new_patient = Client.get_patient_details()
        Client.register_patient(new_patient)


if __name__ == "__main__":
    main()