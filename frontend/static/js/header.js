const passwordModal = document.getElementById("changePasswordModal");
const changePasswordLink = document.getElementById("change-password-link");
const cancelBtn3 = document.getElementById("cancelBtn3");
const form = document.getElementById("changePasswordForm");
const currentPassword = document.getElementById("currentPassword");
const newPassword = document.getElementById("newPassword");
const confirmPassword = document.getElementById("confirmPassword");

const usernameModal = document.getElementById("changeUsernameModal");
const changeUsernameLink = document.getElementById("change-username-link");
const cancelBtn1 = document.getElementById("cancelBtn1");
const usernameform = document.getElementById("changeUsernameForm");
const currentUsername = document.getElementById("currentUsername");
const newUsername = document.getElementById("newUsername");
const userUsernameDetails = document.getElementById("user-username-details");
const usernameHomepage = document.getElementById("username-homepage-display");


const nameModal = document.getElementById("changeNameModal");
const changeNameLink = document.getElementById("change-name-link");
const cancelBtn2 = document.getElementById("cancelBtn2");
const nameform = document.getElementById("changeNameForm");
const currentName = document.getElementById("currentName");
const newName = document.getElementById("newName");
const userNameDetails = document.getElementById("user-name-details");


const profileIcon = document.getElementById("profile-icon");
const profileDropdown = document.getElementById("profile-dropdown");


profileIcon.addEventListener("click", function() {
    profileDropdown.classList.toggle("show");
});


window.addEventListener("click", function(event) {
    if (!profileIcon.contains(event.target) && !profileDropdown.contains(event.target)) {
        profileDropdown.classList.remove("show");
    }
});

changePasswordLink.addEventListener("click", function (event) {
    event.preventDefault(); 
    passwordModal.style.display = "block"; 
});

changeUsernameLink.addEventListener("click", function (event) {
    event.preventDefault(); 
    usernameModal.style.display = "block"; 
});

changeNameLink.addEventListener("click", function (event) {
    event.preventDefault(); 
    nameModal.style.display = "block"; 
});


cancelBtn3.addEventListener("click", function () {
    clearInputsPw();
    clearMessagesPw();
    passwordModal.style.display = "none"; 
});

cancelBtn1.addEventListener("click", function () {
    clearInputsUn();
    clearMessages();
    usernameModal.style.display = "none"; 
});

cancelBtn2.addEventListener("click", function () {
    clearInputsN();
    clearMessagesName();
    nameModal.style.display = "none"; 
});


function clearInputsPw() {
    currentPassword.value = '';
    newPassword.value = '';
    confirmPassword.value = '';
}

function clearInputsUn() {
    newUsername.value = '';
}

function clearInputsUnSuccess () {
  
  let newUsernameSaver = newUsername.value;  

  currentUsername.removeAttribute("readonly");
  currentUsername.removeAttribute("disabled");

  currentUsername.value = newUsernameSaver;
  userUsernameDetails.innerHTML = newUsernameSaver;
  usernameHomepage.innerHTML = newUsernameSaver;

  currentUsername.setAttribute("readonly", true);
  currentUsername.setAttribute("disabled", true);

  newUsername.value = '';
}

function clearInputsN() { 
    newName.value = '';
}



function clearInputsNSuccess() {
    let newNameSaver = newName.value;  

    currentName.removeAttribute("readonly");
    currentName.removeAttribute("disabled");

    currentName.value = newNameSaver;
    userNameDetails.innerHTML = newNameSaver;

    currentName.setAttribute("readonly", true);
    currentName.setAttribute("disabled", true);

    newName.value = '';
}

function clearMessages() {
     
    const flashMessages = document.querySelectorAll('.flash-messages ul');
    flashMessages.forEach(messageList => {
        messageList.innerHTML = ''; 
    });
}

function clearMessagesName() {
     
    const flashMessages = document.querySelectorAll('.flash-messages-name ul');
    flashMessages.forEach(messageList => {
        messageList.innerHTML = ''; 
    });
}

function clearMessagesPw() {
     
    const flashMessages = document.querySelectorAll('.flash-messages-pw ul');
    flashMessages.forEach(messageList => {
        messageList.innerHTML = ''; 
    });
}

form.addEventListener("submit", function (event) {
    
    if (!form.checkValidity()) {
        return; 
    }

    
    event.preventDefault(); 

   
    const formData = new FormData(form);

    fetch("/changepassword", {
        method: "POST",
        body: formData,
    })
        .then(response => response.text())
        .then(html => {
            
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");
            const newFlashMessages = doc.querySelector(".flash-messages-pw").innerHTML;

            document.querySelector(".flash-messages-pw").innerHTML = newFlashMessages;

           
            if (doc.querySelector(".flash-messages-pw .success")) {
                
                document.querySelector(".flash-messages-pw").innerHTML = newFlashMessages;
                clearInputsPw();
            }
        })
        .catch(error => {
            console.error("Error processing change password request:", error);
        });
});

usernameform.addEventListener("submit", function (event) { 
    if (!usernameform.checkValidity()) {
        return; 
    }

    event.preventDefault();  

    
    const formData = new FormData(usernameform);

    fetch("/changeusername", {
        method: "POST",
        body: formData,
    })
    .then(response => response.text())
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const newFlashMessages = doc.querySelector(".flash-messages").innerHTML;

        
        document.querySelector(".flash-messages").innerHTML = newFlashMessages;

       
        if (doc.querySelector(".flash-messages .success")) {
            console.log("Success message found.");
            
            
            setTimeout(clearInputsUnSuccess, 100);  
        }
    })
    .catch(error => {
        console.error("Error processing change username request:", error);
    });
});


nameform.addEventListener("submit", function (event) { 
    if (!nameform.checkValidity()) {
        return; 
    }

    event.preventDefault();  

   
    const formData = new FormData(nameform);

    fetch("/changename", {
        method: "POST",
        body: formData,
    })
    .then(response => response.text())
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const newFlashMessages = doc.querySelector(".flash-messages-name").innerHTML;

        document.querySelector(".flash-messages-name").innerHTML = newFlashMessages;

        if (doc.querySelector(".flash-messages-name .success")) {
            console.log("Success message found.");
            
            
            setTimeout(clearInputsNSuccess, 100);  
        }
    })
    .catch(error => {
        console.error("Error processing change name request:", error);
    });
});


const darkmodeToggle = document.getElementById("darkmode-toggle");
const darkmodeIcon = document.getElementById("darkmode-icon");

let isDarkMode = localStorage.getItem("darkmode") === "true"; // If saved, set to true, else false

if (isDarkMode) {
    document.body.classList.add("dark-mode");
    darkmodeIcon.classList.remove("fa-moon");
    darkmodeIcon.classList.add("fa-sun");
}

darkmodeToggle.addEventListener("click", function() {
   
    isDarkMode = !isDarkMode;
    
    if (isDarkMode) {
        document.body.classList.add("dark-mode");
        darkmodeIcon.classList.remove("fa-moon");
        darkmodeIcon.classList.add("fa-sun");
    } else {
        document.body.classList.remove("dark-mode");
        darkmodeIcon.classList.remove("fa-sun");
        darkmodeIcon.classList.add("fa-moon");
    }
    
    localStorage.setItem("darkmode", isDarkMode);
});
