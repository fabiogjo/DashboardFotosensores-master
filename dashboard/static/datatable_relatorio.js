$(document).ready( function () {
    tbl_paralisados = $('#tblSolvedTickets').DataTable({
        dom: 'Bfrtip',
        buttons:['copy', 'csv', 'excel', 'pdf', 'print'],
        ajax: '/relatorios/get_all_tickets',
        "columns": [
            { "data": "id" },
            { "data": "assunto" },
            { "data": "grupo"},
            { "data": "data_criacao" },
            { "data": "agente" },
            { "data": "paralisado" },
        ],

    });

});

