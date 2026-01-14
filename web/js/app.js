document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('crawl-form');
    const submitBtn = document.getElementById('submit-btn');
    const errorMessage = document.getElementById('error-message');
    const successMessage = document.getElementById('success-message');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        errorMessage.classList.add('hidden');
        successMessage.classList.add('hidden');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Starting...';

        const startUrl = document.getElementById('start_url').value.trim();
        const maxPages = document.getElementById('max_pages').value;
        const ignorePrefixesRaw = document.getElementById('ignore_prefixes').value;

        const ignorePrefixes = ignorePrefixesRaw
            .split(',')
            .map(p => p.trim())
            .filter(p => p.length > 0);

        const payload = {
            start_url: startUrl,
            max_pages: parseInt(maxPages) || 1000,
            ignore_path_prefixes: ignorePrefixes
        };

        try {
            const response = await fetch('/v1/jobs', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.message || data.error || 'Failed to create job');
            }

            localStorage.setItem(`job_${data.job_id}`, data.token);

            window.location.href = `/status?job_id=${data.job_id}&token=${data.token}`;

        } catch (error) {
            errorMessage.textContent = error.message;
            errorMessage.classList.remove('hidden');
            submitBtn.disabled = false;
            submitBtn.textContent = 'Start Crawl';
        }
    });
});
