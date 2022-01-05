const root = document.getElementById("root")

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
        <p style="font-size: 25px;" class="card-title"><a href="">${item.title}</a></p>
        <p class="card-text">${item.description}</p>
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