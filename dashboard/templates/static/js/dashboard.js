document.getElementById("botaoBuscar").addEventListener("click", function() {
    
    renderiza_info_materia()
    
  });

document.getElementById("download_pdf_impar").addEventListener("click", function() {

    semestre = "Ímpar"
    
    downloadPDF(`/generate_pdf/?semestre=${semestre}`)
    
  });

document.getElementById("download_pdf_par").addEventListener("click", function() {

    semestre = "Par"

    downloadPDF(`/generate_pdf/?semestre=${semestre}`)

});


var myChart_info;

function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 170;
        let g = Math.random() * 170;
        let b = Math.random() * 170;
        bg_color.push(`rgba(${r}, ${g}, ${b})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}

function renderiza_lista_materias_atrasados_par(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const ctx = document.getElementById('atrasados_disciplinas_par').getContext('2d');
       
        let labels = []
        let dados = []
        
        for (const chave in data) {
            labels.push(chave);
            dados.push(data[chave]);
        }

        var cores_produtos_mais_vendidos = gera_cor(qtd=20)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    data: dados,
                    backgroundColor: cores_produtos_mais_vendidos[0],
                    borderColor: cores_produtos_mais_vendidos[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });


    })
  
}

function renderiza_lista_materias_atrasados_impar(url){

    
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const ctx = document.getElementById('atrasados_disciplinas_impar').getContext('2d');
       
        let labels = []
        let dados = []
        
        for (const chave in data) {
            labels.push(chave);
            dados.push(data[chave]);
        }

        var cores_produtos_mais_vendidos = gera_cor(qtd=20)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    data: dados,
                    backgroundColor: cores_produtos_mais_vendidos[0],
                    borderColor: cores_produtos_mais_vendidos[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });


    })
  
}

function renderiza_info_materia(url) {

    var valorInput = document.getElementById("meuInput").value;

    document.getElementById("codmat").innerHTML = valorInput

    var codigo = valorInput;

    var url = `/retorna_info_materia/?codigo=${codigo}`;

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const ctx = document.getElementById('informaçao_disciplina').getContext('2d');
        console.log(data)
        let labels = []
        let dados = []
        
        if (myChart_info) {
            myChart_info.destroy(); // Destrua o gráfico anterior
        }


        labels = ["alunos cursando", "alunos a cursar - período ideal", "alunos a cursar - atrasados"]
        dados = [data[labels[0]], data[labels[1]], data[labels[2]]]
        
        var cores_produtos_mais_vendidos = gera_cor(qtd=4)
        myChart_info = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: dados,
                    backgroundColor: cores_produtos_mais_vendidos[0],
                    borderColor: cores_produtos_mais_vendidos[1],
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    legend: {
                        labels: {
                            font: {
                                color: 'black',
                                size: '20'
                            }
                        }
                    }
                }
            }
            
        });


    })
  
}

function downloadPDF(url) {
    fetch(url)
        .then(response => response.blob())
        .then(blob => {
            var url = window.URL.createObjectURL(blob);
            var a = document.createElement('a');
            a.href = url;
            a.download = 'relatorio.pdf';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        });
}

function carregarTabela(url) {
    var tbody = document.querySelector('#tabela tbody');

    // Limpar o conteúdo anterior da tabela
    tbody.innerHTML = '';

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
    //Preencher a tabela com os dados
    
    aluno =  {}
    for (const chave in data) {
        aluno[chave.substring(0,11)] = [data[chave], chave.slice(-4)]
    }

    // Converter o objeto em uma matriz de pares chave-valor
    var dataArray = Object.entries(aluno);

    // Ordenar a matriz com base nos valores (índice 1)
    dataArray.sort(function(a, b) {
        return b[1][0] - a[1][0];
    });

    // Reconstruir o objeto a partir da matriz ordenada
    aluno = Object.fromEntries(dataArray.slice(0,10));


    for (var alunoKey in aluno) {
        if (aluno.hasOwnProperty(alunoKey)) {
            var disciplinasAtrasadas = aluno[alunoKey];
            var row = tbody.insertRow();
            var cellAluno = row.insertCell(0);
            var cellDisciplinas = row.insertCell(1);
            var anoIngresso = row.insertCell(2)

            cellAluno.textContent = alunoKey;
            cellDisciplinas.textContent = disciplinasAtrasadas[0];
            anoIngresso.textContent = disciplinasAtrasadas[1]
        }
    }
    
    })

    
}
