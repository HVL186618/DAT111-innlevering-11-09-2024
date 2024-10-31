// toggle visibility av dropdowns
document.addEventListener("DOMContentLoaded", function() {
    const dropdownToggles = document.querySelectorAll(".dropdown-toggle");
    const dropdownContents = document.querySelectorAll(".dropdown-content");

    dropdownToggles.forEach((toggle, index) => {
        toggle.addEventListener("click", function() {
            // toggle display av korresponderende dropdown content
            const dropdownContent = dropdownContents[index];
            if (dropdownContent.style.display === "block") {
                dropdownContent.style.display = "none";
            } else {
                dropdownContent.style.display = "block";
            }
        });
    });

    // de skulle aldri gitt oss makten til å erstatte alle punktum med små ender
    function replacePeriodsWithImage(node) {
        // for alle nodes
        if (node.nodeType === Node.TEXT_NODE) {
            // hvis text node, lag nytt element hvor punktum er erstatta
            let newText = node.textContent.replace(
                /\./g, // Erstatt "."
                '<img src="period.png" alt="." style="width:10px;height:10px;">' // erstatt med bildeelement 
            ).replace(
                /\@/g, // Erstatt "@"
                '<img src="alphaduck.png" alt="@" style="margin-bottom:-5px;width:20px;height:20px;">' // erstatt med bildeelement 
            );

            // element til å ta den nye koden i
            const span = document.createElement('span');
            span.innerHTML = newText; // erstatt koden til ny span med nye koden vår

            // erstatt original node med nytt element
            node.replaceWith(span);
        } else {
            // hvis ikke text node, recur for å sjekke child nodes
            node.childNodes.forEach(replacePeriodsWithImage);
        }
    }

    // nå blir det party her
    document.body.childNodes.forEach(replacePeriodsWithImage);
});

document.addEventListener("DOMContentLoaded", function() {
    const password = document.querySelector(".password-input");
    const confirmPassword = document.querySelector(".confirm-password-input");
    const username = document.querySelector(".username-input");
    const email = document.querySelector(".email-input");
    const form = document.getElementById("registration-form");
    const registerButton = document.getElementById("register-button");

    const passwordMessage = document.getElementById("password-message");
    const confirmPasswordMessage = document.getElementById("confirm-password-message");
    const usernameMessage = document.getElementById("username-message");
    const emailMessage = document.getElementById("email-message");

    function validatePassword() {
        let passwordValue = password.value;

        // password must contain capital letter
        const hasCapitalLetter = /[A-Z]/.test(passwordValue);

        // password must contain number
        const hasNumber = hasCapitalLetter && /\d/.test(passwordValue);

        // password must contain "duck"
        const hasDuck = hasNumber && /duck/i.test(passwordValue);

        // update validation status message
        if (password.value == "") return false;
        else if (!hasCapitalLetter) {
            passwordMessage.textContent = "Password must contain at least one uppercase letter.";
            passwordMessage.className = "message error";
            return false;
        } else if (!hasNumber) {
            passwordMessage.textContent = "Password must contain at least one number.";
            passwordMessage.className = "message error";
            return false;
        } else if (!hasDuck) {
            passwordMessage.textContent = "Password must contain the word 'duck'.";
            passwordMessage.className = "message error";
            return false;
        } else {
            passwordMessage.textContent = "Password meets all requirements!";
            passwordMessage.className = "message success";
            return true;
        }
    }

    function validateConfirmPassword() {
        if (confirmPassword.value == "") return false;
        else if (confirmPassword.value !== password.value) {
            confirmPasswordMessage.textContent = "Passwords do not match.";
            confirmPasswordMessage.className = "message error";
            return false;
        } else {
            confirmPasswordMessage.textContent = "Passwords match!";
            confirmPasswordMessage.className = "message success";
            return true;
        }
    }

    function validateUsername() {
        const usernameValue = username.value;

        // Username cannot be empty or contain spaces
        if (usernameValue === "") {
            usernameMessage.textContent = "Username cannot be empty.";
            usernameMessage.className = "message error";
            return false;
        } else if (/\s/.test(usernameValue)) {
            usernameMessage.textContent = "Username cannot contain spaces.";
            usernameMessage.className = "message error";
            return false;
        } else {
            usernameMessage.textContent = "Username is valid!";
            usernameMessage.className = "message success";
            return true;
        }
    }

    function validateEmail() {
        const emailValue = email.value;

        // Check for text before '@', '@' symbol, and domain format after '@'
        const isValidEmail = /^[^@]+@[a-zA-Z]+\.[a-zA-Z]+$/.test(emailValue);

        if (email.value == "") return false;
        else if (!isValidEmail) {
            emailMessage.textContent = "Email must be in a valid format (e.g., user@domain.com).";
            emailMessage.className = "message error";
            return false;
        } else {
            emailMessage.textContent = "Email is valid!";
            emailMessage.className = "message success";
            return true;
        }
    }

    function checkFormValidity() {
        const isPasswordValid = validatePassword();
        const isConfirmPasswordValid = validateConfirmPassword();
        const isUsernameValid = validateUsername();
        const isEmailValid = validateEmail();
        registerButton.disabled = !(isPasswordValid && isConfirmPasswordValid && isUsernameValid && isEmailValid);
    }

    // Attach event listeners
    password.addEventListener("input", checkFormValidity);
    confirmPassword.addEventListener("input", checkFormValidity);
    username.addEventListener("input", checkFormValidity);
    email.addEventListener("input", checkFormValidity);

    // submission handler
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // prevent default form submission

        if (!validatePassword() || !validateConfirmPassword() || !validateUsername() || !validateEmail()) {
            // disable and style the button with the disabled message
            registerButton.disabled = true;
            registerButton.classList.add("disabled-button");
            registerButton.textContent = "Please fill in all fields to submit";
        } else {
            // redirect to index.html if all validations pass
            window.location.href = "index.html";
        }
    });

});
