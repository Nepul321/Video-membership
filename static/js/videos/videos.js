const root = document.getElementById("root")
const form = document.getElementById("form")

function getVideos() {
    const xhr = new XMLHttpRequest();
    const method = "GET";
    const url = '/api/videos/'
    xhr.open(method, url)
    xhr.onload = () => {
       const serverResponse = xhr.response;
       var listedItems = serverResponse;
       if (xhr.status === 200) {
           listedItems = JSON.parse(listedItems)
           insertVideos(listedItems);
       } else {
           alert("An error occured")
       }
    }
   
    xhr.send();
}

function addNewPost(item) {
    const card_correct = document.createElement("div")
    const card = document.createElement("div")
    card.className = "card mb-3"
    const row = document.createElement("div")
    row.className = "row g-0"
    const column = document.createElement("div")
    column.className = "col-md-4"
    const column_2 = document.createElement("div")
    column_2.className = "col-md-8"
    const card_body = document.createElement("div")
    card_body.className = "card-body"
    
    column.innerHTML = `
    <img src=${item.thumbnail_image} class="img-fluid rounded-start" alt="..." />
    `

    card_body.innerHTML = `
    <p style="font-size: 25px;" class="card-title"><a href="/videos/${item.id}/">${item.title}</a></p>
    <p>Views : ${item.views}</p>
    <p class="small text-muted">${item.date}</p>
    `
    column_2.appendChild(card_body)

    row.appendChild(column)
    row.appendChild(column_2)
    card.appendChild(row)

    card_correct.appendChild(card)

    return card_correct.innerHTML
}

if (form) {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);
        const endpoint = `/api/videos/create/`;
        const method = "POST";
        const xhr = new XMLHttpRequest();
        xhr.open(method, endpoint)
        xhr.onload = () => {
            if (xhr.status === 201) {
                const responseData = JSON.parse(xhr.response)
                if (responseData.is_superuser === true) {
                    root.innerHTML = addNewPost(responseData) + root.innerHTML
                }
              } else if(xhr.status === 400) {
                alert("Input empty or Post too long")
              } else if (xhr.status === 401 || xhr.status === 403) {
                alert("Authentication error");
                window.location.href = "/accounts/login/?next=/";
              } else if (xhr.status === 500) {
                alert("Please try again");
              }
              form.reset();
        }
    
        xhr.onerror = () => {
            alert("An error occurred. Please try again")
        }
    
        xhr.send(formData)
    
    
    
    })
}


function insertVideos(data) {
        data.forEach((item) => {
        const card = document.createElement("div")
        card.className = "card mb-3"
        const row = document.createElement("div")
        row.className = "row g-0"
        const column = document.createElement("div")
        column.className = "col-md-4"
        const column_2 = document.createElement("div")
        column_2.className = "col-md-8"
        const card_body = document.createElement("div")
        card_body.className = "card-body"
        
        column.innerHTML = `
        <img src=${item.thumbnail_image} class="img-fluid rounded-start" alt="..." />
        `

        card_body.innerHTML = `
        <p style="font-size: 25px;" class="card-title"><a href="/videos/${item.id}/">${item.title}</a></p>
        <p>Views : ${item.views}</p>
        <p class="small text-muted">${item.date}</p>
        `
        column_2.appendChild(card_body)

        row.appendChild(column)
        row.appendChild(column_2)
        card.appendChild(row)

        root.appendChild(card)


    })
}

getVideos();