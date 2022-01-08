const deleteBtn = document.getElementById("deleteBtn");
const form = document.getElementById("form");

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

if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const form = e.target
    const formData = new FormData(form)
    const method = "POST"
    const data = deleteBtn.dataset
    const id = data.id
    const endpoint = `/api/playlists/${id}/`
    const xhr = new XMLHttpRequest();
    xhr.open(method, endpoint)
    
    xhr.onload = () => {
      if (xhr.status === 200) {
        const responseData = JSON.parse(xhr.response)
        const title = responseData.title
        document.getElementById("title").textContent = title
      } else if (xhr.status === 401 || xhr.status === 403) {
        alert("Authentication error");
        window.location.href = "/accounts/login/?next=/";
      } else if (xhr.status === 500) {
        alert("Please try again");
      }
    }

    xhr.onerror = () => {
      alert("Please try again.")
    }

    xhr.send(formData)
  })
}

if (deleteBtn) {
  deleteBtn.addEventListener("click", () => {
    const data = deleteBtn.dataset;
    const id = data.id;
    const method = "DELETE";
    const endpoint = `/api/playlists/${id}/`;
    const xhr = new XMLHttpRequest();
    const csrftoken = getCookie("csrftoken");
    xhr.open(method, endpoint);
    xhr.setRequestHeader("Content-Type", "application/json");
    if (csrftoken) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }

    xhr.onload = () => {
      if (xhr.status === 200) {
        const response = JSON.parse(xhr.response);
        const message = response.message;
        alert(message);
        window.location.href = "/playlists/";
      } else if (xhr.status === 404) {
        alert("Playlist not found");
      } else if (xhr.status === 500) {
        alert("An error occurred. Please  try again.");
      }
    };

    xhr.onerror = () => {
      alert("Please try again.");
    };

    xhr.send();
  });
}
