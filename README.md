# Hospital-Appointment-Management-System

Hospital Appointment Management System is a lightweight web application that manages doctor's appointment for patient.


## Sketching Three User Roles

### Admin:
- Has full control over the system.
- Can manage doctor accounts and monitor all appointment activity.
- Responsibilities:
    - Add or remove doctors.
    - View all appointments.
    - Cancel/reschedule any appointment.

### Doctor:
- Manages their own appointment schedule.
- Responsibilities:
    - Set available time slots.
    - View upcoming appointments.
    - Update appointment status.

### Patient:
- Books appointments with doctors.
- Responsibilities:
    - Book appointments
    - Cancel/reschedule any appointment.
    - View upcoming appointments.
    - Search doctors by name or date.



## Features

| Feature                | Who Can Use It         | Description                            |
| ---------------------- | ---------------------- | -------------------------------------- |
| Book Appointment       | Patient                | Book with a selected doctor and time   |
| Cancel Appointment     | Patient, Admin         | Cancel own or any appointment          |
| Reschedule Appointmen  | Patient, Admin         | Change time of an existing appointment |
| View Appointment       | Patient, Doctor, Admin | View relevant upcoming appointments    |
| Search by Doctor       | Patient, Admin         | Filter doctors or appointments by name |




## Project Overview

The Hospital Appointment Management System is a backend service that allows patients to book appointments with doctors, and helps doctors and admins manage medical schedules effectively. The system operates without user login/authentication for now, focusing on core backend logic and features.


| Role    | Description                                           |
| ------- | ----------------------------------------------------- |
| Admin   | Oversees the system, manages doctors and appointments |
| Doctor  | Views and updates their own appointments              |
| Patient | Books, cancels and reschedules their own appointments |



## Tools:

- Python
- Flask
- VsCode
- Github