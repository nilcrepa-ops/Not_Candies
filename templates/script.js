async function checkDbConnection() {
            const status = document.getElementById('db-status');
            status.textContent = 'Checking connection...';
            status.className = 'db-status';

            try {
                const response = await fetch(`{{ url_for('db_status') }}`);
                const data = await response.json();

                if (response.ok && data.ok) {
                    status.textContent = data.message;
                    status.classList.add('db-ok');
                } else {
                    status.textContent = data.error || 'Unable to connect to database.';
                    status.classList.add('db-fail');
                }
            } catch (error) {
                status.textContent = error.message || 'Connection request failed.';
                status.classList.add('db-fail');
            }
        }