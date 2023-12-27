document.getElementById('createTemplateForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    var title = document.getElementById('templateTitle').value;
    var version = document.getElementById('templateVersion').value;
    var playbook = document.getElementById('playbookSelect').value;
    var inventory = document.getElementById('inventorySelect').value;
    var projectId = document.getElementById('projectId').value;

    // Realiza uma solicitação AJAX para a view de criação de template
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_template/', true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); 

    
    var formData = new FormData();
    formData.append('title', title);
    formData.append('version', version);
    formData.append('playbook', playbook);
    formData.append('inventory', inventory);
    formData.append('project_id', projectId);

    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        if (response.success) {
            var close_modal = document.getElementById('close_modal');
            close_modal.click()
            console.log('Template create successfully! ID #', response.template_id);
            document.getElementById('result').innerHTML = 'Template created successfully! ID #' + response.template_id;

            var get_table = document.getElementById('templateTable');

            var new_table = '<tr class="tb-height" id="templateID' + response.template_id + '"><td><a href="/project/task/' + projectId + '/' + response.template_id +'/">' +  response.template_title + '<span style="color: grey;"> #' + response.template_id + '</a></span></td><td>' + response.template_version + '</td><td>' + response.template_playbook + '</td><td>'+ response.template_inventory + '<td><button class="bx bx-play-circle btn-modal" data-bs-toggle="modal" data-bs-target="#executeTaskModal" onclick="execute_template('+ projectId + ',' + response.template_id +')"></button><i class="bx bxs-cog btn-delete"></i><i class="bx bxs-x-circle btn-delete" onclick="delete_template(' + projectId + ',' + response.template_id + ')"></i></td></tr>';
            get_table.innerHTML += new_table;
            //Clear form
            document.getElementById("createTemplateForm").reset()
        } else {
            console.error('Failed to create template.');
            document.getElementById('result').innerHTML = 'Failed to create template.';
        }
    };
    xhr.send(formData);
});


function delete_template(projectId, templateId) {
    projectId = parseInt(projectId, 10);
    templateId = parseInt(templateId, 10);
    fetch(`/delete_template/${projectId}/${templateId}`, {
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
            console.log('Template deleted successfully.');
            var table_id = 'templateID' + templateId;
            var delete_table = document.getElementById(table_id);
            if (delete_table) {
                delete_table.parentNode.removeChild(delete_table);
            }
        } else {
            console.error(data.message);
        }
    })
    .catch(error => console.error('Failed to delete Template: ', error));
}



function new_task(title, author, author_last_name, status, create,) {
    var terminal_title = document.getElementById('executeTaskModalLabel');
    var terminal_author = document.getElementById('template-author');
    var terminal_status = document.getElementById('template-status');
    var terminal_create = document.getElementById('template-create');

    author = author + ' ' + author_last_name;
    terminal_title.innerHTML = title + ' > Awaiting processing';
    terminal_author.innerHTML = author;
    terminal_create.innerHTML= create;
    var dataAtual = new Date();
    var terminal = document.getElementById('terminal');
    terminal.innerHTML  = '<div class="div_output"><span class="hour_output">[' + dataAtual.toLocaleTimeString()+']</span><span style="margin-left: 15px;"><pre>############### Welcome to SwitchSetup ############ </pre></span></div>'
    terminal.innerHTML  += '<div class="div_output"><span class="hour_output">[' + dataAtual.toLocaleTimeString()+']</span><span style="margin-left: 15px;"><pre>############### Ansible execution ############ </pre></span></div>'
    terminal.innerHTML  += '<div class="div_output"><span class="hour_output">[' + dataAtual.toLocaleTimeString()+']</span><span style="margin-left: 15px;"><pre><span style="color: yellow">Wait for the data to be processed</span> </pre></span></div>'
    terminal.innerHTML  += '<div class="div_output"><span class="hour_output">[' + dataAtual.toLocaleTimeString()+']</span><span style="margin-left: 15px;"><pre><span style="color: yellow">The data will soon be displayed here on the terminal</span> </pre></span></div>'
    
}



function execute_template(projectId, templateId) {
    projectId = parseInt(projectId, 10);
    templateId = parseInt(templateId, 10);
    fetch(`/execute_template/${projectId}/${templateId}`, {
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
            var dataAtual = new Date();
            console.log('Template was executed successfully');
            var terminal = document.getElementById('terminal');
            
            console.log(data.status);
            var terminal_title = document.getElementById('executeTaskModalLabel');
            terminal_title.innerHTML = data.template_title + ' > TASK <span style="color: gray">#'+ data.task_id+'</span>';

            for (let index = 0; index < data.terminal_output.length; index++) {
                if (data.terminal_output[index] != "") { 
                    terminal.innerHTML  += data.terminal_output[index].replace(/^[\r\n]+/, '');
                }
                
            }
            // Alterar status do terminal
            var template_status = document.getElementById('template-status');
            if (data.status == 0) {
                template_status.innerHTML = '<button type="button" class="btn btn-labeled btn-success"><span class="btn-label"><i class="bx bx-check"></i></span>Success</button>'; 
            }
            if (data.status != 0){
                template_status.innerHTML = '<button type="button" class="btn btn-labeled btn-danger"><span class="btn-label"><i class="bx bxs-x-circle"></i></span>Failed</button>'; 

            }
        } else {
            console.error(data.message);
        }
    })
    .catch(error => console.error('Fail to execute Template: ', error));
}