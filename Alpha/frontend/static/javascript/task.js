function get_task(task_id) {
    task_id = parseInt(task_id, 10);
    fetch(`/get_task/${task_id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        credentials: 'same-origin', 
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            var terminal = document.getElementById('terminal');
            var terminal_author = document.getElementById('terminal-author');
            terminal_author.innerHTML = data.task_author_first_name + ' ' + data.task_author_last_name;
            var terminal_create = document.getElementById('terminal-create');
            terminal_create.innerHTML = data.task_date;
            var terminal_title = document.getElementById('executeTaskModalLabel');
            terminal_title.innerHTML = data.task_title + ' > TASK <span style="color: gray">#'+ data.task_id+'</span>';
            terminal.innerHTML  = data.task_output.replace(/^[\r\n]+/, '');
            // Alterar status do terminal
            var template_status = document.getElementById('terminal-status');
            if (data.task_status == '0') {
                template_status.innerHTML = '<button type="button" class="btn btn-labeled btn-success"><span class="btn-label"><i class="bx bx-check"></i></span>Success</button>'; 
            }
            if (data.task_status != '0'){
                template_status.innerHTML = '<button type="button" class="btn btn-labeled btn-danger"><span class="btn-label"><i class="bx bxs-x-circle"></i></span>Failed</button>'; 
            }
            if (data.task_status == '4'){
                template_status.innerHTML = '<button type="button" class="btn btn-labeled btn-danger"><span class="btn-label"><i class="bx bxs-x-circle"></i></span>Unreachable</button>'; 
            }
        } else {
            console.error(data.message);
        }
    })
    .catch(error => console.error('Failed to get task:', error));
}
