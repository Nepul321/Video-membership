const root = document.getElementById("root");
const container = document.querySelector(".container");

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function getVideos() {
  const data = container.dataset;
  const id = data.id;
  const method = "GET";
  const endpoint = `/api/playlists/videos-not-in-playlist/${id}/`;
  const xhr = new XMLHttpRequest();
  xhr.open(method, endpoint);
  xhr.onload = () => {
    if (xhr.status === 200) {
      const response = xhr.response;
      const responseData = JSON.parse(response);
      insertVideos(responseData);
    } else {
      alert("An error occurred");
    }
  };

  xhr.onerror = () => {
    alert("Please try again.");
  };

  xhr.send();
}

function updateHtmlonchange(id) {
 const element = document.getElementById(`video-${id}`)
 if (element) {
     root.removeChild(element)
 }
}

function addvideostoPlayList(id, action) {
  const video_id = id;
  const playlist_id = container.dataset.id;
  const method = "POST";
  const endpoint = `/api/playlists/add-video-to-playlist/`;
  const data = {
    video_id: video_id,
    playlist_id: playlist_id,
    action: action
  };
  const xhr = new XMLHttpRequest();
  const csrftoken = getCookie("csrftoken");
  xhr.open(method, endpoint);
  xhr.setRequestHeader("Content-Type", "application/json");
  if (csrftoken) {
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
  xhr.onload = () => {
    if (xhr.status === 200) {
      alert("Added successfully");
      updateHtmlonchange(video_id);
    } else if (xhr.status === 404) {
      const response = JSON.parse(xhr.response);
      const message = response.message;
      alert(message);
    } else if (xhr.status === 401 || xhr.status === 403) {
      alert("Forbidden.");
    } else if(xhr.status === 400) {
        alert("Bad request");
    } else if (xhr.status === 500) {
      alert("An error occurred. Please try again.");
    }
  };

  xhr.onerror = () => {
    alert("Please try again.");
  };

  xhr.send(JSON.stringify(data));
}

function insertVideos(data) {
  data.forEach((item) => {
    const card = document.createElement("div");
    card.className = "card mb-3";
    card.id = `video-${item.id}`;
    const row = document.createElement("div");
    row.className = "row g-0";
    const column = document.createElement("div");
    column.className = "col-md-4";
    const column_2 = document.createElement("div");
    column_2.className = "col-md-8";
    const card_body = document.createElement("div");
    card_body.className = "card-body";

    column.innerHTML = `
    <img src=${item.thumbnail_image} class="img-fluid rounded-start" alt="..." />
    `;

    card_body.innerHTML = `
    <p style="font-size: 25px;" class="card-title"><a href="/videos/${item.id}/">${item.title}</a></p>
    <p>Views : ${item.views}</p>
    <button class="btn btn-primary" onclick="addvideostoPlayList(${item.id}, 'add')">Add to playlist</button>
    <p class="small text-muted">${item.date}</p>
    `;
    column_2.appendChild(card_body);

    row.appendChild(column);
    row.appendChild(column_2);
    card.appendChild(row);

    root.appendChild(card);
  });
}

getVideos();
