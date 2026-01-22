# Triager

**Triager** is a Django-based bug bounty reporting and triage platform designed to simulate real-world vulnerability disclosure workflows. It enables authenticated users to submit structured vulnerability reports with CVSS severity scoring and proof-of-concept (PoC) files, while administrators review, validate, and triage findings through a secure backend interface.

The platform combines secure web application design with gamification elements such as user dashboards and leaderboards, making it suitable for security training, internal simulations, and hands-on learning of vulnerability management systems.

---

## Why This Project Matters

Modern security teams rely on structured vulnerability intake, severity scoring, and triage pipelines. Triager models this process end-to-end, focusing on:

- Secure handling of user-submitted vulnerability data  
- Clear separation between reporters and reviewers  
- Severity-driven prioritization using CVSS concepts  
- Visibility into reporting status and contributor impact  

This project demonstrates practical experience with **secure backend development**, **access control**, and **security-focused application design**, rather than simple CRUD functionality.

---
## Screenshots

### Recommended Screenshots to Include

1. **Home / Landing Page**
<img width="1208" height="589" alt="image" src="https://github.com/user-attachments/assets/5d1d4b6c-6705-48a8-8d6f-89dda3c396ec" />

2. **Login Page**
<img width="1208" height="588" alt="image" src="https://github.com/user-attachments/assets/b76e9125-2688-451a-b61f-d8775355e174" />

3. **Bug Submission Page**
<img width="1198" height="598" alt="image" src="https://github.com/user-attachments/assets/04100749-07ef-4e6c-b4ae-143cd1db8fb2" />

4. **User Dashboard**
<img width="1207" height="580" alt="image" src="https://github.com/user-attachments/assets/7fb511fc-ac18-4e6c-b485-72dedbaf4905" />

5. **Leaderboard Page**
 <img width="1209" height="590" alt="image" src="https://github.com/user-attachments/assets/f9227a06-42fb-4d2d-8a18-cabf54ea2f7d" />

6. **Admin Panel – Bug Review**
 <img width="1201" height="588" alt="image" src="https://github.com/user-attachments/assets/8df796b2-5a62-4f5d-9785-c3db9b9830a7" />

--- 


## Core Features

### Authentication & Access Control
- Secure user registration and login using Django’s authentication framework
- Protected routes for sensitive actions such as submission, dashboards, and leaderboards

### Vulnerability Reporting
- Structured bug submission with title and CVSS severity score
- Optional proof-of-concept (PoC) file uploads
- Server-side validation and controlled file handling

### Admin Triage Workflow
- Centralized review through Django Admin
- Status lifecycle management: Pending, Approved, Rejected
- Strict separation of user and administrative privileges

### User Dashboard
- Personalized view of all submitted reports
- Real-time visibility into report status and outcomes

### Leaderboard & Gamification
- User ranking based on cumulative CVSS scores of approved reports
- Encourages engagement and competitive learning in controlled environments

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates, HTML, CSS
- **Database:** SQLite
- **Authentication:** Django Auth System
- **File Handling:** Django Media Framework

---

## Project Structure

triager/
├── bugbounty/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── reports/
│ ├── admin.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── templates/
│ ├── home.html
│ ├── submit.html
│ ├── dashboard.html
│ ├── leaderboard.html
│ └── registration/
│ └── login.html
│
├── static/
│ └── css/
│
├── manage.py
└── requirements.txt


---

## Security Considerations

- CSRF protection enabled on all forms
- Authentication enforced on all sensitive routes
- Controlled file uploads via Django’s media handling
- Clear role separation between users and administrators
- Direct access to administrative functionality restricted

> This system is intentionally designed as a **simulation and learning platform**. Production deployment would require additional hardening such as RBAC, advanced input validation, secure storage backends, and monitoring.

---

## Use Cases

- Bug bounty workflow simulation
- Secure web development learning
- Internal security training platforms
- Academic or self-driven cybersecurity projects
- Foundations for CTF-style or internal reporting systems

---

Disclaimer

This project is intended for educational and simulation purposes only. It does not represent a production-ready bug bounty platform and should not be exposed to the public internet without further security hardening.

---
