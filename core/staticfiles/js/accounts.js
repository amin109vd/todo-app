const togglePassword = document.getElementById('togglePassword');
const passwordField = document.getElementById('id_password');

togglePassword.addEventListener('click', function () {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);

    // تغییر کلاس آیکون
    this.classList.toggle('bi-eye');
    this.classList.toggle('bi-eye-slash');
});
