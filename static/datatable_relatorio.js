$(document).ready(function() {
    $('#tblSolvedTickets').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "{% url 'solved_tickets' %}",
        dom: 'Bfrtip',
        buttons: [
            'excel', 'pdf'
        ]
    });
});
