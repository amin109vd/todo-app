// ---------- Navbar Collapse Animation ----------
document.addEventListener('DOMContentLoaded', () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.getElementById('navbarNav');

    if (navbarToggler) {
        navbarToggler.addEventListener('click', () => {
            navbarCollapse.classList.toggle('show');
        });
    }

    // ---------- Scroll effect for Navbar ----------
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 6px 20px rgba(0,0,0,0.2)';
        } else {
            navbar.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
        }
    });
});

// ---------- Footer optional: current year ----------
document.addEventListener('DOMContentLoaded', () => {
    const yearSpan = document.querySelector('.current-year');
    if(yearSpan){
        yearSpan.textContent = new Date().getFullYear();
    }
});
