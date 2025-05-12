[![Platform](https://img.shields.io/badge/Platform-SEEKreto-orange?style=for-the-badge)](https://github.com/drlyngrc/SEEKreto)
# SEEKreto: An Interactive Web Platform for Classical Encryption and Data Encoding

<details>
  <summary><strong>📖 Table of Contents</strong></summary>

1. [Introduction](#-introduction)
2. [Sustainable Development Goals (SDGs)](#-sustainable-development-goals-sdgs)
3. [Key Features](#-key-features)
4. [Project Structure](#-project-structure)
5. [Technologies Used](#-technologies-used)
6. [Getting Started](#-getting-started)
7. [Contributors](#-contributors)
8. [Acknowledgement](#-acknowledgement)
9. [Links](#-links)

</details>

## 📌 Introduction
**SEEKreto** is an interactive cryptography platform that allows users to encrypt and decrypt messages using classical ciphers like Caesar, Vigenère, and more. Aimed at promoting digital literacy and security awareness, SEEKreto also serves as an educational tool, making encryption fun and accessible. Users can create account, save favorites, view encryption history, and switch between light and dark modes—all within a responsive, intuitive UI.


## 🌍 Sustainable Development Goals (SDGs)
> **📘 SDG 4: Quality Education**  
> Promotes digital literacy by educating users on classical encryption methods in an accessible and interactive way.

> **🔧 SDG 9: Industry, Innovation and Infrastructure**  
> Encourages innovation by integrating cryptographic tools into a modern, user-friendly web application.

> **🛡️ SDG 16: Peace, Justice and Strong Institutions**  
> Encourages responsible use of cryptography and supports secure communication, promoting trust and ethical digital practices.

---

## 🌟 Key Features
|                            | **Description**                                                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **🔐 User Authentication** | Secure registration and login system with hashed passwords. Session-based authentication enables a personalized experience. Includes “Forgot Password” via email recovery.  |
| **🧠 Cryptography Tools**  | Encode and decode text using classical ciphers and encoding schemes. Designed with a fun and user-friendly interface for both educational and casual use.                  |
| **🖥️ User-Friendly Interface** | Features intuitive layout, consistent design across cipher pages, with sidebars and headers for smooth navigation.                                                              |
| **⭐ Favorites & 🕘 History**| Users can mark favorite tools for quick access and view recent encryption/decryption activity. Includes filtering by cipher type and sorting by time.                      |
| **📝 Profile Editing**     | Lets users update profile details such as username, name, and password, ensuring flexibility and personalization.                                                            |
| **🌙 Dark Mode**           | Offers a comfortable dark theme for low-light environments, reducing eye strain and enhancing visual experience.                                                             |
| **📱 Responsive Design**   | Fully responsive layout ensures accessibility across various devices, browsers, and screen sizes.                                                                            |


## 📁 Project Structure
<pre>
SEEKreto
├── Team 3                   # Photos of the contributors
├── backend                  # Backend code (Flask app)
│   ├── pycache              
│   ├── app.py               
│   └── requirements.txt     
├── db                       # Database-related files
│   └── schema.sql           
├── fronted                  # Frontend code (HTML, CSS, JS)
│   ├── static               # Static assets
│      ├── images            
│      ├── js               
│      └── styles            
│   └── templates            # HTML templates for frontend pages
└── README.md                # Project documentation

</pre>


---

## 💻 Technologies Used
- **Front-end:** HTML, CSS, JavaScript  
- **Back-end:** Node.js, Express.js  
- **Database:** MySQL  
- **Version Control:** Git & GitHub  
- **Tools & Libraries:** 
- **Deployment:** GitHub Pages

---

## 🚀 Getting Started

Follow the steps below to run SEEKreto on your local machine.

### 🛠️ Prerequisites
- Python 3.8 or above
- MySQL Server
- Git

### 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/drlyngrc/SEEKreto.git
   cd SEEKreto
2. **Set up the database**
  - Open MySQL and create a database:
       ```bash
       CREATE DATABASE seekreto_db;
  -  Then import the schema:
       ```sql
       USE seekreto_db;
       SOURCE db/schema.sql;
3. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install backend dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```
5. **Run the backend server**
   ```bash
   cd backend
   python app.py
   ```
6. **Access the platform**
   - Open your browser and go to: http://127.0.0.1:5000

---

## 👥 Contributors

| <img src="./Team%203/jaron.jpg" width="200"/> | <img src="./Team%203/jeff.jpg" width="200"/> | <img src="./Team%203/darlyne.jpg" width="200"/> | <img src="./Team%203/carle.jpg" width="200"/> | <img src="./Team%203/paul.jpg" width="200"/> |
| :--------------------------------------------: | :--------------------------------------------: | :---------------------------------------------: | :---------------------------------------------: | :---------------------------------------------: |
| **[Arquillo, Jaron](https://github.com/JaronLouise)** <br> _JaronLouise_ <br> | **[Balbuena, Jeff](https://github.com/lawrencioqt)** <br> _JeffLawrence_ <br> | **[Lalongisip, Darlyne](https://github.com/drlyngrc)** <br> _Darlyne_ <br> | **[Medina, Carle](https://github.com/controlplusn)** <br> _DevEminent_ <br> | **[Reyes, Paul](https://github.com/par-paulreyes)** <br> _Paul_ <br>|

## 🩷 Acknowledgement
  We extend our sincere gratitude to Ms. Fatima Marie P. Agdon, MSCS, for her unwavering guidance and support throughout our Software Engineering project. Her encouragement and direction kept us focused and aligned from start to finish.
  We also thank our fellow team members for their collaboration, dedication, and hard work across every phase of the project—from ideation to deployment.
  Lastly, we appreciate our peers for their valuable feedback and encouragement, which helped us improve SEEKreto every step of the way. 🩷

## 🔗 Links
- 📄 [**Final Report**](https://drive.google.com/file/d/1nX-O0bOsScbo_xkGm7Z1vWBlMnOtrBep/view?usp=sharing)
- 📊 [**Presentation Slides**](link)
- 💻 [**GitHub Repository**](https://github.com/drlyngrc/SEEKreto)

## 🔐 Security Note
This project is for academic purposes only. Do not store or share sensitive or personal data when using the platform.
