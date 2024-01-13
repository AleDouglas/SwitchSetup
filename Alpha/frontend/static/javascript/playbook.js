document.getElementById('createPlaybookForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    var title = document.getElementById('playbookTitle').value;
    var description = document.getElementById('playbookDescription').value;
    var playbookFile = document.getElementById('playbookFile').files[0]; 
    var projectId = document.getElementById('projectId').value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_playbook/', true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); 

    
    var formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('playbook_file', playbookFile);
    formData.append('project_id', projectId);

    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        if (response.success) { 
            var close_modal = document.getElementById('close_modal');
            close_modal.click()
            console.log('Playbook created successfully ID #', response.playbook_id);
            document.getElementById('result').innerHTML = 'Playbook created successfully! ID #' + response.playbook_id;

            var get_table = document.getElementById('playbookTable');
            const data = new Date(response.playbook_time);
            const options = {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
                hour12: true,
            };

            const date_time = new Intl.DateTimeFormat('en-US', options).format(data);
            var new_table = '<tr class="tb-height" id="playbookID' + response.playbook_id + '"><td>' +  response.playbook_title + '<span style="color: grey;"> #' + response.playbook_id + '</span></td><td>' + response.playbook_description + '</td><td>' + date_time + '<td><i class="bx bxs-x-circle btn-delete" data-bs-toggle="modal" data-bs-target="#RemoveModal" onclick="delete_modal(' + projectId + ',' + response.playbook_id + ')"></i></td></tr>';
            get_table.innerHTML += new_table;


            //Clear form
            document.getElementById("createPlaybookForm").reset()
        } else {
            console.error('Failed to create Playbook.');
            document.getElementById('result').innerHTML = 'Failed to create Playbook.';
        }
    };

    // Envia a solicitação AJAX usando FormData
    xhr.send(formData);
});


function delete_playbook(projectId, playbookId) {
    projectId = parseInt(projectId, 10);
    playbookId = parseInt(playbookId, 10);
    fetch(`/delete_playbook/${projectId}/${playbookId}`, {
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
            console.log('Playbook deleted successfully.');
            var table_id = 'playbookID' + playbookId;
            var delete_table = document.getElementById(table_id);
            if (delete_table) {
                delete_table.parentNode.removeChild(delete_table);
            }
        } else {
            console.error(data.message);
        }
    })
    .catch(error => console.error('Failed to delete Playbook:', error));
}