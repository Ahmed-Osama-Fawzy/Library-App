document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('signupForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        validateForm();
    });

    function validateForm() {
        const usernameInput = document.getElementById('usernameInput');
        const emailInput = document.getElementById('emailInput');
        const passwordInput = document.getElementById('passwordInput');
        const confirmPasswordInput = document.getElementById('confirmPasswordInput');
        const isAdminCheckbox = document.getElementById('isAdminCheckbox');

        const usernameValue = usernameInput.value.trim();
        const emailValue = emailInput.value.trim();
        const passwordValue = passwordInput.value.trim();
        const confirmPasswordValue = confirmPasswordInput.value.trim();
        const isAdmin = isAdminCheckbox.checked;

        // Retrieve accounts from localStorage
        let accounts = JSON.parse(localStorage.getItem('accounts')) || [];

        // Check if email already exists
        const emailExists = accounts.some(acc => acc.email === emailValue);

        if (emailExists) {
            alert('Email already exists');
            emailInput.focus();
            return false;
        }

        const usernamePattern = /^[a-zA-Z0-9]+$/; // Alphanumeric characters only

        if (!usernamePattern.test(usernameValue)) {
            alert('Username cannot contain special characters');
            usernameInput.focus();
            return false;
        }
        

        if (usernameValue === '') {
            alert('Username field cannot be empty');
            usernameInput.focus();
            return false;
        }

        if (emailValue === '') {
            alert('Email field cannot be empty');
            emailInput.focus();
            return false;
        }

        if (passwordValue === '') {
            alert('Password field cannot be empty');
            passwordInput.focus();
            return false;
        }

        if (confirmPasswordValue === '') {
            alert('Confirm Password field cannot be empty');
            confirmPasswordInput.focus();
            return false;
        }

        if (passwordValue !== confirmPasswordValue) {
            alert('Passwords do not match');
            confirmPasswordInput.focus();
            return false;
        }

        if (emailValue.length < 8 || emailValue.length > 35) {
            alert('Email must be between 8 and 35 characters');
            emailInput.focus();
            return false;
        }

        if (passwordValue.length < 9 || passwordValue.length > 25) {
            alert('Password must be between 9 and 25 characters');
            passwordInput.focus();
            return false;
        }

        // If all validations pass, create an account object
        const account = {
            username: usernameValue,
            email: emailValue,
            password: passwordValue,
            isAdmin: isAdmin
        };

        // Store the account object
        storeAccount(account);

        // If all validations pass, submit the form
        alert('Form submitted successfully!');
        form.reset();
    }

    function storeAccount(account) {
        // Retrieve accounts from localStorage or initialize an empty array
        let accounts = JSON.parse(localStorage.getItem('accounts')) || [];

        // Store the account object in the accounts array
        accounts.push(account);

        // Save accounts array back to localStorage
        localStorage.setItem('accounts', JSON.stringify(accounts));

        console.log('Stored Account:', account);
        console.log('All Accounts:', accounts);
    }
});
