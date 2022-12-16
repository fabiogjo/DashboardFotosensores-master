Chart.register(ChartDataLabels);


function renderiza_tickets_por_tipo(url){

    const labels = []
    const values = []

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

    var size = Object.keys(data).length;
    for (var i = 0; i < size; i++) {

        if(data[i]['tipo__count'] > 5) {
            labels.push(data[i]['tipo']);
            values.push(data[i]['tipo__count']);
        }
    }
    const myChart = new Chart(tickets_por_tipo, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Chamados',
            barPercentage: 1,
            barThickness: 30,
            maxBarThickness: 50,
            minBarLength: 5,
            data: values,
            backgroundColor:
                'rgba(16, 0, 62, 1)',

            borderColor: [
                'rgba(0, 0, 0, 1)',
            ],
            borderWidth: 1
        }]

    },
        options: {
            plugins: {
                legend:{
                    display: false
                },
                title:{
                    display: true,
                    color: '#000',
                    text: 'Contagem de tickets por tipo',

                },
                datalabels:{

                    color: '#FFF'

                }
            },

            responsive: true,
            indexAxis: 'x',
            scales: {
                x: {
                    ticks:{
                        autoSkip: false,
                        color: '#000',
                        font:{
                            size: 10

                        }
                    },
                    grid:{
                        color: '#FFF'
                    }

                },
                y: {
                    grid:{
                        borderDash: [5,5],
                        color: '#000'
                    },
                    ticks:{

                        autoSkip: true,
                        maxTicksLimit: 8,
                        min: 0,
                        stepSize: 5

                    }
                }
            }
        }
    });
})
}


function renderiza_tickets_por_setor(url){

    const labels = []
    const values = []

    fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){

    var size = Object.keys(data).length;
    for (var i = 0; i < size; i++) {
        if(data[i]['ticket_freshdesk__count'] > 1) {
        labels.push(data[i]['lote']);
        values.push(data[i]['ticket_freshdesk__count']);
        }

    }

    const chart_tickets_por_setor = new Chart(tickets_por_setor, {
    type: 'doughnut',
    data: {
        labels: ['Lote ' + labels[0], 'Lote ' + labels[1], 'Lote ' + labels[2]],
        datasets: [{
            label: 'Chamados',
            data: values,
            backgroundColor: ['rgba(16, 0, 62, 1)', 'rgba(69, 76, 116, 0.8)', 'rgba(213, 217, 238, 0.8)'],
        }]
    },
        options: {
            plugins: {
                legend:{
                    display: true,
                    position: 'top'
                },
                title:{
                    display: true,
                    color: '#000',
                    text: 'Contagem de tickets por lote',

                },
                datalabels:{

                    color: '#FFF'

                }
            },
            responsive: true,
            scales: {
                x: {
                    ticks:{
                        display: false,
                        autoSkip: false,
                        font:{
                            size: 15
                        }
                    },
                    grid:{
                        display: false
                    }

                },
                y: {
                    grid:{
                        display: false

                    },
                    ticks:{
                        display: false,
                        autoSkip: true,

                    }
                }
            }
        }
    });
})
}


function renderiza_tarefas_por_tecnico(url){

    const labels = []
    const values = []

    fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){

    var size = Object.keys(data).length;
    for (var i = 0; i < size; i++) {
        if(data[i]['id_ticket__count'] >= 5) {
        labels.push(data[i]['agente']);
        values.push(data[i]['id_ticket__count']);
        }

    }

    const chart_tarefas_por_tecnico = new Chart(tarefas_por_tecnico, {
    type: 'bar',
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Chamados',
            barPercentage: 1,
            barThickness: 15,
            maxBarThickness: 15,
            minBarLength: 5,
            data: values,
            backgroundColor:
                'rgba(16, 0, 62, 1)',

            borderColor: [
                'rgba(0, 0, 0, 1)',
            ],
            borderWidth: 1
        }]

    },
        options: {
            plugins: {
                legend:{
                    display: false
                },
                title:{
                    display: true,
                    color: '#000',
                    text: 'Tickets por agente',

                },
                datalabels:{

                    color: '#FFF'

                }
            },

            responsive: true,
            indexAxis: 'y',
            scales: {
                x: {
                    ticks:{
                        autoSkip: false,
                        color: '#000',
                        font:{
                            size: 0

                        }
                    },
                    grid:{
                        color: '#FFF'
                    }

                },
                y: {
                    grid:{
                        borderDash: [0,0],
                        color: ''
                    },
                    ticks:{

                        autoSkip: false,
                        maxTicksLimit: 8,
                        min: 0,
                        stepSize: 5

                    }
                }
            }
        }
    });
})
}


