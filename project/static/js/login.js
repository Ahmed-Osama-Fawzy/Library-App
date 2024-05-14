document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        validateForm();
    });

    function validateForm() {
        const emailInput = document.querySelector('input[type="email"]');
        const passwordInput = document.querySelector('input[type="password"]');
        const emailValue = emailInput.value.trim();
        const passwordValue = passwordInput.value.trim();

        const accounts = JSON.parse(localStorage.getItem('accounts')) || [];

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

    
        const account = accounts.find(acc => acc.email === emailValue);

        if (!account || account.password !== passwordValue) {
            alert('Wrong password or email');
            return false;
        }

        console.log('Found Account:', account);

      
        console.log('isAdmin:', account.isAdmin);

      
        if (account.isAdmin) {
            
            window.location.href = 'AdminHomePage.html';
        } else {
         
            window.location.href = 'UserHomePage.html';
        }
    }
});
