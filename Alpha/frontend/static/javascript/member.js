document.getElementById('newMemberForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    var user_id = document.getElementById('user_id').value;
    var project_id = document.getElementById('project_id').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_member/', true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); 
    var formData = new FormData();
    formData.append('user_id', user_id);
    formData.append('project_id', project_id);
    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        if (response.success) {
            console.log('New member added successfully! ID #', response.member_id);
            document.getElementById('result').innerHTML = 'New member added successfully: ID #' + response.member_id;
            var get_table = document.getElementById('MemberTable');

            var new_table = '<tr class="tb-height" id="MemberID' + response.member_id + '">';
            var td_1 = '<td>' + response.member_first_name + ' '+ response.member_last_name + '</td>';
            var td_2 = '<td>' + response.member_username +'</td>';
            var td_3 = '<td>' +  response.member_email +'</td>';
            var td_4 = '<td>' +  'Development' +'</td>'; 
            var td_5 = '<td>' +  '<i class="bx bxs-x-circle btn-delete" onclick="delete_member('+ project_id + ','+ response.member_id + ')"></i>' +'</td></tr>';
            new_table += td_1 + td_2 + td_3 + td_4 + td_5;
            get_table.innerHTML += new_table;
        } else {
            console.error('Failed to add new member.');
            document.getElementById('result').innerHTML = 'Failed to add new member.';
        }
    };
    xhr.send(formData);
});


function delete_member(projectId, user_id) {
    projectId = parseInt(projectId, 10);
    user_id = parseInt(user_id, 10);
    fetch(`/delete_member/${projectId}/${user_id}`, {
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
            console.log('Member deleted successfully.');
            var table_id = 'MemberID' + user_id;
            var delete_table = document.getElementById(table_id);
            if (delete_table) {
                delete_table.parentNode.removeChild(delete_table);
            }
        } else {
            console.error(data.message);
        }
    })
    .catch(error => console.error('Failed to delete member: ', error));
}