function renderiza_paralisacoes_x_desparalisacoes(url){


    month = {
        '1':'Janeiro',
		'2':'Fevereiro',
		'3':'Março',
		'4':'Abril',
		'5':'Maio',
		'6':'Junho',
		'7':'Julho',
		'8':'Agosto',
		'9':'Setembro',
		'10':'Outubro',
		'11':'Novembro',
		'12':'Dezembro'		}


    const labels = []
    const paralisados = []
    const desparalisados = []

    fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){

    var size = Object.keys(data).length;
    for (var i = 0; i < size; i++) {
        if(data[i]['year'] == 2022) {
        labels.push(month[data[i]['month']]);
        paralisados.push(data[i]['paralisados']);
        desparalisados.push(data[i]['desparalisados']);
        }

    }

    const chart_paralisacoes_x_desparalisacoes = new Chart(paralisacoes_x_desparalisacoes, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Paralisados',
            barPercentage: 1,
            barThickness: 30,
            maxBarThickness: 30,
            minBarLength: 5,
            data: paralisados,
            backgroundColor:
                'rgba(16, 0, 62, 1)',

            borderColor: [
                'rgba(0, 0, 0, 1)',
            ],
            borderWidth: 1
        },{
            label: 'Desparalisados',
            barPercentage: 1,
            barThickness: 30,
            maxBarThickness: 30,
            minBarLength: 5,
            data: desparalisados,
            backgroundColor:
                'rgba(69, 76, 116, 0.8)',

            borderColor: [
                'rgba(0, 0, 0, 1)',
            ],
            borderWidth: 1
        }]

    },
        options: {
            plugins: {
                legend:{
                    display: true
                },
                title:{
                    display: true,
                    color: '#000',
                    text: 'Paralisações por mês',

                },
                datalabels:{

                    color: '#000',
                    anchor: 'end',
                    align: 'top'
                }
            },

            responsive: true,
            indexAxis: 'x',
            scales: {
                x: {
                    ticks:{
                        autoSkip: false,
                        color: '#000',
                        font:{
                            size: 10

                        }
                    },
                    grid:{
                        color: '#FFF'
                    }

                },
                y: {
                    grid:{
                        borderDash: [5,5],
                        color: '#000'
                    },
                    ticks:{

                        autoSkip: false,
                        maxTicksLimit: 12,
                        min: 0,
                        stepSize: 5

                    }
                }
            }
        }
    });
})
}


function renderiza_indice_desempenho(url){

    const labels = []
    const values_cev = []
    const values_rev = []

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

    var size = Object.keys(data).length;

    for (var i = 0; i < size; i++) {

        if(data[i]['municipio__setor__responsavel__nome'] != null) {



            if(data[i]['tipo_equipamento'] == 'CEV') {
                labels.push(data[i]['municipio__setor__responsavel__nome']);
                values_cev.push(data[i]['media']);

            }else{

                values_rev.push(data[i]['media']);

            }
        }
    }

    const chart_indice_por_tecnico = new Chart(graph_indice_desempenho, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'CEV',
            barPercentage: 1,
            barThickness: 25,
            maxBarThickness: 25,
            minBarLength: 5,
            data: values_cev,
            backgroundColor:
                'rgba(8, 14, 44)',

            borderColor: [
                'rgba(0, 0, 0, 0)',
            ],
            borderWidth: 1
        },{
            label: 'REV',
            barPercentage: 1,
            barThickness: 25,
            maxBarThickness: 25,
            minBarLength: 5,
            data: values_rev,
            backgroundColor:
                'rgba(40, 67, 135)',

            borderColor: [
                'rgba(0, 0, 0, 0)',
            ],
            borderWidth: 1
        }]

    },
        options: {
            plugins: {
                legend:{
                    display: true,
                    labels:{
                        color: '#000',
                        weight: 'bold'
                    }

                },
                title:{
                    display: true,
                    color: '#000',
                    text: 'Indice de desempenho',
                    font:{

                        size: 13

                    }

                },
                datalabels:{

                    color: '#fff',
                    font:{
                            size: 10,
                            weight: 'bold',

                        },

                    align: 'top'

                }
            },

            responsive: true,
            indexAxis: 'x',
            scales: {
                x: {
                    ticks:{
                        autoSkip: false,
                        color: '#000',
                        font:{
                            size: 10,
                            weight: 'bold'

                        }
                    },
                    grid:{
                        color: '#FFF'
                    }

                },
                y: {
                    grid:{
                        borderDash: [5,5],
                        color: '#000',
                        stepSize: 5
                    },
                    ticks:{

                        autoSkip: true,
                        maxTicksLimit: 5,
                        min: 0,
                        max: 2,
                        stepSize: 0.25,
                        color: '#000',
                        font:{
                            size: 11,
                            weight: 'bold'


                        }

                    }
                }
            }
        }
    });
})
}


function renderiza_faixas_por_setor(url){

    const labels = []
    const values = []

    fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){

    var size = Object.keys(data).length;
    for (var i = 0; i < 8; i++) {

        labels.push(data[i]['municipio__setor']);
        values.push(data[i]['numero_de_serie__count']);

    }

    const chart_graph_faixas_por_setor = new Chart(graph_faixas_por_setor, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Faixas',

            categoryPercentage: 1,
            barPercentage: 2,
            borderWidth: 20,
            minBarLength: 50,
            maintainAspectRatio: false,
            data: values,
            backgroundColor:
                'rgba(16, 0, 62, 1)',

            borderColor: [
                'rgba(0, 0, 0, 1)',
            ],
            borderWidth: 1
        }]

    },
        options: {
            layout:{

                padding: 20

            },
            plugins: {
                legend:{
                    display: false
                },
                title:{
                    display: true,
                    color: '#000',
                    text: 'Tickets por agente',

                },
                datalabels:{

                    color: '#FFF'

                }
            },

            responsive: true,
            indexAxis: 'y',
            scales: {
                x: {
                    ticks:{
                        autoSkip: false,
                        color: '#000',
                        font:{
                            size: 0

                        }
                    },
                    grid:{
                        color: '#FFF'
                    }

                },
                y: {
                    grid:{
                        borderDash: [0,0],
                        color: ''
                    },
                    ticks:{

                        autoSkip: false,
                        maxTicksLimit: 8,
                        min: 0,
                        stepSize: 5,



                    }
                }
            }
        }
    });
})
}

