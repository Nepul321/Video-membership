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
    console.log(data)
}

getVideos();