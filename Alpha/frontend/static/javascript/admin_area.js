
function delete_user(user_id) {
    user_id = parseInt(user_id, 10);
    fetch(`/admin_area/delete_user/${user_id}/`, {
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
            console.log('User deleted successfully.');
            document.getElementById('result_user').innerHTML = data.result_user;
            var table_id = 'tableUser' + user_id
            var delete_table = document.getElementById(table_id);
            if (delete_table) {
                delete_table.parentNode.removeChild(delete_table);
            }
        } else {
            document.getElementById('result_user').innerHTML = data.result_user;
            console.error(data.result_user);
        }
    })
    .catch(error => console.error('Failed to delete user: ', error));
}