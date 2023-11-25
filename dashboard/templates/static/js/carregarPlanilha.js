function updateProgressBar(percentComplete) {
    var progressBar = document.getElementById('uploadProgress');
    progressBar.style.width = percentComplete + '%';
}

function uploadFile() {

    var input = document.getElementById('fileInput');
    var file = input.files[0];

    if (file) {
        var formData = new FormData();
        formData.append('file', file);
        url = "upload_planilha"
        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"), 
            },

        })
        .then(response => response.json())
        .then(data => {
            console.log('Upload bem-sucedido:', data);

            
        })
        .catch(error => {
            console.error('Erro no upload:', error);
            // Adicione aqui qualquer lógica para lidar com erros durante o upload
        });
    } else {
        console.error('Nenhum arquivo selecionado.');
    }
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


