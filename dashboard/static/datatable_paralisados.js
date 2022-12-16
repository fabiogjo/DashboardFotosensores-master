
   $(document).ready( function () {
            tbl_paralisados = $('#tbl_paralisados').DataTable({
                dom: 'Bfrtip',
                buttons:['copy', 'csv', 'excel', 'pdf', 'print'],
                ajax: '/json_paralisados',
                "columns":[
                    {"data":"id", },
                    {"data": "lote"},
                    {"data": "serial"},
                    {"data": "municipio"},
                    {"data": "codigo"},
                    {"data": "faixa"},
                    {"data": "data_abertura"},
                    {"data": "data_encerramento"},
                    {"data": "motivo"},
                    {"data":null,

                    render:function(data, type, row)
                    {
                      var status = "";
                      if (data.status == "Em Análise (Encerramento)" || data.status == "Em Análise (Início)") {

                                status = "pending";

                            } else if (data.status == "Deferida (Encerramento)") {

                                status = "delivered";

                            } else if (data.status == "Indeferida (Início)" || data.status == "Indeferida (Encerramento)" || data.status == "Deferida (Início)") {

                                status = "return";

                            }
                            return '<button type="button" id="a" class="status '+ status +'" data-toggle="modal" data-target="#exampleModal" data-serial="'+ data.serial + '" data-municipio="'+ data.municipio +'" data-faixa="'+ data.faixa + '" data-Motivo="'+data.motivo+'" data-data_de_abertura="'+ data.data_abertura +'" data-data_de_encerramento="'+data.data_encerramento+'" data-status="'+data.status+'" data-id="'+data.id+'">' +data.status+ '</button>';

                        }
                      },

                ],
                "columnDefs": [
                    {
                     "targets": [0],
                     "visible": false,
                     "searchable": false
                     },

                ],




            });

    });


        function format(dataChild) {
            // `d` is the original data object for the row
            return (
                '<table cellpadding="5" cellspacing="0" border="2" style="padding-left:50px;">' +
                '<tr>' +
                    '<td>' +
                    'ALGUM TEXTO INFORMANDO A TRATATIVA DO EQUIPAMENTO' +
                    '</td>' +

                '</tr>' +
                '</table>'
            );
        }

        $('#tbl_paralisados tbody').on( 'click', 'tr', function () {
            var data = tbl_paralisados.row( $(this).parents('tr') ).data();
             var tr = $(this).closest('tr');
        var row = tbl_paralisados.row(tr);

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