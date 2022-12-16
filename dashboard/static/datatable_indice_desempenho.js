// DATATABLE INDICE DESEMPENHO

        data_indice_desempenho = {
                "ajax":"/json_indice_desempenho",
                "columns":[
                    {"data": "serial"},
                    {"data": "municipio"},
                    {"data": "codigo"},
                    {"data": "faixa"},
                    {"data": "indice_desempenho"},

                ],

            }

        dataChild = {
            "ajax":"/json_indice_desempenho",
            "columns":[
                    {"data": "icid"},
                    {"data": "icin"},
                    {"data": "idf"},
                    {"data": "ilpd"},
                    {"data": "ilpn"},
                    {"data": "ievri"},
                    {"data": "ievdt"},
                    {"data": "ievdt"},

            ],

        }

        function format(dataChild) {
            // `d` is the original data object for the row
            return (
                '<table cellpadding="5" cellspacing="0" border="2" style="padding-left:50px;">' +
                '<tr>' +
                    '<td>Disponibilidade:</td>' +
                    '<td>' +
                    dataChild.idf +
                    '</td>' +
                    '<td>Imagem Diurna:</td>' +
                    '<td>' +
                    dataChild.icid +
                    '</td>' +
                    '<td>Imagem Noturna:</td>' +
                    '<td>' +
                    dataChild.icin +
                    '</td>' +

                    '<td>OCR Diurno:</td>' +
                    '<td>' +
                    dataChild.ilpd +
                    '</td>' +
                '</tr>' +
                '<tr>' +

                    '<td>OCR Noturno:</td>' +
                    '<td>' +
                    dataChild.ilpn +
                    '</td>' +

                    '<td>IEVri:</td>' +
                    '<td>' +
                    dataChild.ievri +
                    '</td>' +

                    '<td>IEVdt:</td>' +
                    '<td>' +
                    dataChild.ievdt +
                    '</td>' +

                    '<td>ICV:</td>' +
                    '<td>' +
                    dataChild.icv +
                    '</td>' +

                '</tr>' +
                '<tr>' +

                '</tr>' +
                '</table>'
            );
        }


        $(document).ready( function () {
            tbl_indice_desempenho = $('#tbl_indice_desempenho').DataTable({ 
                dom: 'Bfrtip',
                buttons:['copy', 'csv', 'excel', 'pdf', 'print'],
                ajax:"/json_indice_desempenho",
                "columns":[
                    {"data": "serial"},
                    {"data": "municipio"},
                    {"data": "codigo"},
                    {"data": "faixa"},
                    {"data": "indice_desempenho"},

                ],
            
            
            
            });
        });

        $('#tbl_indice_desempenho tbody').on( 'click', 'tr', function () {
            var data = tbl_indice_desempenho.row( $(this).parents('tr') ).data();
             var tr = $(this).closest('tr');
        var row = tbl_indice_desempenho.row(tr);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        } else {
            // Open this row
            row.child(format(row.data())).show();
            tr.addClass('shown');

        }
    });