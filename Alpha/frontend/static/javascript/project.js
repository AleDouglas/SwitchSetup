document.getElementById('createProjectForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    var title = document.getElementById('title').value;
    var password = document.getElementById('password').value;

    // Realiza uma solicitação AJAX para a view de criação de projeto
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_project/', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    // Passa o token CSRF no corpo da solicitação
    var data = 'title=' + encodeURIComponent(title) + '&password=' + encodeURIComponent(password) + '&csrfmiddlewaretoken=' + encodeURIComponent('{{ csrf_token }}');
    
    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        if (response.success) {
            var get_card = document.getElementById('card-new');
            var new_card = '<div class="card-principal" id="card-id' + response.project_id +'"><div class="project-info"><i class="bx bxs-archive project-icon"></i><a href=/project/dashboard/'+ response.project_id + '/>' + response.project_title + '</a></div><i class="bx bxs-x-circle btn-delete" onclick="delete_project('+ response.project_id +')"></i></div>';
            get_card.innerHTML += new_card;
            document.getElementById('result').innerHTML = 'Project created successfully! Project ID: ' + response.project_id;
        } else {
            document.getElementById('result').innerHTML = 'Failed to create the project.';
        }
    };
    xhr.send(data);
});

function delete_project(projectId) {
    projectId = parseInt(projectId, 10);
    fetch(`/delete_project/${projectId}/`, {
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
            console.log('Project deleted successfully.');
            var card_id = 'card-id' + projectId
            var delete_div = document.getElementById(card_id);
            if (delete_div) {
                delete_div.parentNode.removeChild(delete_div);
            }
        } else {
            console.error(data.message);
        }
    })
    .catch(error => console.error('Error deleting project:', error));
}