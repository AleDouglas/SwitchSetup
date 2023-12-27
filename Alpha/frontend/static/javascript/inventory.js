document.getElementById('createInventoryForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    var title = document.getElementById('inventoryTitle').value;
    var description = document.getElementById('inventoryDescription').value;
    var inventoryFile = document.getElementById('inventoryFile').files[0]; 
    var projectId = document.getElementById('projectId').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_inventory/', true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); 
    var formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('inventory_file', inventoryFile);
    formData.append('project_id', projectId);

    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        if (response.success) {
            var close_modal = document.getElementById('close_modal');
            close_modal.click()
            console.log('Inventory create successfully! ID:', response.inventory_id);
            document.getElementById('result').innerHTML = 'Inventory create successfully! ID: ' + response.inventory_id;
            var get_table = document.getElementById('inventoryTable');
            const data = new Date(response.inventory_time);
            const options = {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
                hour12: true,
            };
            const date_time = new Intl.DateTimeFormat('en-US', options).format(data);
            var new_table = '<tr class="tb-height" id="inventoryID'+ response.inventory_id +'"><td>' +  response.inventory_title + '<span style="color: grey;"> #' + response.inventory_id + '</span></td><td>' + response.inventory_description + '</td><td>' + date_time + '<td><i class="bx bxs-x-circle btn-delete" onclick="delete_inventory(' + projectId + ',' + response.inventory_id + ')"></i></td></tr>';
            get_table.innerHTML += new_table;

            //Clear form
            document.getElementById("createInventoryForm").reset()
        } else {
            console.error('Failed to create inventory');
            document.getElementById('result').innerHTML = 'Failed to create inventory';
        }
    };
    xhr.send(formData);
});


function delete_inventory(projectId, inventoryId) {
    projectId = parseInt(projectId, 10);
    inventoryId = parseInt(inventoryId, 10);
    fetch(`/delete_inventory/${projectId}/${inventoryId}`, {
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
            console.log('Inventory deleted successfully.');
            var table_id = 'inventoryID' + inventoryId
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