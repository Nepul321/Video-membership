const root = document.getElementById("root");
const form = document.getElementById("form");

function getPlaylists() {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "/api/playlists/";
  xhr.open(method, url);
  xhr.onload = () => {
    const serverResponse = xhr.response;
    var listedItems = serverResponse;
    if (xhr.status === 200) {
      listedItems = JSON.parse(listedItems);
      insertPlaylists(listedItems);
    } else {
      alert("An error occured");
    }
  };

  xhr.send();
}

function addNewPlayList(item) {
  const card_ = document.createElement("div");
  const card = document.createElement("div");
  card.className = "card mb-3";
  const row = document.createElement("div");
  row.className = "row g-0";
  const column = document.createElement("div");
  column.className = "col-md-4";
  const column_2 = document.createElement("div");
  column_2.className = "col-md-8";
  const card_body = document.createElement("div");
  card_body.className = "card-body";

  column.innerHTML = `
    <img src=${item.thumbnail} class="img-fluid rounded-start" alt="..." />
    `;

  card_body.innerHTML = `
    <p style="font-size: 25px;" class="card-title"><a href="/playlists/${item.id}/">${item.title}</a></p>
    <p class="small text-muted">${item.date}</p>
    `;
  column_2.appendChild(card_body);

  row.appendChild(column);
  row.appendChild(column_2);
  card.appendChild(row);

  card_.appendChild(card);
  return card_.innerHTML;
}

if (form) {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const method = "POST";
    const endpoint = "/api/playlists/create/";
    const xhr = new XMLHttpRequest();
    xhr.open(method, endpoint);
    xhr.onload = () => {
      if (xhr.status === 201) {
        const responseData = JSON.parse(xhr.response);
        root.innerHTML = addNewPlayList(responseData) + root.innerHTML;
      } else if (xhr.status === 401 || xhr.status === 403) {
        alert("Forbidden.");
      } else if (xhr.status === 500) {
        alert("Please try again");
      }
      form.reset();
    };

    xhr.onerror = () => {
      alert("An error occurred. Please try again");
    };

    xhr.send(formData);
  });
}

function insertPlaylists(data) {
  data.forEach((item) => {
    const card = document.createElement("div");
    card.className = "card mb-3";
    const row = document.createElement("div");
    row.className = "row g-0";
    const column = document.createElement("div");
    column.className = "col-md-4";
    const column_2 = document.createElement("div");
    column_2.className = "col-md-8";
    const card_body = document.createElement("div");
    card_body.className = "card-body";

    column.innerHTML = `
            <img src=${item.thumbnail} class="img-fluid rounded-start" alt="..." />
            `;

    card_body.innerHTML = `
            <p style="font-size: 25px;" class="card-title"><a href="/playlists/${item.id}/">${item.title}</a></p>
            <p class="small text-muted">${item.date}</p>
            `;
    column_2.appendChild(card_body);

    row.appendChild(column);
    row.appendChild(column_2);
    card.appendChild(row);

    root.appendChild(card);
  });
}

getPlaylists();
