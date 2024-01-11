document.getElementById('newKeyForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    var project_id = document.getElementById('project_id').value;
    var title = document.getElementById('key_title').value;
    var add_inventory = document.getElementById('add_inventory').checked;
    var add_playbook = document.getElementById('add_playbook').checked;
    var add_template = document.getElementById('add_template').checked;
    var remove_items = document.getElementById('remove_items').checked;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_key/', true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); 
    var formData = new FormData();
    formData.append('title', title);
    formData.append('add_inventory', add_inventory);
    formData.append('add_playbook', add_playbook);
    formData.append('add_template', add_template);
    formData.append('remove_items', remove_items);
    formData.append('project_id', project_id);

    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        if (response.success) {
            var close_modal = document.getElementById('close_modal');
            close_modal.click()
            console.log('Key create successfully! ID:');
            document.getElementById('result').innerHTML = 'Key create successfully! ID: ' + response.inventory_id;
            
            var get_table = document.getElementById('KeyTable');

            var new_table = '<tr class="tb-height" id="KeyID'+ response.key_id +'">';
            new_table += '<td>' + response.key_title + '#' + response.key_id + '</td>';
            new_table += '<td style="color: red;">' + response.key_inventory +'</td>';
            new_table += '<td style="color: red;">' + response.key_playbook +'</td>';
            new_table += '<td style="color: red;">' + response.key_template +'</td>';
            new_table += '<td style="color: red;">' + response.key_remove +'</td>';
            new_table += '<td><i' + ' onclick="delete_key('+ project_id +','+ response.key_id +')"'+ 'class="bx bxs-x-circle btn-delete"></i></td></tr>';
            get_table.innerHTML += new_table;

            //Clear form
            document.getElementById("newKeyForm").reset()
        } else {
            console.error('Failed to create key');
            document.getElementById('result').innerHTML = 'Failed to create key';
        }
    };
    xhr.send(formData);
});

function delete_key(project_id, key_id) {
    project_id = parseInt(project_id, 10);
    key_id = parseInt(key_id, 10);
    fetch(`/delete_key/${project_id}/${key_id}`, {
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
            console.log('Key deleted successfully.');
            var table_id = 'KeyID' + key_id;
            var delete_table = document.getElementById(table_id);
            if (delete_table) {
                delete_table.parentNode.removeChild(delete_table);
            }
        } else {
            console.error(data.message);
        }
    })
    .catch(error => console.error('Erro ao excluir o projeto:', error));
}