// Optional: simple fade effect on toggle
document.querySelectorAll('.form-check-input').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const card = this.closest('.todo-card');
        if (this.checked) {
            card.querySelector('.task-title').classList.add('completed');
        } else {
            card.querySelector('.task-title').classList.remove('completed');
        }
    });
});
