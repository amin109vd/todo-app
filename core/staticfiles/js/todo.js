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
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const taskListContainer = document.querySelector('.task-list') || document.querySelector('.task-controls').nextElementSibling;

    searchInput.addEventListener('input', function() {
        const query = this.value;

        fetch(`${window.location.pathname}?search-area=${encodeURIComponent(query)}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.text())
        .then(html => {
            taskListContainer.innerHTML = html;
        })
        .catch(err => {
            console.error('Error fetching tasks:', err);
        });
    });
});
