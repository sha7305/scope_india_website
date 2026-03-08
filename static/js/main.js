document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.registration-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const timings = document.querySelectorAll('input[name="preferred_timings"]:checked');
            if (timings.length === 0) {
                e.preventDefault();
                alert('Please select at least one preferred training timing.');
            }
        });
    }
});