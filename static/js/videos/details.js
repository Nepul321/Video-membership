const deleteBtn = document.getElementById("delete");
const container = document.getElementById("data");

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

if (deleteBtn) {
  deleteBtn.addEventListener("click", () => {
    const data = container.dataset;
    const id = data.id;
    const method = "DELETE";
    const endpoint = `/api/videos/${id}/`;
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
        alert(response.message);
        window.location.href = "/videos/";
      } else if (xhr.status === 404) {
        alert("Video not found");
      } else if (xhr.status === 500) {
        alert("An error occurred. Please try again.");
      }
    };

    xhr.onerror = () => {
      alert("Please try again.");
    };

    xhr.send();
  });
}
