[![Platform](https://img.shields.io/badge/Platform-SEEKreto-orange?style=for-the-badge)](https://github.com/drlyngrc/SEEKreto)
# SEEKreto: An Interactive Web Platform for Classical Encryption and Data Encoding

<details>
  <summary><strong>📖 Table of Contents</strong></summary>

1. [Project Overview](#-project-overview)
2. [Sustainable Development Goals (SDGs)](#-sustainable-development-goals-sdgs)
3. [Key Features](#-key-features)
4. [Project Structure](#-project-structure)
5. [Technologies Used](#-technologies-used)
6. [Getting Started](#-getting-started)
7. [Supported Methods](#-supported-methods)
8. [Usage Guide](#-usage-guide)
9. [Contributors](#-contributors)
10. [Acknowledgement](#-acknowledgement)
11. [Links](#-links)

</details>

## 📘 Project Overview

**SEEKreto** is a web-based application that allows users to securely **encrypt and decrypt data** using classical or traditional cipher techniques such as Caesar Cipher, Vigenère Cipher, and more. It also includes **data representation tools** like Base64 and hexadecimal encoding, offering users practical methods for transforming and protecting information.

Designed with both functionality and education in mind, SEEKreto serves as a **learning platform** for students and cryptography enthusiasts. It provides **hands-on experience** with basic encryption methods, helping users understand fundamental data security principles through interactive exploration.

## 🎯 Who Are the Intended Users?

| **Cryptography Enthusiasts**               | **Students**                     | **General Users**            |
|--------------------------------------------|----------------------------------|-------------------------------|
| Individuals interested in exploring and experimenting with encryption. | Learners from IT related fields who want hands-on experience with classical encryption. | People who need a simple and secure way to encrypt and decrypt sensitive data. |

### 🧩 What Problem Does It Solve?

SEEKreto addresses the **lack of accessible and beginner-friendly platforms** for learning and applying classical encryption techniques. It offers a **user-friendly interface** to:

- Explore and experiment with various ciphers  
- Securely encode sensitive data  
- Bridge the gap between **cryptographic theory and real-world application**

---

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
- **Back-end:** Python, Flask, werkzeug.security (for password hashing)
- **Database:** MySQL  
- **Version Control:** Git & GitHub  
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

## 🔐 Supported Methods
| **Type**               | **Methods Available**                                  | 
|------------------------|--------------------------------------------------------|
| Encryption             | Affine, Atbash, Caesar, Rail Fence, ROT13, Vigenère    |
| Encoding               | Base64, Binary, Hexadecimal, Morse Code                |


## 🚀 Usage Guide
### 1. 🔐 Access, Registration, and Login
- You can **access SEEKreto** without logging in to use the cipher and encoding tools.
- To unlock full features like **Favorites** and **History**, register by providing your **name**, **email**, **username**, and **password**.
- Log in to enable those features and have a personalized experience.

### 2. 🧭 Select a Cipher Tool
- Navigate using the **sidebar** or the **cards on the homepage** to select a cipher or encoding method.
- Choose between **Text to Cipher** or **Cipher to Text**.
- Enter the text you want to **encrypt** or **decrypt**, along with any required keys (e.g., Caesar shift or Vigenère keyword).
- Click the **Convert** button to perform the operation.

### 3. 📤 Results
- The result of your encryption or decryption will be shown in a dedicated **output area** next to the input field.

### 4. ⭐ Favorites (Login Required)
- Logged-in users can mark frequently used ciphers as **favorites**.
- These are saved and displayed in a **Favorites** section for quick future access.

### 5. 🕓 History (Login Required)
- Logged-in users have access to a **History** panel showing previous encryptions and decryptions.
- You can **filter** by cipher type or **sort** by date (newest or oldest) to revisit past actions.

### 6. 🔓 Logout
- When you're finished, click the **Logout** button to securely exit your session.


#### ✨ Whether you're a guest or a registered user, SEEKreto makes classical encryption and data encoding intuitive and fun!

---
## 👥 Contributors

| <img src="./Team%203/jaron.jpg" width="200"/> | <img src="./Team%203/jeff.jpg" width="200"/> | <img src="./Team%203/darlyne.jpg" width="200"/> | <img src="./Team%203/carle.jpg" width="200"/> | <img src="./Team%203/paul.jpg" width="210"/> |
| :--------------------------------------------: | :--------------------------------------------: | :---------------------------------------------: | :---------------------------------------------: | :---------------------------------------------: |
| **[Arquillo, Jaron](https://github.com/JaronLouise)** <br> _JaronLouise_ <br> | **[Balbuena, Jeff](https://github.com/lawrencioqt)** <br> _JeffLawrence_ <br> | **[Lalongisip, Darlyne](https://github.com/drlyngrc)** <br> _Darlyne_ <br> | **[Medina, Carle](https://github.com/controlplusn)** <br> _DevEminent_ <br> | **[Reyes, Paul](https://github.com/par-paulreyes)** <br> _Paul_ <br>|

---

## 🩷 Acknowledgement
  We extend our sincere gratitude to Ms. Fatima Marie P. Agdon, MSCS, for her unwavering guidance and support throughout our Software Engineering project. Her encouragement and direction kept us focused and aligned from start to finish.
  We also thank our fellow team members for their collaboration, dedication, and hard work across every phase of the project—from ideation to deployment.
  Lastly, we appreciate our peers for their valuable feedback and encouragement, which helped us improve SEEKreto every step of the way. 🩷

#### Instructor:  **[Ms. Fatima Marie P. Agdon, MSCS ](https://github.com/marieemoiselle)** - CS 322 | Software Engineering

## 🔗 Links
- 📄 [**Final Report**](https://drive.google.com/file/d/1nX-O0bOsScbo_xkGm7Z1vWBlMnOtrBep/view?usp=sharing)
- 📊 [**Presentation Slides**](https://www.canva.com/design/DAGnPviHTiU/mrsyLEkNFKeD0fVfe7Znag/view?utm_content=DAGnPviHTiU&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hb8bab68973)
- 📈 [**UML Diagrams**](https://drive.google.com/drive/folders/1GDIYkAGs2dePe-nJi8FmnJU84wi6nCdb?usp=sharing) 
- 💻 [**GitHub Repository**](https://github.com/drlyngrc/SEEKreto)

## 🔐 Security Note
This project is for academic purposes only. Do not store or share sensitive or personal data when using the platform.
