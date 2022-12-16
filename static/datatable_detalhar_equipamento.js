    $(document).ready( function () {
            tbl_detalhar_equipamento = $('#tbl_detalhar_equipamento').DataTable({
                dom: 'Bfrtip',
                buttons:['copy', 'csv', 'excel', 'pdf', 'print'],
                ajax: '/json_equipamentos',
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
                     }
                ],




            });

    });